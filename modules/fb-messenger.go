package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
)

type Message struct {
	Sender   string `json:"sender_name"`
	Time     int    `json:"timestamp_ms"`
	Content  string `json:"content"`
	Type     string `json:"type"`
	IsUnsent bool   `json:"is_unsent"`
}

type Messages struct {
	List []Message `json:"messages"`
}

func main() {
	var files []string

	root := "data/fb-messenger/messages/messages/inbox/"
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if filepath.Ext(path) != ".json" {
			return nil
		}
		files = append(files, path)
		return nil
	})
	if err != nil {
		panic(err)
	}

	fmt.Println(len(files))

	// for _, file := range files {
	// 	fmt.Println(file)
	// 	currentJsonMessage, _ := os.Open(file)
	// 	defer currentJsonMessage.Close()

	// 	byteValue, _ := ioutil.ReadAll(currentJsonMessage)

	// 	var result map[string]interface{}
	// 	json.Unmarshal([]byte(byteValue), &result)

	// 	fmt.Println(result["messages"])
	// }

	var file string
	file = files[2]

	currentJsonMessage, _ := os.Open(file)
	defer currentJsonMessage.Close()

	byteValue, _ := ioutil.ReadAll(currentJsonMessage)

	var messageList Messages
	if err := json.Unmarshal([]byte(byteValue), &messageList); err != nil {
		log.Fatal(err)
	}

	for _, x := range messageList.List {
		fmt.Println(x.Sender + ": " + x.Content)
	}

	fmt.Println(messageList.List[0].Content)

	// fmt.Println("Please Enter Search Term:")
	// var term string
	// fmt.Scanln(&term)

	// fmt.Println(term)
}
