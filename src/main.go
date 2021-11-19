package main

import (
	"github.com/nt92/memex/src/lib"
	"github.com/nt92/memex/src/sources"
)

func main() {
	records, tokens := sources.GetRecordsAndTokens()

	// for _, record := range records {
	// 	fmt.Println(record)
	// }

	lib.CreateDocsJson(records)
	lib.CreateIndexJson(tokens)
}
