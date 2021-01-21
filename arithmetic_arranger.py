import sys


def arithmetic_arranger(problems):
    #! print error message if there are more than 5 problems
    if len(problems) > 5:
        print("Error: Too many problems.")
        sys.exit()

    answers = []  # array to store answers to the problems
    for prob in problems:
        split = prob.split()
        lengths = {}  # key = string, value = length
        for i in range(len(split)):
            elt_length = len(split[i])
            lengths.append(split[i], elt_length)

        lengths

    return arranged_problems
