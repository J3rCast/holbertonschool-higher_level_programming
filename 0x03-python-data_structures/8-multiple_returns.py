#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        new_tuple = (0, None)
    else:
        new_tuple = (len(sentece), sentence[0])

    return new_tuple
