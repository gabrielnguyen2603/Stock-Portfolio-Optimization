from typing import List, Optional
import pandas as pd
import numpy as np
import datetime as dt

try:
	import yfinance as yf
except Exception:  # pragma: no cover
	yf = None


def fetch_adjusted_close_prices(
	tickers: List[str],
	start: Optional[str] = None,
	end: Optional[str] = None,
)	-> pd.DataFrame:
	"""Download adjusted close prices for given tickers using yfinance.

	Args:
		tickers: List of ticker symbols.
		start: ISO date string YYYY-MM-DD; defaults to 5 years ago.
		end: ISO date string YYYY-MM-DD; defaults to today.

	Returns:
		DataFrame indexed by date with columns per ticker.
	"""
	if start is None:
		start_dt = (dt.datetime.now() - dt.timedelta(days=5 * 365)).strftime("%Y-%m-%d")
	else:
		start_dt = start

	if end is None:
		end_dt = dt.datetime.now().strftime("%Y-%m-%d")
	else:
		end_dt = end

	if yf is None:
		raise ImportError("yfinance is required to fetch market data")

	prices = yf.download(tickers, start=start_dt, end=end_dt, auto_adjust=False)[
		"Adj Close"
	]
	prices.index = pd.to_datetime(prices.index)
	return prices.sort_index()


def compute_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
	"""Compute daily log returns from price DataFrame."""
	log_returns = np.log(prices / prices.shift(1))
	return log_returns.dropna(how="all").dropna()


