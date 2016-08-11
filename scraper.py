import json,requests,sqlite3

headers = {'User-Agent':'Python script gathering traffic data once a day; contact at: reddit.com/u/hypd09 (gzip)', 'Accept-Encoding': 'gzip', 'Content-Encoding': 'gzip'}
req = requests.Session()

DB_FILE = 'data.sqlite'
conn = sqlite3.connect(DB_FILE)

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS data (time INTEGER PRIMARY KEY, uniques INTEGER, pageviews INTEGER)')

link = 'http://www.reddit.com/r/datasets/about/traffic/.json'

data = json.loads(req.get(link,headers=headers).text)

for hour in data['hour']:
    c.execute('INSERT OR REPLACE INTO data VALUES (?,?,?)',hour)
    
conn.commit()
c.close()
