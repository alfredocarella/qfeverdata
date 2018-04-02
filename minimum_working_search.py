## Import modules
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
import json

## Load configuration
with open("config.json") as con_file:
    config = json.load(con_file)  # Only my API key in this file
client = ElsClient(config['apikey'])
    
## Define query and execute search
query = 'PUBYEAR > 2015 AND TITLE-ABS-KEY(Masonry+Earthquake)&view=COMPLETE'
doc_srch = ElsSearch(query, 'scopus')
doc_srch.execute(client, get_all=False)

## Print obtained fields for the first record
print(doc_srch.results[0].keys())