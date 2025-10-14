from typing import Tuple
import numpy as np
import pandas as pd


def annualized_return_and_volatility(log_returns: pd.DataFrame, trading_days: int = 252) -> Tuple[pd.Series, pd.Series]:
	"""Compute annualized mean returns and volatilities from daily log returns."""
	annualized_mean_return = log_returns.mean() * trading_days
	annualized_volatility = log_returns.std() * np.sqrt(trading_days)
	return annualized_mean_return, annualized_volatility


def annualized_covariance(log_returns: pd.DataFrame, trading_days: int = 252) -> pd.DataFrame:
	"""Compute annualized covariance matrix from daily log returns."""
	return log_returns.cov() * trading_days


