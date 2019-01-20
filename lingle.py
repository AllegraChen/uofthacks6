# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from split_article import find_sentences

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = open("article.txt", 'r')
text_to_read = text.read()
document = types.Document(content=text_to_read,
                          type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
# Detects the entities of the text
response = client.analyze_entities(document=document, encoding_type='UTF32')
# Detects the entities' score of the text
response_two = client.analyze_entity_sentiment(document=document,
                                               encoding_type='UTF32')

# build four list containing all the information from the text
# like the name, type,metadata and salience
i = 0
text_name = []
text_type = []
text_metadata = []
text_salience = []
text_score = []

for entity in response.entities:
    text_name.append(entity.name)
    text_type.append(entity.type)
    text_metadata.append(entity.metadata)
    text_salience.append(entity.salience)
    if entity.name != response_two.entities[i].name
        print("wrong")
    text_score.append(response_two.entities[i].sentiment.score)
    i = i + 1

# list these list in order according to the salience
length = len(text_salience)
for j in range(0, length - 1):
    for k in range(0, length - j - 1):
        if text_salience[k] < text_salience[k + 1]:
            text_name[k], text_name[k + 1] = text_name[k + 1], text_name[k]
            text_type[k], text_type[k + 1] = text_type[k + 1], text_type[k]
            text_metadata[k], text_metadata[k + 1] = text_metadata[k + 1], \
                                                     text_metadata[k]
            text_salience[k], text_salience[k + 1] = text_salience[k + 1], \
                                                     text_salience[k]
            text_score[k], text_score[k + 1] = text_score[k + 1], text_score[k], \
                                               text_salience[k]

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
print(text_name)

# for entity in text_name:
#     if entity.type ==
