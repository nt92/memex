from src.lib.database import Database
from src.lib.timestamp import from_timestamp, date_to_range
from src.sources.source import get_records


def main():
    print("Hello! Welcome to your Memex. What would you like to do? These options define the main API for your Memex.")
    print("1. Re-index your data")
    print("2. Search your data")
    print("3. Output a particular day's data")
    choice = int(input("Enter your choice: "))

    db = Database()

    # Re-index
    if choice == 1:
        db.reset()
        db.setup()

        get_records(db)

    # Search
    elif choice == 2:
        term = input("Enter a search term: ")
        output = db.search(term)
        for item in output:
            print(item[3], from_timestamp(item[3]), item[2])

    # Output a particular day's data
    elif choice == 3:
        day = input("Enter a day (YYYY-MM-DD): ")
        [start, end] = date_to_range(day)
        print(start, end)
        output = db.search_day(day)
        for item in output:
            print(item[3], from_timestamp(item[3]), item[2])


if __name__ == "__main__":
    main()
