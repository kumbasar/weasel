#!/usr/bin/env python3

import logging
import string
import random
import os
import time
import sys

""" Input parameters """
_defaultTestString = "METHINKS IT IS LIKE A WEASEL"
_population_size = 100
_mutation_rate = 0.05
_sleep_time = 0.01


def randomtext(chars, length):
    """ Create inital random text """
    return ''.join(random.choice(chars) for i in range(length))


def mutatetext(text, mutate=_mutation_rate):
    """ mutate the text """
    newtext = ''
    for i in text:
        if random.random() <= mutate:
            newtext += random.choice(chars)
        else:
            newtext += i

    return newtext


def scoring(source, target):

    """ Score the test """

    score = 0

    for idx in range(len(target)):

        if ord(source[idx]) == ord(target[idx]):
            score += 1

    return score


def get_chars():
    # letters + digits + whitespace
    chars = string.ascii_letters + string.digits + " "

    logging.info("char list is '{}'".format(chars))

    return chars


if __name__ == "__main__":

    logging.basicConfig(filename="weasel.log", level=logging.INFO,
                        filemode='w')

    if len(sys.argv) == 2 and sys.argv[1]:
        targetString = sys.argv[1]
    else:
        targetString = _defaultTestString

    logging.info("Target text is '{}'".format(targetString))

    # Create chars
    chars = get_chars()
    max_score = len(targetString)
    logging.info("Max score is {}".format(max_score))

    gen_text = randomtext(chars, len(targetString))
    logging.info("Inital text: {}".format(gen_text))

    gen_score = scoring(gen_text, targetString)
    logging.info("'{}' score is {}".format(gen_text, gen_score))
    logging.info("Population size: {}".format(_population_size))
    logging.info("Mutation rate: {}".format(_mutation_rate))

    generation = 0

    while (gen_score < max_score):

        pop_text = gen_text
        generation += 1

        for i in range(_population_size):
            new_text = mutatetext(pop_text)
            new_score = scoring(new_text, targetString)

            if new_score > gen_score:
                gen_score = new_score
                gen_text = new_text

                if gen_score == max_score:
                    break

        logging.info("{}. {} score: {}".format(generation,
                     gen_text, gen_score))

        os.system('clear')
        print(gen_text)
        time.sleep(_sleep_time)
