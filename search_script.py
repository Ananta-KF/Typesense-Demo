import typesense
import json
import pprint

client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8081',
        'protocol': 'http'
    }],
    'api_key': 'VfNGkGkGyka1PdFbwKMaFsst48MFrgLJzWlMeksLjoM=',
    'connection_timeout_seconds': 600
})

search_parameters = {
  'q'         : 'Apache VXQuery',
  'query_by'  : 'name',
  'prioritize_exact_match' : True,
  'per_page' : 1,
  'exact_on_single_word_query' : 'strict',
  'num_typos' : 0
}
 
response = client.collections['skillsexperiment'].documents.search(search_parameters)
pp = pprint.PrettyPrinter(indent = 2, width =30, compact = True)

pp.pprint(response)