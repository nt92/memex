import json
from typing import Dict
from src.schema.record import Record


# RecordInfo turns the records into a map so that we can search based on the ID key
class RecordInfo:
    def __init__(self, record_map: Dict[str, Record]):
        self.record_map = record_map

    def add_record(self, key: str, value: Record):
        self.record_map[key] = [value]

    def get_dict(self):
        return self.record_map

    def to_json(self):
        return json.dumps(self.record_map, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
