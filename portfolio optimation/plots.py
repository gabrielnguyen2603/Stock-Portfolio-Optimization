from typing import Sequence
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_prices_and_normalized(prices: pd.DataFrame) -> None:
	plt.style.use('dark_background')
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=100)
	fig.patch.set_facecolor('#0d1117')

	for col in prices.columns:
		ax1.plot(prices.index, prices[col], linewidth=1.5, alpha=0.85, label=col)
	ax1.set_title('Stock Prices Over Time')
	ax1.legend()

	norm = prices / prices.iloc[0] * 100
	for col in norm.columns:
		ax2.plot(norm.index, norm[col], linewidth=1.5, alpha=0.85, label=col)
	ax2.set_title('Normalized Stock Prices (Base=100)')
	ax2.legend()
	plt.tight_layout()
	plt.show()


def plot_efficient_frontier(vols: np.ndarray, rets: np.ndarray, asset_stds: Sequence[float], asset_rets: Sequence[float]) -> None:
	plt.figure(figsize=(12, 8))
	plt.plot(vols, rets, 'b-', linewidth=3, label='Efficient Frontier')
	for s, r in zip(asset_stds, asset_rets):
		plt.scatter(s, r, s=70, alpha=0.7)
	plt.title('Efficient Frontier & Assets')
	plt.xlabel('Volatility')
	plt.ylabel('Return')
	plt.grid(True, alpha=0.3)
	plt.legend()
	plt.tight_layout()
	plt.show()


