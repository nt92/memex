package main

import (
	"github.com/nt92/memex/src/lib"
	"github.com/nt92/memex/src/sources"
)

func main() {
	records := sources.GetRecords()
	tokens := sources.GetTokens()

	// for _, record := range records {
	// 	fmt.Println(record)
	// }

	lib.CreateDocsJson(records)
	lib.CreateIndexJson(tokens)
}
