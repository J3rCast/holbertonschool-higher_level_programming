#!/usr/bin/python3
"""This moduele contains a function
that indent a string based on '?', '.',
':'
"""


def text_indentation(text):
    """ Arguments:
            text: string to be indented

        Returns:
            Error: is text is not a string
            Otherwise: prints new indented string
    """
    i = 0
    if type(text) is not str:
        raise TypeError("text must be a string")

    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(f"{text[i]}\n")
            i += 1
            if i < len(text):
                while text[i] == ' ':
                    i += 1
            continue
        print(text[i], end="")
        i += 1
