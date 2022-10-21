import sqlite3
from datetime import datetime

from src.lib.database import Database

imessage_path = "./data/imessage/chat.db"
# imessage_path = "~/Library/Messages/chat.db"
imessage_prefix = "imsg"

# Apple's epoch starts on January 1st, 2001 for some reason...
# http://apple.stackexchange.com/questions/114168
epoch = 978307200


def get_imessage_records(db: Database):
    conn = sqlite3.connect(imessage_path)
    cur = conn.cursor()
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
    ORDER BY
        message_date ASC
    LIMIT 100;
    """)
    for message in messages:
        title = "iMessage Thread with " + message[0]
        content = 'Me: ' + message[1] if message[3] else 'Other: ' + message[1]
        time = round(datetime.strptime(message[2], "%Y-%m-%d %H:%M:%S").timestamp())
        db.save_record(imessage_prefix, title, content, time, "")
