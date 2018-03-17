##################################################################################################################
"""
Author : Wajih
"""
import numpy as np

def name_matcher(sentence, autom_matrix):
    is_matched = False

    word_chars = [autom_matrix[x, 0] for x in range(1, autom_matrix.shape[0])]

    for word in sentence.split(' '):
        # Start with initial state
        current_state = 0
        for chr in word:
            for i in range(1, autom_matrix.shape[0]):

                if chr.strip() not in word_chars:
                    current_state = 0
                    continue

                if chr == autom_matrix[i, 0]:

                    for j in range(1, autom_matrix.shape[1]):
                        if current_state == int(autom_matrix[0, j]):

                            current_state = int(autom_matrix[i, j])

                            # Automata Reached end state successfully
                            if current_state == len(word_chars):
                                is_matched = True
                                return is_matched
                            break

    return is_matched


def main():
    sentence = 'this program belongs to WAJIH and is an assignment.'
    autom_matrix = np.matrix([[-1, 0, 1, 2, 3, 4], ['W', 1, 0, 0, 0, 0],
    ['A', 0, 2, 0, 0, 0], ['J', 0, 0, 3, 0, 0], ['I', 0, 0, 0, 4, 0],['H', 0, 0, 0, 0, 5]])

    match = name_matcher(sentence, autom_matrix)

    if match:
        print "Matched name in string"
    else:
        print "Name not found in string"


if __name__ == "__main__": 
    main()

