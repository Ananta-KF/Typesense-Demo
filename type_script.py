import csv
import json
import typesense

client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8081',
        'protocol': 'http'
    }],
    'api_key': 'VfNGkGkGyka1PdFbwKMaFsst48MFrgLJzWlMeksLjoM=',
    'connection_timeout_seconds': 600
})

csv_file_path = 'skills_library_v1.0.30-19052023.csv'

arr = []

with open(csv_file_path, mode='r', encoding='utf-8-sig') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
      document = {
          "id": row['id'],
          "id_number": int(row['id']),  
          "context": row['context'],
          "function": row['function'],
          "subFunction": row['subFunction'],
          "name": row['name'],
          "skillElement": row['skillElement'],
          "skillDescription": row['skillDescription'],
          "skillSynonyms": row['skillSynonyms'],
          "status": row['status']
      }
      arr.append(document)

response = client.collections['skillsexperiment'].documents.import_(arr, {'action': 'create'})

# print(response)

            #     # response = client.collections['skills'].documents.upsert(document)
            #     # print(f"Added document: {response['name']}")

            # except Exception as e:
            #     print(f"Error adding document: {e}")
