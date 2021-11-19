package lib

import "github.com/nt92/memex/src/schema"

// Function to take the maps of various records and merge them together for the
// final index that will be in docs.json
func MergeMaps(maps ...map[string]schema.Record) map[string]schema.Record {
	result := map[string]schema.Record{}
	for _, recordMap := range maps {
		for key := range recordMap {
			result[key] = recordMap[key]
		}
	}
	return result
}
