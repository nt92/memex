import glob
import json

from src.lib.database import Database

import re

messenger_path = "./data/fb-messenger/messages/messages/inbox/*/*.json"
# messenger_path = "./data/fb-messenger/messages/messages/inbox/mackenziepatel_8sbrouv7sg/*.json"
messenger_prefix = "msgr"


def get_messenger_records_and_tokens(db: Database):
    messenger_json_list = glob.glob(messenger_path)

    for file_index, file in enumerate(messenger_json_list, len(messenger_json_list) - 1):
        with open(file, "r") as f:
            data = json.load(f)

            messages_with_content = (messages for messages in data["messages"] if 'content' in messages)
            for message_index, message in enumerate(messages_with_content):
                # msgr saves special char content in a weird way so we have to decode it
                message_content = re.sub(r'[\xc2-\xf4][\x80-\xbf]+',
                                         lambda m: m.group(0).encode('latin1').decode('utf8'), message["content"])

                source = messenger_prefix
                title = "Messenger Thread with " + data["title"]
                content = message["sender_name"] + ": " + message_content
                time = message["timestamp_ms"]

                db.save_record(source, title, content, time, "")
