package main

import (
	"fmt"

	"github.com/nt92/memex/src/lib"
	"github.com/nt92/memex/src/sources"
)

func main() {
	records := sources.GetRecords()

	for _, record := range records {
		fmt.Println(record)
	}

	lib.CreateDocsJson(records)
}
