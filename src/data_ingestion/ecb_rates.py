print("ECB script started")
import requests
import pandas as pd
from io import StringIO
url = "https://data-api.ecb.europa.eu/service/data/FM/D.U2.EUR.4F.KR.DFR.LEV?startPeriod=2000-01-01"
response = requests.get(
    url,
    headers={"Accept": "text/csv"},
    timeout=30
)
data = pd.read_csv(StringIO(response.text))
data = data[["TIME_PERIOD", "OBS_VALUE"]]
data = data.rename(columns={
    "TIME_PERIOD": "date",
    "OBS_VALUE": "deposit_rate"
})
data.to_csv("data/ecb_deposit_rate.csv", index=False)

print(data.head())
print("Number of rows:", len(data))
print("First date:", data["date"].iloc[0])
print("Last date:", data["date"].iloc[-1])