package sources
//
//import (
//	"database/sql"
//	"encoding/json"
//	"fmt"
//	"io/ioutil"
//	"log"
//	"os"
//
//	"github.com/nt92/memex/src/lib"
//	"github.com/nt92/memex/src/schema"
//
//	_ "github.com/mattn/go-sqlite3"
//)
//
//type AppleMessage struct {
//	Sender   string `json:"sender_name"`
//	Time     int    `json:"timestamp_ms"`
//	Content  string `json:"content"`
//	Type     string `json:"type"`
//	IsUnsent bool   `json:"is_unsent"`
//}
//
//type AppleMessages struct {
//	List []MessengerMessage `json:"messages"`
//}
//
//const appleMessagePath = "./../data/imessage/chat.db"
//const appleMessagePrefix = "imsg"
//
//func getAppleMessageRecords() schema.RecordInfo {
//	messageRecordMap := make(schema.RecordInfo)
//
//// 	sqliteDatabase, _ := sql.Open("sqlite3", appleMessagePath)
//
//	// Query for list of handles
//	// Loop through handles to find all individual messages & data
//
//	// for messageIndex, message := range messageList.List {
//	// 	messageID := fmt.Sprintf("%s-%d-%d", messengerPrefix, threadIndex, messageIndex)
//	// 	tokens := lib.GetTokenFrequencyMap(message.Content)
//
//	// 	messageRecord :=
//	// 		schema.Record{
//	// 			ID:             messageID,
//	// 			Title:          "Messenger Message from " + message.Sender,
//	// 			Content:        message.Sender + ": " + message.Content,
//	// 			Time:           message.Time / 1000,
//	// 			TokenFrequency: tokens,
//	// 		}
//	// 	messageRecordMap[messageID] = messageRecord
//	// }
//
//	return messageRecordMap
//}
//
//func getAppleMessageTokens() schema.TokenIndex {
//	var messengerFiles = getMessengerFileList()
//	tokenMap := make(schema.TokenIndex)
//
//	// for threadIndex, file := range messengerFiles {
//	for threadIndex := 0; threadIndex <= 100; threadIndex++ {
//		// currentJsonMessage, _ := os.Open(file)
//		currentJsonMessage, _ := os.Open(messengerFiles[threadIndex])
//		defer currentJsonMessage.Close()
//
//		byteValue, _ := ioutil.ReadAll(currentJsonMessage)
//
//		var messageList MessengerMessages
//		err := json.Unmarshal([]byte(byteValue), &messageList)
//		if err != nil {
//			log.Fatal(err)
//		}
//
//		for messageIndex, message := range messageList.List {
//			messageID := fmt.Sprintf("%s-%d-%d", messengerPrefix, threadIndex, messageIndex)
//			tokens := lib.GetTokenFrequencyMap(message.Content)
//
//			for token := range tokens {
//				_, ok := tokenMap[token]
//				if ok {
//					tokenMap[token] = append(tokenMap[token], messageID)
//				} else {
//					tokenMap[token] = []string{messageID}
//				}
//			}
//		}
//	}
//
//	return tokenMap
//}
