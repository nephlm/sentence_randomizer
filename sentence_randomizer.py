# Sentece ranomizer
# runs in nltk virtenv on python3

# need punkt corpus
# gotten originally by running:
# nltk.download('punkt')

RANGE = 1000

import argparse
import random

# import nltk.data
import nltk.tokenize

def get_data(args):
    raw_text = open(args.path).read()
    return raw_text

    
def parse_sentences(raw_text):
    # tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    # sentences = tokenizer.tokenize(data)
    sentences = nltk.tokenize.sent_tokenize(raw_text)
    return sentences
    
def score_sentence(sentence):
    return int(sum([ord(x) for x in sentence]) % RANGE)


def randomize(sentences, true_random):
    random_sentences = []
    for idx, sentence in enumerate(sentences):
        random_sentences.append({'idx': idx, 'sentence': sentence, 'score': score_sentence(sentence)})
    if true_random:
        random.shuffle(random_sentences)
        return random_sentences
    else:
        return sorted(random_sentences, key=lambda k: k['score'])

def display(randomized_sentences):
    num_sentences = len(randomized_sentences)
    for num, sdict in enumerate(randomized_sentences):
        print(f'\n{num + 1} / {num_sentences} ({sdict["idx"] +1})')
        print(f'{sdict["sentence"]}\n')
        print(' ------ ')

def main(args):
    raw_text = get_data(args)
    sentences = parse_sentences(raw_text)
    randomized_sentences = randomize(sentences, args.random)
    display(randomized_sentences)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'A small script to randomize the sentences in a text file.'
    parser.add_argument('path', metavar='PATH',
                help='Path to a text file.')
    parser.add_argument('-r', '--random', default=False, action='store_true', 
                help='Order the sentences using true randomization (non-repeatable)')
    args =  parser.parse_args()
    main(args)

