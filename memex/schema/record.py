from typing import Dict


class Record:
    def __init__(
        self,
        record_id: str,
        title: str,
        content: str,
        link: str,
        frequency: Dict[str, int],
        time: int
    ):
        self.record_id = record_id
        self.title = title
        self.content = content
        self.link = link
        self.frequency = frequency
        self.time = time
