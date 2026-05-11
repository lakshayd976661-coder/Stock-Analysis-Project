Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> ```python
... import pandas as pd
... import yfinance as yf
... import seaborn as sns
... import matplotlib.pyplot as plt
... 
... defense_tickers = ["LMT", "NOC", "GD", "RTX", "LHX", "HII", "LDOS", "BAH", "SAIC", "CACI", "HWM", "TDG", "HEI", "AVAV", "KTOS", "BAESY", "HO.PA", "FINMY", "RNMBY", "HON", "ETN", "PH", "TDY", "CW"]
... oil_tickers = ["XOM", "CVX", "SHEL", "TTE", "BP", "COP", "EQNR", "PBR", "EOG", "VLO", "MPC", "PSX", "ET", "SU", "CNQ", "CVE", "IMO", "OXY", "BKR", "HAL", "SLB", "KMI", "LNG", "ENB", "OKE"]
... all_tickers = list(set(defense_tickers + oil_tickers))
... 
... data = yf.download(all_tickers, period="1y", interval="1d", progress=False)['Adj Close']
... returns = data.pct_change().dropna()
... 
... defense_returns = returns[defense_tickers].mean(axis=1)
... oil_returns = returns[oil_tickers].mean(axis=1)
... sector_comparison = pd.DataFrame({"Defense": defense_returns, "Oil": oil_returns})
... sector_corr = sector_comparison.corr().iloc[0, 1]
... 
... display_tickers = defense_tickers[:10] + oil_tickers[:10]
... corr_matrix = returns[display_tickers].corr()
... 
... plt.figure(figsize=(12, 9))
... sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, vmin=-1, vmax=1)
... plt.title(f'Sector Correlation Matrix\nOverall Defense vs Oil Correlation: {sector_corr:.2f}')
... plt.tight_layout()
... plt.savefig('correlation_2d.png')
... plt.show()
... 
... print(f"Overall Sector Correlation: {sector_corr:.4f}")
... 
... ```
