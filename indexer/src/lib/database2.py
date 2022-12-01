import os
from dotenv import load_dotenv
from supabase import create_client


class Database:
    def __init__(self):
        load_dotenv()
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_SECRET_KEY")
        self.supabase = create_client(url, key)

    def save_record(self, source, title, content, time, link):
        record = {'source': source, 'title': title, 'content': content, 'time': time, 'link': link}
        self.supabase.table('records').insert(record).execute()

    def save_records(self, records):
        self.supabase.table('records').insert(records).execute()
