from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple
import numpy as np
import pandas as pd

from .optimizers import (
	negative_sharpe_ratio,
	portfolio_volatility,
)


@dataclass
class BacktestParams:
	lookback_window_days: int = 252
	rebalance_frequency_days: int = 21
	risk_free_rate: float = 0.02


def rolling_backtest(
	prices: pd.DataFrame,
	optimize_fn: Callable[[pd.Series, pd.DataFrame, float], np.ndarray],
	params: BacktestParams,
)	-> Dict[str, List]:
	"""Generic rolling backtest with monthly rebalancing and one-period-ahead evaluation.

	optimize_fn must return a weight vector for the training window.
	"""
	log_returns = np.log(prices / prices.shift(1)).dropna()
	start_date = prices.index[params.lookback_window_days]
	end_date = prices.index[-1]

	results = {"returns": [], "weights_history": [], "dates": []}
	n_assets = prices.shape[1]

	for i in range(0, len(prices) - params.lookback_window_days, params.rebalance_frequency_days):
		train = log_returns.iloc[i : i + params.lookback_window_days]
		if i + params.lookback_window_days >= len(prices) - 1:
			break
		test = log_returns.iloc[
			i + params.lookback_window_days : i + params.lookback_window_days + params.rebalance_frequency_days
		]
		if len(test) == 0:
			continue

		expected = train.mean() * 252
		cov = train.cov() * 252
		weights = optimize_fn(expected, cov, params.risk_free_rate)
		if weights is None or len(weights) != n_assets:
			weights = np.array([1.0 / n_assets] * n_assets)

		daily = np.dot(test.values, weights)
		results["returns"].append(float(np.sum(daily)))
		results["weights_history"].append(weights.copy())
		results["dates"].append(prices.index[i + params.lookback_window_days])

	return results


