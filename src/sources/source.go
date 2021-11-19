package sources

import (
	"github.com/nt92/memex/src/schema"
)

func GetRecordsAndTokens() (schema.RecordInfo, schema.TokenIndex) {
	var messengerRecords, messengerTokens = getMessengerRecords()
	return messengerRecords, messengerTokens
}
