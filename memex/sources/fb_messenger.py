import glob
import json
from typing import Tuple

from memex.lib.tokenizer import get_token_frequency_map
from memex.schema.record import Record
from memex.schema.record_info import RecordInfo
from memex.schema.token_index import TokenIndex

messenger_path = "./data/fb-messenger/messages/messages/inbox/*/*.json"
messenger_prefix = "msgr"


def get_messenger_records_and_tokens() -> Tuple[RecordInfo, TokenIndex]:
    messenger_json_list = glob.glob(messenger_path)
    messenger_record_map = RecordInfo({})
    messenger_token_map = TokenIndex({})

    for file_index, file in enumerate(messenger_json_list, len(messenger_json_list) - 1):
        with open(file, "r") as f:
            data = json.load(f)

            messages_with_content = (messages for messages in data["messages"] if 'content' in messages)
            for message_index, message in enumerate(messages_with_content):
                message_id = "{0}-{1}-{2}".format(messenger_prefix, file_index, message_index)
                title = "Messenger Message from " + data["title"]
                content = message["sender_name"] + ": " + message["content"]
                time = message["timestamp_ms"]
                token_frequency = get_token_frequency_map(message["content"])

                message_record = Record(message_id, title, content, token_frequency, time)
                messenger_record_map.add_record(message_id, message_record)

                for token in token_frequency:
                    if token in messenger_token_map.get_token_index():
                        messenger_token_map.get_token_index()[token].add(message_id)
                    else:
                        messenger_token_map.get_token_index()[token] = {message_id}

    for message_record in messenger_record_map.get_dict().values():
        print(message_record.content)

    return messenger_record_map, messenger_json_list
