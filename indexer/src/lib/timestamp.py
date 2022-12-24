import re
from datetime import datetime


def to_timestamp(time_string: str) -> int:
    return round(datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S").timestamp())


def to_timestamp_loc(time_string: str) -> datetime:
    remove_fraction = re.sub(r"\.\d+", "", time_string)
    timestamp_int = round(datetime.strptime(remove_fraction, "%Y-%m-%dT%H:%M:%SZ").timestamp())
    return datetime.utcfromtimestamp(timestamp_int)


def from_timestamp(timestamp: int) -> datetime:
    return datetime.utcfromtimestamp(timestamp)


def date_to_range(date: str) -> (int, int):
    start = to_timestamp(date + " 00:00:00")
    end = to_timestamp(date + " 23:59:59")
    return start, end
