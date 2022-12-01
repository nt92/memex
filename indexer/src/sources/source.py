from src.lib.database import Database
from src.sources.fb_messenger import get_messenger_records
from src.sources.imessage import get_imessage_records


def get_records(db: Database):
    get_imessage_records(db)
    get_messenger_records(db)
