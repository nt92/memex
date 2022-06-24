from typing import Dict
from memex.schema.record import Record


# RecordInfo turns the records into a map so that we can search based on the ID key
class RecordInfo:
    def __init__(self, record_map: Dict[str, Record]):
        self.record_map = record_map
