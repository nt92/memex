from src.lib.database import Database
from src.sources.fb_messenger import get_messenger_records_and_tokens


def get_records_and_tokens(db: Database):
    get_messenger_records_and_tokens(db)
