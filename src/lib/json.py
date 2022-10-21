import json

from src.schema.record_info import RecordInfo
from src.schema.token_index import TokenIndex

docs_json_path = './db/docs.json'
index_json_path = './db/index.json'


def create_docs_json(record: RecordInfo):
    with open(docs_json_path, 'w') as output:
        json.dump(record.to_json(), output)


def create_index_json(token_index: TokenIndex):
    with open(index_json_path, 'w') as output:
        json.dump(token_index.to_json(), output)


def search_index(query: str):
    with open(index_json_path, 'r') as index_file:
        index_json = json.load(index_file)
        index = TokenIndex(**index_json)
        print(index.index.values())
