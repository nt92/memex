import glob
import json

from indexer.src.lib.database2 import Database

import re

from indexer.src.lib.timestamp import from_timestamp

messenger_path = "./indexer/data/fb-messenger/messages/messages/inbox/*/*.json"
# messenger_path = "./indexer/data/fb-messenger/messages/messages/inbox/mackenziepatel_8sbrouv7sg/*.json"
messenger_prefix = "msgr"


def get_messenger_records(db: Database):
    messenger_json_list = glob.glob(messenger_path)

    for file_index, file in enumerate(messenger_json_list, len(messenger_json_list) - 1):
        with open(file, "r") as f:
            data = json.load(f)

            messages_with_content = (messages for messages in data["messages"] if 'content' in messages)
            db_entries = []
            for message_index, message in enumerate(messages_with_content):
                # msgr saves special char content in a weird way so we have to decode it
                message_content = re.sub(r'[\xc2-\xf4][\x80-\xbf]+',
                                         lambda m: m.group(0).encode('latin1').decode('utf8'), message["content"])

                if content_filter(message_content):
                    continue

                title = "Messenger Thread with " + data["title"]
                content = message["sender_name"] + ": " + message_content
                time = from_timestamp(round(message["timestamp_ms"]/1000)).isoformat()

                db_entries.append({'source': messenger_prefix, 'title': title, 'content': content, 'time': time, 'link': ''})
            db.save_records(db_entries)


def content_filter(content):
    filters = ['missed a call', 'missed your call', 'Reacted']
    for filter_str in filters:
        if filter_str in content:
            return True
    return False

# TODO: Create a more scalable system for content filtering on a per-integration basis
