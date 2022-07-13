import pandas as pd
import urllib.request

idxurl = 'https://www.idxchannel.com/market-stock'

with urllib.request.urlopen(idxurl) as i:
    html = i.read()
    
data = pd.read_html(html)[0]
print(data)

data.to_csv("idx_market_stock.csv")