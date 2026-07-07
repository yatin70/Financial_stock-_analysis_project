import pandas as pd


df = pd.read_csv(r'E:\Yatin\VS CODE\python\SP 500 Stock Prices 2014-2017 (1).csv')


df['date'] = pd.to_datetime(df['date'])
df = df.dropna(subset=['open', 'high', 'low', 'close'])
df = df.sort_values(['symbol', 'date']).reset_index(drop=True)


sector_map = {
    'AAPL': 'Technology', 'MSFT': 'Technology', 'GOOGL': 'Technology', 'INTC': 'Technology', 'ADBE': 'Technology',
    'JPM': 'Financials', 'BAC': 'Financials', 'GS': 'Financials', 'AIG': 'Financials',
    'XOM': 'Energy', 'CVX': 'Energy', 'COP': 'Energy',
    'JNJ': 'Healthcare', 'PFE': 'Healthcare', 'ABT': 'Healthcare', 'ABBV': 'Healthcare',
    'KO': 'Consumer Staples', 'PG': 'Consumer Staples', 'PEP': 'Consumer Staples',
    'AMZN': 'Consumer Discretionary', 'HD': 'Consumer Discretionary', 'MCD': 'Consumer Discretionary'
}
df = df[df['symbol'].isin(sector_map.keys())].copy()
df['sector'] = df['symbol'].map(sector_map)


df['daily_return'] = df.groupby('symbol')['close'].pct_change().round(4)
df['rolling_avg_20'] = df.groupby('symbol')['close'].transform(lambda x: x.rolling(20).mean()).round(4)
df['rolling_volatility_20'] = df.groupby('symbol')['daily_return'].transform(lambda x: x.rolling(20).std()).round(4)


df['vol_mean'] = df.groupby('symbol')['volume'].transform('mean').round(4)
df['vol_std'] = df.groupby('symbol')['volume'].transform('std').round(4)
df['volume_zscore'] = ((df['volume'] - df['vol_mean']) / df['vol_std']).round(4)


sector_kpi = df.groupby('sector').agg(
    avg_close=('close', 'mean'),
    avg_daily_return=('daily_return', 'mean'),
    avg_volatility=('rolling_volatility_20', 'mean'),
    avg_volume=('volume', 'mean')
)
print("Sector-level KPIs:")
print(sector_kpi)
print()


sector_momentum = df.groupby('sector')['daily_return'].mean().sort_values(ascending=False)
print("Sector momentum ranking (highest to lowest):")
print(sector_momentum)
print()


anomalies = df[df['volume_zscore'] > 3][['symbol', 'date', 'volume', 'volume_zscore', 'daily_return']]
print(f"Volume anomalies found: {len(anomalies)}")
print(anomalies.sort_values('volume_zscore', ascending=False).head(10))


df.to_csv('sp500_final.csv', index=False)