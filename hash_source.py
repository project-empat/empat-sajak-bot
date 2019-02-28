from local_settings import *
import glob
from hashlib import sha256

def hash_source():
    # text_model = json.loads(open('markov_model.json').read())
    text_data = ''
    files = glob.glob(DATA_SOURCE_FOLDER + "*.txt")

    for file in files:
        with open(file, encoding='utf-8') as corpus:
            text = corpus.read()
        text_data += text

    return sha256(text_data.encode('utf-8')).hexdigest()


if __name__ == "__main__":
    print(hash_source())
