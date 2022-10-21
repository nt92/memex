from datetime import datetime

from src.lib.database import Database
from src.sources.imessage import get_imessage_records
from src.sources.source import get_records


def main():
    print("Hello! Welcome to your Memex. What would you like to do?")
    print("1. Re-index your data")
    print("2. Search your data")
    print("3. Current experiment")
    choice = int(input("Enter your choice: "))

    db = Database()

    if choice == 1:
        db.reset()
        db.setup()

        get_records(db)
    elif choice == 2:
        term = input("Enter a search term: ")
        output = db.search(term)
        for item in output:
            print(datetime.fromtimestamp(item[3]), item[2])
    # elif choice == 3:


if __name__ == "__main__":
    main()
