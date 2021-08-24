package sources

import (
	"github.com/nt92/memex/schema"
)

func GetRecords() []schema.Record {
	var messenger = getMessengerRecords()
	return messenger
}
