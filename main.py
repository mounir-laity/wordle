from random import randint
from os.path import exists


def extract_possible_words(min_length=5, max_length=8, in_file="words.txt"):
    out_file_name = "" + str(min_length) + "-" + str(max_length) + "_letters_words.txt"
    if not check_file(min_length, max_length):
        with open(in_file, "r+") as file:
            with open(out_file_name, "w+") as write_to:
                for line in file:
                    length = len(line)
                    if length > min_length and length <= max_length + 1:
                        write_to.write(line)
    return out_file_name


def check_file(min_length, max_length):
    file_name = str(min_length) + "-" + str(max_length) + "_letters_words.txt"
    return exists(file_name)


def get_random_word(file):
    with open(file, "r+") as words_list:
        num_lines = sum(1 for line in words_list)
        if num_lines > 0:
            chosen_num = randint(1, num_lines)
        else:
            return None
    with open(file, "r+") as words_list:
        for line_num, word in enumerate(words_list):
            if line_num == chosen_num:
                return word.strip()
        return None


print(get_random_word(extract_possible_words(3, 5, "words.txt")))
