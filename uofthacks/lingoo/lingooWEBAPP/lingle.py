# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from lingooWEBAPP.split_article import find_sentences

def make_lists(color, text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    text_to_read = text
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
                text_score[k], text_score[k + 1] = text_score[k + 1], text_score[k]

    # remove the entities with type == OTHER from text_name
    for entity in response.entities:
        entity_type = enums.Entity.Type(entity.type)
        if entity_type.name == "OTHER":
            index = text_name.index(entity.name)
            text_name.remove(entity.name)
            del text_score[index]

    # take the first n entities with the highest salience,
    # if the len(text_name) >= n
    # otherwise, take all entities in text_name
    NUM_ENTITIES = 3
    i = min(NUM_ENTITIES, len(text_name)) #min not taking min value??
    first_three_entities = text_name[:i]
    first_three_entities_score = text_score[:i]

    # add the sentence containing one of the three entities into list_extract
    sentence_list = find_sentences(text_to_read)
    blue = []
    red = []
    yellow = []
    if i==0:
        yellow = sentence_list
    else:
        for sentence in sentence_list:
            whether_in = 0
            score = 0
            for q in range(i):
                if first_three_entities[q] in sentence:
                    whether_in = 1
            #if ((first_three_entities[0] in sentence or
 #              first_three_entities[1] in sentence) or
 #              first_three_entities[2] in sentence):
 #               whether_in = 1
            if whether_in == 1:
                for q in range(i):
                    if first_three_entities[q] in sentence:
                        score += first_three_entities_score[q]
                #if first_three_entities[0] in sentence:
 #                   score += first_three_entities_score[0]
 #               elif first_three_entities[1] in sentence:
#                    score += first_three_entities_score[1]
#                elif first_three_entities[2] in sentence:
#                    score += first_three_entities_score[2]
            if (score == 0 and whether_in == 1) is True:
                yellow.append(sentence)
            elif score < 0:
                blue.append(sentence)
            elif score > 0:
                red.append(sentence)

    if color == "blue":
        return blue
    if color == 'red':
        return red
    if color == 'yellow':
        return yellow

def get_blue(text):
    return make_lists("blue", text)

def get_red(text):
    return make_lists("red", text)

def get_yellow(text):
    return make_lists("yellow", text)

