import os

mega_doc_pos = ""
mega_doc_neg = ""

positive_files = os.listdir(os.getcwd() + '\\pos\\')
negative_files =  os.listdir(os.getcwd() + '\\neg\\')

for mfile in positive_files:
    mega_doc_pos += open(os.getcwd() + '\\pos\\' + mfile , 'r').read()

for mfile in negative_files:
    mega_doc_neg += open(os.getcwd() + '\\neg\\' + mfile , 'r').read()

test_sentence = "This is a fantastic film"

total_words_in_pos = mega_doc_pos.split(' ')
total_words_in_neg = mega_doc_neg.split(' ')

vocab_pos = list(set(total_words_in_pos))
vocab_neg = list(set(total_words_in_neg))

positive_class_probability = (float(len(positive_files))) / (len(positive_files) + len(negative_files))
negaitive_class_probability = (float(len(negative_files))) / (len(positive_files) + len(negative_files))

sentence_probab_pos = {}

for x in test_sentence.split(' '):
    count_of_word_in_vocab = total_words_in_pos.count(x)
    sentence_probab_pos[x] = float(((count_of_word_in_vocab) + 1)) / (len(total_words_in_pos) + len(vocab_pos))

sentence_probab_neg = {}

for x in test_sentence.split(' '):
    count_of_word_in_vocab = total_words_in_neg.count(x)
    sentence_probab_neg[x] = float(((count_of_word_in_vocab) + 1)) / (len(total_words_in_neg) + len(vocab_neg))

positive = positive_class_probability * reduce(lambda x, y: x*y, sentence_probab_pos.values())
negative = negaitive_class_probability * reduce(lambda x, y: x*y, sentence_probab_neg.values())

class_belongs = "Belongs to Positive Class" if positive > negative else "Belongs to Negative Class"

print class_belongs