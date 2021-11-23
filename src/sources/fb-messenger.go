package sources

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"

	"github.com/nt92/memex/src/lib"
	"github.com/nt92/memex/src/schema"
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

const messengerPath = "./../data/fb-messenger/messages/messages/inbox/"
const messengerPrefix = "msgr"

func getMessengerRecords() schema.RecordInfo {
	var messengerFiles = getMessengerFileList()
	messageRecordMap := make(schema.RecordInfo)

	// for threadIndex, file := range messengerFiles {
	for threadIndex := 0; threadIndex <= 100; threadIndex++ {
		// currentJsonMessage, _ := os.Open(file)
		currentJsonMessage, _ := os.Open(messengerFiles[threadIndex])
		defer currentJsonMessage.Close()

		byteValue, _ := ioutil.ReadAll(currentJsonMessage)

		var messageList MessengerMessages
		err := json.Unmarshal([]byte(byteValue), &messageList)
		if err != nil {
			log.Fatal(err)
		}

		for messageIndex, message := range messageList.List {
			messageID := fmt.Sprintf("%s-%d-%d", messengerPrefix, threadIndex, messageIndex)
			tokens := lib.GetTokenFrequencyMap(message.Content)

			messageRecord :=
				schema.Record{
					ID:             messageID,
					Title:          "Messenger Message from " + message.Sender,
					Content:        message.Sender + ": " + message.Content,
					Time:           message.Time / 1000,
					TokenFrequency: tokens,
				}
			messageRecordMap[messageID] = messageRecord
		}
	}

	return messageRecordMap
}

func getMessengerTokens() schema.TokenIndex {
	var messengerFiles = getMessengerFileList()
	tokenMap := make(schema.TokenIndex)

	// for threadIndex, file := range messengerFiles {
	for threadIndex := 0; threadIndex <= 100; threadIndex++ {
		// currentJsonMessage, _ := os.Open(file)
		currentJsonMessage, _ := os.Open(messengerFiles[threadIndex])
		defer currentJsonMessage.Close()

		byteValue, _ := ioutil.ReadAll(currentJsonMessage)

		var messageList MessengerMessages
		err := json.Unmarshal([]byte(byteValue), &messageList)
		if err != nil {
			log.Fatal(err)
		}

		for messageIndex, message := range messageList.List {
			messageID := fmt.Sprintf("%s-%d-%d", messengerPrefix, threadIndex, messageIndex)
			tokens := lib.GetTokenFrequencyMap(message.Content)

			for token := range tokens {
				_, ok := tokenMap[token]
				if ok {
					tokenMap[token] = append(tokenMap[token], messageID)
				} else {
					tokenMap[token] = []string{messageID}
				}
			}
		}
	}

	return tokenMap
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

// TODO: possibly remove records for "You are now connected on Messenger"
// TODO: figure out how to handle & index names properly
// TODO: handle emojis somehow
