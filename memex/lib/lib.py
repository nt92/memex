import json

from memex.schema.record_info import RecordInfo
from memex.schema.token_index import TokenIndex

docs_json_path = './output/docs.json'
index_json_path = './output/index.json'


def create_docs_json(record: RecordInfo):
    with open(docs_json_path, 'w') as output:
        json.dump(record.to_json(), output)


def create_index_json(token_index: TokenIndex):
    with open(index_json_path, 'w') as output:
        print(token_index.to_json())
        json.dump(token_index.to_json(), output)
