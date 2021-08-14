package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	jsonExample, err := os.Open("data/example.json")
	if err != nil {
		fmt.Println(err)
	}

	defer jsonExample.Close()

	byteValue, _ := ioutil.ReadAll(jsonExample)

	var result map[string]interface{}
	json.Unmarshal([]byte(byteValue), &result)

	fmt.Println(result["users"])

	// fmt.Println("Please Enter Search Term:")
	// var term string
	// fmt.Scanln(&term)

	// fmt.Println(term)
}
