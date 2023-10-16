The data in presented in jsonl format

Each line has an object of the format
{
    doc_id: id of document
    tokens: list of tokens in document
    sentences: list of sentences
    entity_mentions: doesnt matter
    relation mentions: doesnt matter
    event_mentions: list of events
}

where sentence: [
    list of metawords 
    sentence string
]

where metaword: [
    word string
    start pos
    end pos
]

where event: {
    id: id of event
    event_type: type of event
    trigger: {
        start pos
        end pos
        trigger text
        sent_idx ???
    }
    list of arguments
}

where argument: {
    entity_id
    role
    text
}

Download data via:
- `wget https://gen-arg-data.s3.us-east-2.amazonaws.com/wikievents/data/<split>.jsonl` for split={train, dev,test}.