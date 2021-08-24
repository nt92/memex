package sources

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"

	"github.com/nt92/memex/schema"
)

type MessengerMessage struct {
	Sender   string `json:"sender_name"`
	Time     int    `json:"timestamp_ms"`
	Content  string `json:"content"`
	Type     string `json:"type"`
	IsUnsent bool   `json:"is_unsent"`
}

type MessengerMessages struct {
	List []MessengerMessage `json:"messages"`
}

const messengerPath = "./data/fb-messenger/messages/messages/inbox/"

func getMessengerRecords() []schema.Record {
	var messengerFiles = getMessengerFileList()
	var messageRecordList []schema.Record

	// for , file := range messengerFiles {
	for i := 0; i <= 2; i++ {
		// currentJsonMessage, _ := os.Open(file)
		currentJsonMessage, _ := os.Open(messengerFiles[i])
		defer currentJsonMessage.Close()

		byteValue, _ := ioutil.ReadAll(currentJsonMessage)

		var messageList MessengerMessages
		err := json.Unmarshal([]byte(byteValue), &messageList)
		if err != nil {
			log.Fatal(err)
		}

		for _, message := range messageList.List {
			messageRecord :=
				schema.Record{
					ID:      "TODO",
					Title:   "Messenger Message from " + message.Sender,
					Content: message.Sender + ": " + message.Content,
					Time:    message.Time,
				}
			messageRecordList = append(messageRecordList, messageRecord)
		}
	}

	return messageRecordList
}

func getMessengerFileList() []string {
	var files []string
	err :=
		filepath.Walk(
			messengerPath,
			func(path string, info os.FileInfo, err error) error {
				if filepath.Ext(path) != ".json" {
					return nil
				}
				files = append(files, path)
				return nil
			})
	if err != nil {
		panic(err)
	}

	return files
}
