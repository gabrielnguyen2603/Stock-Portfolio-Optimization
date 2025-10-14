from typing import Dict, Tuple
import numpy as np
import pandas as pd


def monte_carlo_portfolio(
	weights: np.ndarray,
	log_returns: pd.DataFrame,
	n_simulations: int = 10000,
	time_horizon_days: int = 252,
	seed: int | None = 42,
)	-> Dict[str, np.ndarray | float]:
	"""Run Monte Carlo on portfolio given weights and historical daily log-returns.

	Returns dict with 'returns' (array) and 'paths' (matrix).
	"""
	if seed is not None:
		np.random.seed(seed)

	mu = log_returns.mean().values
	Sigma = log_returns.cov().values
	n_assets = len(mu)

	returns = np.zeros(n_simulations)
	paths = np.zeros((n_simulations, time_horizon_days))

	# Cholesky factor; if fails, sample directly from multivariate normal
	try:
		L = np.linalg.cholesky(Sigma)
		for i in range(n_simulations):
			z = np.random.standard_normal((time_horizon_days, n_assets))
			R = mu + z @ L.T
			p = R @ weights
			returns[i] = float(np.sum(p))
			paths[i] = np.cumsum(p)
	except np.linalg.LinAlgError:
		for i in range(n_simulations):
			R = np.random.multivariate_normal(mu, Sigma, time_horizon_days)
			p = R @ weights
			returns[i] = float(np.sum(p))
			paths[i] = np.cumsum(p)

	return {"returns": returns, "paths": paths}


