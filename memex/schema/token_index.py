from typing import Dict, Set


# TokenIndex maps a token to a list of IDs that it appears in
class TokenIndex:
    def __init__(self, index: Dict[str, Set[str]]):
        self.index = index

    def get_token_index(self):
        return self.index
