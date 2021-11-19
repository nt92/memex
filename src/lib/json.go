package lib

import (
	"encoding/json"
	"os"

	"github.com/nt92/memex/src/schema"
)

func CreateDocsJson(records schema.RecordInfo) {
	json_data, _ := json.Marshal(records)

	file, _ := os.OpenFile(
		"./../output/docs.json",
		os.O_WRONLY|os.O_TRUNC|os.O_CREATE,
		0666,
	)

	defer file.Close()
	file.Write(json_data)
}

func CreateIndexJson(tokenIndex schema.TokenIndex) {
	json_data, _ := json.Marshal(tokenIndex)

	file, _ := os.OpenFile(
		"./../output/index.json",
		os.O_WRONLY|os.O_TRUNC|os.O_CREATE,
		0666,
	)

	defer file.Close()
	file.Write(json_data)
}
