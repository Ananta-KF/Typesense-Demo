import typesense
import pprint

pp = pprint.PrettyPrinter(indent=2, width=30, compact=True)

client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8081',
        'protocol': 'http'
    }],
    'api_key': 'VfNGkGkGyka1PdFbwKMaFsst48MFrgLJzWlMeksLjoM=',
    'connection_timeout_seconds': 600
})

# Basic Search 
def basic_search(query, client):
    search_parameters = {
        'q': query,
        'query_by': 'name',
        'num_typos': 0, 
        'exact_on_single_word_query' : 'strict'
    }
    return client.collections['skillsexperiment'].documents.search(search_parameters)

# response = basic_search("Apache VXQuery", client)
# pp.pprint(response)

# Typo Tolerance
def typo_tolerance(query, client):
    search_parameters = {
        'q': query,
        'query_by': 'name',
        'num_typos': 1  # one typo allowed
    }
    return client.collections['skillsexperiment'].documents.search(search_parameters)

# response = typo_tolerance("Zeppin", client) # "Zeppin" instead of "Zeplin"
# pp.pprint(response)

# exact match function
def exact_match(query, client):
    search_parameters = {
        'q': query,
        'query_by': 'name, subFunction',
        'num_typos': 0,  
        'per_page' : 2,
        'split_join_tokens': 'off',
        'num_typos': 0,
        'typo_tokens_threshold': 0,
        'drop_tokens_threshold': 0,
        # 'highlight_fields': 'none',
        # 'highlight_full_fields': 'none'
        #'exact_phrase' : True,
        #'exact_match' : True,
        #'pre_segmented_query': False,  
        #'exact_on_single_word_query': 'strict',
        #'sort_by': '_text_match:desc',
        #'query_by_weights' : '10'
    }
    return client.collections['skillsexperiment'].documents.search(search_parameters)

# response = exact_match("Apache VXQuery", client)
# pp.pprint(response)

# text match score
def text_match(query, client):  # returns documents based on the text match score
    search_parameters = {        
        'q': query,
        'query_by': 'name',
        'num_typos' : 0,
        'typo_tokens_threshold': 0,
        'drop_tokens_threshold': 0,
        'text_match_threshold': '30000000',
        #'filter_by'    : 'id:<100',
        'per_page': 9
    }
    return client.collections['skillsexperiment'].documents.search(search_parameters)

# response = text_match("Zeplin", client)
# pp.pprint(response)

# prefix query 
def prefix_query(query, client): # (uses the last word as a prefix) 
    search_parameters = {        # could be used for autocomplete functionality
        'q': query,
        'query_by': 'name, function, subFunction',
        'prefix' : True,
        'per_page' : 100
    }
    return client.collections['skillsexperiment'].documents.search(search_parameters)

response = prefix_query("Apache", client)
pp.pprint(response)

# search with weights given to columns
def search_with_query_by_weights(query, client):
    search_parameters = {
        'q': query,
        'query_by': 'function, name, skillDescription',  # using multiple fields
        'query_by_weights': '2,1,1',  # helps in boosting the weight of the 'name' field
        'num_typos': 1  
    }
    return client.collections['skillsexperiment'].documents.search(search_parameters)
    

# response = search_with_query_by_weights("Technology & IT", client)
# pp.pprint(response)

