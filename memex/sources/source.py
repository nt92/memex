from memex.schema.record_info import RecordInfo
from memex.schema.token_index import TokenIndex
from memex.sources.fb_messenger import get_messenger_records


def get_records() -> RecordInfo:
    messenger_records = get_messenger_records()
    return messenger_records


def get_tokens() -> TokenIndex:
    messenger_tokens = 1
    return messenger_tokens
