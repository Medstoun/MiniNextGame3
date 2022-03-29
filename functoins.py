import random

def get_word():

    words = "words.txt"

    with open(words, "r") as file:
        lines = file.read()
        split_lines = lines.splitlines()

    return split_lines

def random_letters(word):

    result = random.sample(word, len(word))

    return "".join(result)

def save_point(name, score):

    history = "history.txt"

    with open(history, "a") as file:
        file.write(f"{name}   {score}\n")

def get_statistics():

    history = "history.txt"
    scores = []

    with open(history, "r") as file:
        for line in file:
            score = line.strip().split(" ")[-1]
            scores.append(int(score))

    max_score = max(scores)
    len_score = len(scores)

    return {"max": max_score, "len": len_score}






