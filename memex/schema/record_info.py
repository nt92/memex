from typing import Dict
from memex.schema.record import Record


class RecordInfo:
    def __init__(self, record_map: Dict[str, Record]):
        self.record_map = record_map
