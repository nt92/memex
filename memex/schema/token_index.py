from typing import Dict, List


# TokenIndex maps a token to a list of IDs that it appears in
class TokenIndex:
    def __init__(self, index: Dict[str, List[str]]):
        self.index = index
