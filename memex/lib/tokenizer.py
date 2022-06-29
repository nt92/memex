from typing import Dict, List

#  Borrowing list of punctuation & stopwords from https://github.dev/thesephist/monocle/blob/main/lib/tokenizer.ink
punctuation = {".", "?", "!", ",", ":", ";", "-", "(", ")", "\"", "'", "{", "}", "[", "]", "#", "<", ">", "\\",
               "~", "*", "_", "|", "%", "/"}
stopwords = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "'re", "yours", "yourself",
             "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
             "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
             "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
             "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
             "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
             "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
             "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
             "few", "more", "most", "other", "some", "such", "no", "nor", "not", "'t", "'nt", "only", "own", "same",
             "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "'ll", "won", "ya",
             "'s", "'m", "'ve"}


def get_token_frequency_map(content: str) -> Dict[str, int]:
    # first, get the list of tokens from the content
    tokens = []
    curr = []
    for char in content:
        is_punct = char in punctuation
        if char == ' ':
            # efficient stringbuilder
            append_word(curr, tokens)
        # newline character, go to next word
        elif char == 10:
            append_word(curr, tokens)
        elif is_punct:
            # check if apostrophe, treat contraction as two words
            if len(curr) != 0 and char == "'":
                append_word(curr, tokens)
                curr = ["'"]
            continue
        else:
            curr.append(char)
    if len(curr) != 0:
        append_word(curr, tokens)

    # then, we create a token frequency map
    token_frequency_map: Dict[str, int] = {}
    for token in tokens:
        if token not in token_frequency_map:
            token_frequency_map[token] = 0
        token_frequency_map[token] += 1

    return token_frequency_map


def append_word(curr: List[str], tokens: List[str]):
    word_to_append = "".join(curr).lower()

    # check if stopword
    is_stopword = word_to_append in stopwords
    if not is_stopword and len(curr) > 1:
        tokens.append(word_to_append)
    curr.clear()
