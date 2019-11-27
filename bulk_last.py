import random
import names
from elasticsearch import Elasticsearch, helpers

client = Elasticsearch("localhost:9200")

row = []
for i in range(25000): 
    row.append({"id":i, "name":names.get_full_name(), "ano":random.randint(1950,2019)})

print(row)

resp = helpers.bulk(client, row, index="personas", doc_type="_doc")
