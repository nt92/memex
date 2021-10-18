package lib

import (
	"strings"
)

var punctuation map[string]bool
var stopwords map[string]bool

func GetTokenFrequencyMap(content string) map[string]int {
	tokenFrequencyMap := make(map[string]int)
	tokens := splitStringBySpace(content)

	return tokenFrequencyMap
}

func splitStringBySpace(content string) []string {
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

func initializeSets() {
	// Borrowing list of punctional & stopwords from https://github.dev/thesephist/monocle/blob/main/lib/tokenizer.ink
	punctuationRaw := []string{".", "?", "!", ",", ":", ";", "-", "(", ")", "\"", "'", "{", "}", "[", "]", "#", "<", ">", "\\",
		"~", "*", "_", "|", "%", "/"}
	stopwordsRaw := []string{"a", "about", "an", "are", "and", "as", "at", "be", "but", "by",
		"com", "do", "don\"t", "for", "from", "has", "have", "he", "his", "http",
		"https", "i", "i\"m", "in", "is", "it", "it\"s", "just", "like", "me",
		"my", "not", "of", "on", "or", "rt", "so", "t", "that", "the", "they",
		"this", "to", "twitter", "was", "we", "were", "with", "you", "your"}

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
