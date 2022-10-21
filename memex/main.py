from memex.lib.lib import create_docs_json, create_index_json
from sources.source import get_records_and_tokens


def main():
    records, tokens = get_records_and_tokens()
    create_docs_json(records)
    create_index_json(tokens)
    print("hello world")


if __name__ == "__main__":
    main()
