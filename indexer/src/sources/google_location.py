import glob
import json

from indexer.src.lib.database2 import Database

from indexer.src.lib.timestamp import to_timestamp_loc

location_path = "./indexer/data/google/Location History/Semantic Location History/*/*.json"
# location_path = "./indexer/data/google/Location History/Semantic Location History/2022/2022_NOVEMBER.json"
location_prefix = "maps"


def get_location_data(db: Database):
    location_json_list = glob.glob(location_path)

    for file in location_json_list:
        with open(file, "r") as f:
            data = json.load(f)

            db_entries = []
            for timelineObject in data["timelineObjects"]:
                if "placeVisit" in timelineObject:
                    place_visit = timelineObject["placeVisit"]
                    if "address" in place_visit["location"]:
                        title = place_visit["location"]["address"]
                        if "name" in place_visit["location"]:
                            title = place_visit["location"]["name"] + ": " + title
                    elif "otherCandidateLocations" in place_visit:
                        try:
                            title = place_visit["otherCandidateLocations"][0]["address"]
                        except KeyError:
                            title = "Unknown Location"
                    else:
                        title = "Unknown Location"
                    start_time = to_timestamp_loc(place_visit["duration"]["startTimestamp"]).isoformat()
                    end_time = to_timestamp_loc(place_visit["duration"]["endTimestamp"]).isoformat()

                elif "activitySegment" in timelineObject:
                    activity_segment = timelineObject["activitySegment"]
                    try:
                        title = activity_segment["activityType"]
                    except KeyError:
                        title = "Unknown Activity"
                    if "distance" in activity_segment:
                        title += " for " + str(round(activity_segment["distance"] / 1600, 1)) + " miles"
                    start_time = to_timestamp_loc(activity_segment["duration"]["startTimestamp"]).isoformat()
                    end_time = to_timestamp_loc(activity_segment["duration"]["endTimestamp"]).isoformat()

                db_entries.append({'title': title, 'start_time': start_time, 'end_time': end_time})
                print(title, start_time, end_time)
            db.save_locations(db_entries)
