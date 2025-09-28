import requests
import pandas as pd
from datetime import datetime

req=requests.get("https://wallettrackapi-655880131780.us-central1.run.app/")

data=req.json()

processed_data = []
for i in data["data"]:
    i['datetime'] = datetime.fromtimestamp(i['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    processed_data.append(i)

df = pd.DataFrame(processed_data)
df = df.sort_values('timestamp')
df.to_csv('insiders_data.csv', index=False)

print(f"Saved {len(processed_data)} records to insiders_data.csv (sorted by timestamp)")
print("Sample record with converted datetime:")
print(processed_data[0])
