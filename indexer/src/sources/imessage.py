import sqlite3

from indexer.src.lib.database2 import Database
from indexer.src.lib.timestamp import to_timestamp, from_timestamp

imessage_path = "./indexer/data/imessage/chat.db"
# imessage_path = "~/Library/Messages/chat.db"
imessage_prefix = "imsg"


def get_imessage_records(db: Database):
    conn = sqlite3.connect(imessage_path)
    cur = conn.cursor()

    # Apple's epoch starts on January 1st, 2001 for some reason...
    # http://apple.stackexchange.com/questions/114168
    messages = cur.execute("""
    SELECT
        chat.chat_identifier,
        message.text,
        datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime") AS message_date,
        message.is_from_me
    FROM
        chat
    JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id
    JOIN message ON chat_message_join.message_id = message. "ROWID"
    """)
    db_entries = []
    for message in messages:
        if message[1] is not None:
            title = "iMessage Thread with " + message[0]
            content = 'Me: ' + message[1] if message[3] else 'Other: ' + message[1]
            time = from_timestamp(to_timestamp(message[2])).isoformat()
            db_entries.append({'source': imessage_prefix, 'title': title, 'content': content, 'time': time, 'link': ''})
    db.save_records(db_entries)
# TODO: Get a contact's name from Contacts.app
