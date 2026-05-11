Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
import pandas as pd

# 1. Expanded Dataset
data = {
    "Company": ["Lockheed Martin", "Northrop Grumman", "General Dynamics", "RTX Corp", "L3Harris", "Huntington Ingalls", "Leidos", "Booz Allen", "SAIC", "CACI", "Howmet", "TransDigm", "HEICO", "AeroVironment", "Kratos", "BAE Systems", "Thales", "Leonardo", "Rheinmetall", "Honeywell", "Eaton", "Parker-Hannifin", "Teledyne", "Curtiss-Wright"],
    "Ticker": ["LMT", "NOC", "GD", "RTX", "LHX", "HII", "LDOS", "BAH", "SAIC", "CACI", "HWM", "TDG", "HEI", "AVAV", "KTOS", "BAESY", "HO.PA", "FINMY", "RNMBY", "HON", "ETN", "PH", "TDY", "CW"],
    "Current Price": [640, 725, 350, 205, 375, 290, 167, 150, 135, 370, 241, 1250, 200, 180, 22, 27, 160, 18, 75, 210, 330, 630, 430, 300],
    "52W High": [650, 730, 370, 205, 379, 293, 206, 170, 150, 400, 267, 1300, 210, 220, 25, 27, 165, 19, 80, 221, 345, 640, 450, 320],
    "52W Low": [420, 420, 240, 97, 160, 159, 135, 110, 105, 280, 160, 800, 150, 90, 12, 15, 110, 10, 40, 175, 192, 360, 350, 210]
... }
... 
... df = pd.DataFrame(data)
... 
... # 2. Automated Calculations
... df['52W Midpoint'] = (df['52W High'] + df['52W Low']) / 2
... df['% off 52W High'] = (((df['52W High'] - df['Current Price']) / df['52W High']) * 100).round(2)
... df['Annual Volatility ($)'] = df['52W High'] - df['52W Low']
... df['Price Strength (%)'] = ((df['Current Price'] - df['52W Low']) / (df['52W High'] - df['52W Low']) * 100).round(1)
... 
... # 3. High-Level Metrics
... sector_avg_price = df['Current Price'].mean()
... most_expensive = df.loc[df['Current Price'].idxmax(), 'Company']
... closest_to_high = df.loc[df['% off 52W High'].idxmin(), 'Company']
... 
... # 4. Display Logic
... print("="*100)
... print(f"{'DEFENSE & AEROSPACE SECTOR ANALYSIS':^100}")
... print("="*100)
... 
... pd.set_option('display.max_columns', None)
... pd.set_option('display.width', 1000)
... 
... print(df.to_string(index=False))
... 
... print("-" * 100)
... print(f"SECTOR SUMMARY:")
... print(f"* Total Companies Analyzed: {len(df)}")
... print(f"* Average Stock Price: ${sector_avg_price:.2f}")
... print(f"* Highest Value Ticker: {most_expensive} (${df['Current Price'].max()})")
... print(f"* Strongest Momentum: {closest_to_high} (only {df['% off 52W High'].min()}% off 52W High)")
... print("-" * 100)
... 
... # 5. Export to CSV (no extra dependencies needed)
... df.to_csv("top_25_defence_stocks.csv", index=False)
