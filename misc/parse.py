import json
import csv
from nltk.tokenize.treebank import TreebankWordDetokenizer
import re

csv_file = open('../mturk_data1.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
field = ['text', 'trigger']
writer.writerow(field)


json_file = open('../WikiEvents/data/train_info.jsonl', 'r')

train_json = list(json_file)

json_file.close()

# output = open('output.txt', 'w')

for i in range(2, 7):
    example = json.loads(train_json[i].encode('utf-8'))
    for event in example['event_mentions']:
        revert = example['tokens'][event['trigger']['start']]
        example['tokens'][event['trigger']['start']] = '<b>' + example['tokens'][event['trigger']['start']] + '</b>'
        text = TreebankWordDetokenizer().detokenize(example['tokens'])
        text = re.sub('\s*,\s*', ', ', text)
        text = re.sub('\s*\.\s*', '. ', text)
        text = re.sub('\s*\?\s*', '? ', text)
        text = re.sub('\s*\-\s*', '-', text)
        text = re.sub('\s*\’\s*', '’', text)
        text = re.sub('\s*\“\s*', ' “', text)
        text = re.sub('\s*\”\s*', '” ', text)
        text = re.sub('\s*\–\s*', '–', text)
        text = re.sub('\s*\'\s*', "'", text)
        text = re.sub('\s*\"\s*', '"', text)
        
        writer.writerow([text, event['trigger']['text']])
        example['tokens'][event['trigger']['start']] = revert

# triggers = []

# for i in example['event_mentions']:
#     triggers.append(i['trigger']['text'])

# prompt = 'Here is a passage: {passage}\nProvide wh* questions with their corresponding answers regarding each of the following triggers: {triggers}. The questions must start with either who, what, or when, and must include a trigger word. Answers must come from direct quotes in the passage.'.format(passage=example['text'], triggers=', '.join(triggers))

# print('prompt:', prompt)

# for entry in train_json:
#     json_object = json.loads(entry)
#     print('text:')
#     print(json_object['text'].encode('utf-8'))
#     print('\n')
#     print('triggers:')
#     for mention in json_object['event_mentions']:
#         print(mention['trigger']['text'])
#     print('\n')
    # output.write('text: ')
    # output.write(json_object['text'])
    # output.write('\n\n')
    # output.write('entity mentions: ')
    # output.write(json.dumps(json_object['entity_mentions']))
    # output.write('\n\n')
    # output.write('relation mentions: ')
    # output.write(json.dumps(json_object['relation_mentions']))
    # output.write('\n\n')
    # output.write('event mentions: ')
    # output.write(json.dumps(json_object['event_mentions']))
    # output.write('\n\n')

# output.close()