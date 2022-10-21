from src.lib.database import Database
from src.sources.source import get_records_and_tokens


def main():
    print("Hello! Welcome to your Memex. What would you like to do?")
    print("1. Re-index your data")
    print("2. Search your data")
    choice = int(input("Enter your choice: "))

    db = Database()

    if choice == 1:
        db.reset()
        db.setup()

        get_records_and_tokens(db)
    elif choice == 2:
        term = input("Enter a search term: ")
        output = db.search(term)
        print(output)


if __name__ == "__main__":
    main()
