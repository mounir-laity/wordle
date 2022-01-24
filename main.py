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


# print(get_random_word(extract_possible_words(3, 5, "words.txt")))

if __name__ == "__main__":
    min_size_chosen = False
    max_size_chosen = False
    while not min_size_chosen:
        min_size = input("How many letters should your word be at least ?\n")
        try:
            min_size = int(min_size)
            if min_size < 1 or min_size > 25:
                raise ValueError
            min_size_chosen = True
            print("Your word will be of at least", str(min_size), "letters long.")
        except ValueError:
            print("Please enter a number.")
    while not max_size_chosen:
        max_size = input("How many letters should your word be at most ?\n")
        try:
            max_size = int(max_size)
            if max_size < min_size or max_size > 25:
                raise ValueError
            max_size_chosen = True
            print("Your word will be of at most", str(max_size), "long.")
        except ValueError:
            print("Please enter a number.")
    print(
        get_random_word(
            extract_possible_words(min_length=min_size, max_length=max_size)
        )
    )
