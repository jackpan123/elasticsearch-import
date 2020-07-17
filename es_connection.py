from elasticsearch import Elasticsearch


class ElasticsearchConnect:

    
    def __init__(self):
        print()
    def connect(self):
        es = Elasticsearch([
            {'host': '192.168.101.17'},
            {'host': '192.168.101.18'},
            {'host': '192.168.101.19'},
        ])

        return es


        

