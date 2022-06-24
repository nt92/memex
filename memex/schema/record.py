from typing import Dict


# Record represents the data that will be stored in the inverted index. Each piece of content that can be surfaced to
# the user will conform to this format — the client-side index will utilize this.
class Record:
    def __init__(
            self,
            record_id: str,
            title: str,
            content: str,
            link: str,
            frequency: Dict[str, int],
            time: int
    ):
        # A globally unique identifier for this item across all items
        # It's a 2 letter prefix for mod (e.g. "tw" for Tweets) and a number
        self.record_id = record_id
        # The title of the piece of content
        self.title = title
        # The item's text content to be displayed in the results
        self.content = content
        # Potential link to the source if applicable
        self.link = link
        # A map of <each_token_in_item>:<number_of_times_in_item>
        self.frequency = frequency
        # A relevant timestamp for the item
        self.time = time
