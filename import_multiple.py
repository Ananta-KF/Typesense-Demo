import csv
import typesense
import json

def createCollection(client):
    skillsExpSchema = {
        "name": "skillsexperiment",
        "fields": [
        {"name": "id", "type": "string"},
        {"name": "id_number", "type": "int32"},
        {"name": "context", "type": "string"},
        {"name": "function", "type": "string"},
        {"name": "subFunction", "type": "string", "facet": True},
        {"name": "name", "type": "string", "facet": True}, #, "index": True, "tokenizer" : "whitespace"},
        {"name": "skillElement", "type": "string"},
        {"name": "skillDescription", "type": "string"},
        {"name": "skillSynonyms", "type": "string"},
        {"name": "status", "type": "string"}
        ],
        "default_sorting_field": "id_number"
    }
    #client.collections["skillsexperiment"].delete()
    client.collections.create(skillsExpSchema)
    
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8081',
        'protocol': 'http'
    }],
    'api_key': 'VfNGkGkGyka1PdFbwKMaFsst48MFrgLJzWlMeksLjoM=',
    'connection_timeout_seconds': 600
})

createCollection(client)

# with open('skills.jsonl') as jsonl_file:
#   response = client.collections['skillsexperiment'].documents.import_(jsonl_file.read().encode('utf-8-sig'), {'action': 'create'})
#   print(response)

# # Open CSV file and read its content
# with open(csv_file_path, mode='r', encoding='utf-8-sig') as csvfile:
#     csv_reader = csv.DictReader(csvfile)
#     for row in csv_reader:
#         if row['name'] != 'Zeplin':
#             try:
#                 document = {
#                     "id": row['id'],  # Ensure this matches your CSV header exactly
#                     "id_number": int(row['id']),
#                     "context": row['context'],
#                     "function": row['function'],
#                     "subFunction": row['subFunction'],
#                     "name": row['name'],
#                     "skillElement": row['skillElement'],
#                     "skillDescription": row['skillDescription'],
#                     "skillSynonyms": row['skillSynonyms'],
#                     "status": row['status']
#                 }

#                 response = client.collections['skills'].documents.upsert(document)
#                 print(f"Added document: {response['name']}")

#             except Exception as e:
#                 print(f"Error adding document: {e}")
