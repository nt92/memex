import json

from memex.schema.record_info import RecordInfo

docs_json_path = './output/docs.json'
indexJsonPath = './output/index.json'


def create_docs_json(record: RecordInfo):
    with open(docs_json_path, 'w') as output:
        json.dump(record.get_dict(), output)
