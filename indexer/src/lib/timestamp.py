from datetime import datetime


def to_timestamp(time_string: str) -> int:
    return round(datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S").timestamp())


def from_timestamp(timestamp: int) -> datetime:
    return datetime.utcfromtimestamp(timestamp)


def date_to_range(date: str) -> (int, int):
    start = to_timestamp(date + " 00:00:00")
    end = to_timestamp(date + " 23:59:59")
    return start, end
