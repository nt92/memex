package main

import (
	"fmt"

	"github.com/nt92/memex/sources"
)

func main() {
	records := sources.GetRecords()

	for _, record := range records {
		fmt.Println(record.Content)
	}
}
