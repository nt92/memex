package sources

import (
	"github.com/nt92/memex/src/schema"
)

func GetRecords() schema.RecordInfo {
	var messengerRecords = getMessengerRecords()
	return messengerRecords
}

func GetTokens() schema.TokenIndex {
	var messengerTokens = getMessengerTokens()
	return messengerTokens
}
