from typing import Tuple

from memex.schema.record_info import RecordInfo
from memex.schema.token_index import TokenIndex
from memex.sources.fb_messenger import get_messenger_records_and_tokens


def get_records_and_tokens() -> Tuple[RecordInfo, TokenIndex]:
    messenger_records, messenger_tokens = get_messenger_records_and_tokens()
    return messenger_records, messenger_tokens
