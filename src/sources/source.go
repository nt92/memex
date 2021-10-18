package sources

import (
	"github.com/nt92/memex/src/schema"
)

func GetRecords() []schema.Record {
	var messenger = getMessengerRecords()
	return messenger
}
