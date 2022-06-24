import glob
import json

from memex.schema.record import Record
from memex.schema.record_info import RecordInfo
# from memex.schema.token_index import TokenIndex

messenger_path = "./data/fb-messenger/messages/messages/inbox/*/*.json"
messenger_prefix = "msgr"


def get_messenger_records() -> RecordInfo:
    messenger_json_list = glob.glob(messenger_path)
    messenger_record_map = RecordInfo({})

    for file_index, file in enumerate(messenger_json_list):
        with open(file, "r") as f:
            data = json.load(f)
            # message_record = Record()

            messages_with_content = (messages for messages in data["messages"] if 'content' in messages)
            for message_index, message in enumerate(messages_with_content):
                message_id = "{0}-{1}-{2}".format(messenger_prefix, file_index, message_index)
                title = "Messenger Message from " + data["title"]
                content = message["sender_name"] + ": " + message["content"]
                time = message["timestamp_ms"]
                print(message_id, title, content, time)

# def get_messenger_tokens() -> TokenIndex:
