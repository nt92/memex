package lib

import (
	"encoding/json"
	"os"

	"github.com/nt92/memex/src/schema"
)

func CreateDocsJson(records []schema.Record) {
	json_data, _ := json.Marshal(records)

	file, _ := os.OpenFile(
		"./../output/docs.json",
		os.O_WRONLY|os.O_TRUNC|os.O_CREATE,
		0666,
	)

	defer file.Close()
	file.Write(json_data)
}

func CreateIndexJson() {

}
