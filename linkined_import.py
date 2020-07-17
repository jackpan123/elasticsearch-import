from es_connection import ElasticsearchConnect
import json
from datetime import datetime

con = ElasticsearchConnect()
es_client = con.connect()

print('开始导入数据，请稍等...')
with open('resumes.json', 'r') as f:
    data = json.load(f)
    records = data['RECORDS']
    for i in range(len(records)):
        row = records[i]
        id = row.pop('_id')
        row['added_date'] = int(round(datetime.now().timestamp() * 1000))
        res = es_client.index(index="linkedin", doc_type='linkedin_type', id=id, body=row)
        #print(res['result'])

print('导入数据完成，请查收')

