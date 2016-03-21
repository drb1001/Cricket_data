import requests as req
import json as j
from bs4 import BeautifulSoup
import re
import csv


# get cricket ground data from
# https://en.wikipedia.org/wiki/List_of_One_Day_International_cricket_grounds

wikipage = "List_of_One_Day_International_cricket_grounds"
api_link = "https://en.wikipedia.org/w/api.php?action=query&titles="+wikipage+"&prop=revisions&rvprop=content&format=json&rvparse=1"

r = req.get(api_link)
req_status = r.status_code
print req_status

jsondata = r.json()
data = jsondata["query"]["pages"]["36008812"]["revisions"][0]["*"]
html_data = BeautifulSoup(data, "html.parser")
html_table = html_data.find('table', attrs={"class":"wikitable sortable"})

headers = [header.text for header in html_table.find_all('th')]
del headers[-2] # remove incorrect header
print headers

rows = []
for row in html_table.find_all('tr'):
    rows.append([val.text.encode('utf8') for val in row.find_all('td')])

# todo:
# add a space into second column
# strip spaces from 3rd column + split into two columns around first comma
# strip spaces from 4th column + split remove second half


with open('odi_venues.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in rows if row)



# print j.dumps( data0 , sort_keys=True, indent=4, separators=(',', ': ') )
