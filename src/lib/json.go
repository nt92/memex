package lib

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/nt92/memex/src/schema"
)

const docsJsonPath = "./../output/docs.json"
const indexJsonPath = "./../output/index.json"

func CreateDocsJson(records schema.RecordInfo) {
	json_data, _ := json.Marshal(records)

	file, _ := os.OpenFile(
		docsJsonPath,
		os.O_WRONLY|os.O_TRUNC|os.O_CREATE,
		0666,
	)

	defer file.Close()
	file.Write(json_data)
}

func CreateIndexJson(tokenIndex schema.TokenIndex) {
	json_data, _ := json.Marshal(tokenIndex)

	file, _ := os.OpenFile(
		indexJsonPath,
		os.O_WRONLY|os.O_TRUNC|os.O_CREATE,
		0666,
	)

	defer file.Close()
	file.Write(json_data)
}

func SearchIndex(searchTerm string) {
	indexFile, _ := os.Open(indexJsonPath)
	defer indexFile.Close()
	byteValue, _ := ioutil.ReadAll(indexFile)

	var tokenIndex schema.TokenIndex
	err := json.Unmarshal([]byte(byteValue), &tokenIndex)
	if err != nil {
		log.Fatal(err)
	}

	searchRecords(tokenIndex[searchTerm])
}

func searchRecords(IDs []string) {
	recordsFile, _ := os.Open(docsJsonPath)
	defer recordsFile.Close()
	byteValue, _ := ioutil.ReadAll(recordsFile)

	var recordInfo schema.RecordInfo
	err := json.Unmarshal([]byte(byteValue), &recordInfo)
	if err != nil {
		log.Fatal(err)
	}

	for _, ID := range IDs {
		recordContent := recordInfo[ID].Content
		recordTime := recordInfo[ID].Time
		fmt.Println(TimestampToDate(recordTime), recordContent)
	}
}
