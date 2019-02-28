import markovify
import random
from hash_source import *
import os.path
import json


def build_models():
    # text_model = json.loads(open('markov_model.json').read())
    text_data = ''
    files = glob.glob(DATA_SOURCE_FOLDER + "*.txt")
    if not hash_source() != DATA_SOURCE_HASH and not os.path.isfile(MARKOV_MODEL_JSON):
        print("Read file")
        for file in files:
            with open(file, encoding='utf-8') as corpus:
                text = corpus.read()
            text_data += text

        try:
            text_model = markovify.NewlineText(text_data)
            file = open(MARKOV_MODEL_JSON, "w")
            file.write(text_model.to_json())
        except Exception as err:
            text_model = None
    else:
        print("Use generated model")
        try:
            text_model = markovify.Text.from_json(json.dumps(json.loads(open(MARKOV_MODEL_JSON).read())))
        except Exception as err:
            print(err)
            text_model = None

    return text_model


def generate_poems():
    text_model = build_models()

    if text_model != None:
        try:
            lines_possible = [2, 3, 4, 5, 6]
            lines = lines_possible[random.randint(1, len(lines_possible)) - 1]

            poem = [text_model.make_short_sentence(50) for i in range(lines)]

            toupper_ind = []
            tolower_ind = []
            for i in range(len(poem)):
                line = poem[i]
                end_line = line[len(line) - 1]
                if end_line == ',' and i + 1 < len(poem):
                    tolower_ind = tolower_ind + [i + 1]
                elif end_line == "." and i + 1 < len(poem):
                    toupper_ind = toupper_ind + [i + 1]
                elif end_line.isalpha() == True and i + 1 < len(poem):
                    tolower_ind = tolower_ind + [i + 1]

            poem_list = []
            for i in range(len(poem)):
                line = poem[i]
                if (i in toupper_ind) == True:
                    line = line[0].upper() + line[1:]
                    poem_list = poem_list + [line]
                elif (i in tolower_ind) == True:
                    line = line[0].lower() + line[1:]
                    poem_list = poem_list + [line]
                else:
                    poem_list = poem_list + [line]

            poem = '\n'.join(poem_list)
        except Exception as err:
            poem = ''
    else:
        poem = ''

    return poem


if __name__ == "__main__":
    poem = generate_poems()
    print(poem)
