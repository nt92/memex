package main

import (
	"fmt"

	"github.com/nt92/memex/src/lib"
	"github.com/nt92/memex/src/sources"
)

func main() {
	records := sources.GetRecords()
	tokens := sources.GetTokens()

	lib.CreateDocsJson(records)
	lib.CreateIndexJson(tokens)

	fmt.Print("Enter a search term: ")
	var searchTerm string
	fmt.Scanln(&searchTerm)

	lib.SearchIndex(searchTerm)
}
