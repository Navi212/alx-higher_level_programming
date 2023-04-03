#!/usr/bin/python3
"""
The ```5-text_indentation``` module povides a function that prints text
with 2 new lines after eash of these characters: ``` ., ?,and : ```
The function is ``` text_indentation() ```

Example:
>>>x = "Hello sam. what is your name? about:"
>>>text_indentation(x)
Hello sam.
what is your name?
about:
"""


def text_indentation(text):
    """ Prints a text with 2 lines. """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if ord(text[i]
               ) == 32 and ord(text[i - 1]
                               ) == 46 or ord(text[i - 1]
                                              ) == 63 or ord(text[i - 1]
                                                             ) == 58:
            print("")
            if text[i] == " ":
                print("")
                continue
        print(text[i], end="")


if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet,
consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
eatiorem! Iam ruinas videres""")
