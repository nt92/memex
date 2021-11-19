package sources

import (
	"github.com/nt92/memex/src/schema"
)

func GetRecords() schema.RecordInfo {
	var messenger = getMessengerRecords()
	return messenger
}
