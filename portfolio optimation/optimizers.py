from typing import Dict, Tuple
import numpy as np
import pandas as pd
import scipy.optimize as sco


def portfolio_return(weights: np.ndarray, expected_returns: pd.Series) -> float:
	return float(np.sum(weights * expected_returns.values))


def portfolio_volatility(weights: np.ndarray, cov_matrix: pd.DataFrame) -> float:
	return float(np.sqrt(np.dot(weights.T, np.dot(cov_matrix.values, weights))))


def sharpe_ratio(weights: np.ndarray, expected_returns: pd.Series, cov_matrix: pd.DataFrame, risk_free_rate: float) -> float:
	p_ret = portfolio_return(weights, expected_returns)
	p_vol = portfolio_volatility(weights, cov_matrix)
	return (p_ret - risk_free_rate) / p_vol if p_vol > 0 else -np.inf


def negative_sharpe_ratio(weights: np.ndarray, expected_returns: pd.Series, cov_matrix: pd.DataFrame, risk_free_rate: float) -> float:
	return -sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate)


def optimize_mean_variance(
	expected_returns: pd.Series,
	cov_matrix: pd.DataFrame,
	risk_free_rate: float,
	target_return: float | None = None,
	allow_short: bool = False,
) -> Dict[str, Tuple[np.ndarray, float, float, float]]:
	"""Run standard MVO optimizations: max Sharpe, min vol, and optional target return.

	Returns a dict with keys: 'max_sharpe', 'min_vol', and optionally 'target'.
	Each value is a tuple: (weights, ret, vol, sharpe).
	"""
	n_assets = len(expected_returns)
	initial = np.array([1.0 / n_assets] * n_assets)
	constraints_sum_to_1 = ({"type": "eq", "fun": lambda x: np.sum(x) - 1.0},)
	bounds = tuple((None if allow_short else 0.0, 1.0) for _ in range(n_assets))

	# Max Sharpe
	res_max = sco.minimize(
		negative_sharpe_ratio,
		initial,
		args=(expected_returns, cov_matrix, risk_free_rate),
		method="SLSQP",
		bounds=bounds,
		constraints=constraints_sum_to_1,
	)
	weights_max = res_max.x
	ret_max = portfolio_return(weights_max, expected_returns)
	vol_max = portfolio_volatility(weights_max, cov_matrix)
	sharpe_max = sharpe_ratio(weights_max, expected_returns, cov_matrix, risk_free_rate)

	# Min Vol
	res_min = sco.minimize(
		portfolio_volatility,
		initial,
		args=(cov_matrix,),
		method="SLSQP",
		bounds=bounds,
		constraints=constraints_sum_to_1,
	)
	weights_min = res_min.x
	ret_min = portfolio_return(weights_min, expected_returns)
	vol_min = portfolio_volatility(weights_min, cov_matrix)
	sharpe_min = (ret_min - risk_free_rate) / vol_min if vol_min > 0 else 0.0

	results: Dict[str, Tuple[np.ndarray, float, float, float]] = {
		"max_sharpe": (weights_max, ret_max, vol_max, sharpe_max),
		"min_vol": (weights_min, ret_min, vol_min, sharpe_min),
	}

	# Target return portfolio (optional)
	if target_return is not None:
		constraints_target = (
			{"type": "eq", "fun": lambda x: np.sum(x) - 1.0},
			{"type": "eq", "fun": lambda x: portfolio_return(x, expected_returns) - target_return},
		)
		res_target = sco.minimize(
			portfolio_volatility,
			initial,
			args=(cov_matrix,),
			method="SLSQP",
			bounds=bounds,
			constraints=constraints_target,
		)
		if res_target.success:
			w = res_target.x
			v = portfolio_volatility(w, cov_matrix)
			r = portfolio_return(w, expected_returns)
			s = (r - risk_free_rate) / v if v > 0 else 0.0
			results["target"] = (w, r, v, s)

	return results


def efficient_frontier(
	expected_returns: pd.Series,
	cov_matrix: pd.DataFrame,
	n_points: int = 50,
	allow_short: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
	"""Compute efficient frontier volatilities, returns, and weights across target returns."""
	n_assets = len(expected_returns)
	initial = np.array([1.0 / n_assets] * n_assets)
	bounds = tuple((None if allow_short else 0.0, 1.0) for _ in range(n_assets))

	min_ret = portfolio_return(initial, expected_returns)
	max_ret = float(expected_returns.max())
	targets = np.linspace(min_ret, max_ret, n_points)

	vols, rets, weights_list = [], [], []
	for t in targets:
		constraints = (
			{"type": "eq", "fun": lambda x: np.sum(x) - 1.0},
			{"type": "eq", "fun": lambda x: portfolio_return(x, expected_returns) - t},
		)
		res = sco.minimize(
			portfolio_volatility,
			initial,
			args=(cov_matrix,),
			method="SLSQP",
			bounds=bounds,
			constraints=constraints,
		)
		if res.success:
			w = res.x
			weights_list.append(w)
			vols.append(portfolio_volatility(w, cov_matrix))
			rets.append(t)

	return np.array(vols), np.array(rets), np.array(weights_list)


