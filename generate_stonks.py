
import csv
import json
import os.path as osp

rows = []

# CSV got by https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=GME&interval=5min&slice=year1month2&apikey=ALPHA_VANTAGE_API_KEY
# Where ALPHA_VANTAGE_API_KEY is your API key.
with open('raw_data/GME_y1m1_5min.csv') as f:
	rows.extend(csv.DictReader(f))

per_day_data = {}

for row in rows:
	day, _, tm = row['time'].partition(' ')
	per_day_data.setdefault(day, []).append(row)

for day, dt in per_day_data.iteritems():
	dt.sort(key=lambda x:x['time'])
	list_of_rows = []
	for x in dt:
		list_of_rows.append(['', float(x['low']), float(x['open']), float(x['close']), float(x['high'])])
	with open(osp.join('real_stonks', day), 'w') as f:
		json.dump(list_of_rows, f)
