from src.lib.database import Database
from src.lib.json import create_docs_json, create_index_json, search_index
from sources.source import get_records_and_tokens


def main():
    # records, tokens = get_records_and_tokens()
    # create_docs_json(records)
    # create_index_json(tokens)

    # search_index("hello")

    db = Database()

    print(db)


if __name__ == "__main__":
    main()
