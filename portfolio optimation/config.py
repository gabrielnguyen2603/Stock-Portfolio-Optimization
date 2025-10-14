from dataclasses import dataclass


@dataclass
class ProjectConfig:
	"""Centralized configuration for portfolio optimization workflows."""
	risk_free_rate: float = 0.02
	trading_days_per_year: int = 252
	lookback_window_days: int = 252
	rebalance_frequency_days: int = 21
	seed: int = 42


