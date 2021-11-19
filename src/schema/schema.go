package schema

/*
This record represents the data that will be stored in the inverted index.
Each piece of content that can be surfaced to the user will conform to this
format — the client-side index will utilize this.
*/
type Record struct {
	// A globally unique identifier for this item across all items
	// It's a 2 letter prefix for mod (e.g. "tw" for Tweets) and a number
	ID string `json:"id"`

	// The title of the piece of content
	Title string `json:"title"`

	// The item's text content to be be displayed in the results
	Content string `json:"content"`

	// Potential link to the source if applicable
	Link string `json:"link"`

	// A map of <each_token_in_item>:<number_of_times_in_item>
	TokenFrequency map[string]int `json:"tokenFrequency"`

	// A relevant timestamp for the item
	Time int `json:"timestamp"`
}

// Turn the records into a map so that we can search based on the ID key
type RecordInfo map[string]Record
