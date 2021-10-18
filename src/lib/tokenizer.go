package lib

import (
	"strings"
)

var punctuation map[string]bool
var stopwords map[string]bool

func GetTokenFrequencyMap(content string) map[string]int {
	if len(punctuation) == 0 || len(stopwords) == 0 {
		initializeSets()
	}

	tokens := splitStringBySpaceAndRemovePunctuation(content)
	tokenFrequencyMap := createTokenFrequencyMap(tokens)

	return tokenFrequencyMap
}

func splitStringBySpaceAndRemovePunctuation(content string) []string {
	tokens := make([]string, 0)
	var sb strings.Builder

	for index := 0; index < len(content); index++ {
		char := string(content[index])
		_, isPunc := punctuation[char]
		if char == " " {
			appendWord(&sb, &tokens)
			// Check if is new line char and go to next word
		} else if content[index] == 10 {
			appendWord(&sb, &tokens)
			sb.Reset()
		} else if isPunc {
			// Check if apostrophe — treat contractions as two words
			if sb.Len() != 0 && char == "'" {
				appendWord(&sb, &tokens)
				sb.Reset()
				sb.WriteString("'")
			}
			continue
		} else {
			sb.WriteByte(content[index])
		}
	}
	if sb.Len() != 0 {
		appendWord(&sb, &tokens)
	}
	return tokens
}

func appendWord(sb *strings.Builder, tokens *[]string) {
	currWord := strings.ToLower(sb.String())

	// Sanity check to see if it's a stopword
	if _, isStopWord := stopwords[currWord]; !isStopWord && sb.Len() != 1 {
		*tokens = append(*tokens, currWord)
	}

	sb.Reset()
}

func createTokenFrequencyMap(tokens []string) map[string]int {
	tokenFrequencyMap := make(map[string]int)

	for _, token := range tokens {
		tokenFrequencyMap[token] = tokenFrequencyMap[token] + 1
	}

	return tokenFrequencyMap
}

func initializeSets() {
	// Borrowing list of punctional & stopwords from https://github.dev/thesephist/monocle/blob/main/lib/tokenizer.ink
	punctuationRaw := []string{".", "?", "!", ",", ":", ";", "-", "(", ")", "\"", "'", "{", "}", "[", "]", "#", "<", ">", "\\",
		"~", "*", "_", "|", "%", "/"}
	stopwordsRaw := []string{"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "'re", "yours", "yourself", "yourselves", "he", "him",
		"his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
		"what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
		"have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
		"until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
		"after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then",
		"once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some",
		"such", "no", "nor", "not", "'t", "'nt", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
		"should", "now", "'ll", "won", "ya", "'s", "'m"}

	punctuation = make(map[string]bool)
	stopwords = make(map[string]bool)

	// Go doesn't have sets — let's make one for easy O(1) lookup through the use of a boolean map
	for _, each := range punctuationRaw {
		punctuation[each] = true
	}

	for _, each := range stopwordsRaw {
		stopwords[each] = true
	}
}
