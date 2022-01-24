from random import randint


def extract_possible_words(min_length=5, max_length=8, in_file="words.txt"):
    out_file_name = "" + str(min_length) + "-" + str(max_length) + "words.txt"
    with open(in_file, "r+") as file:
        with open(out_file_name, "w+") as write_to:
            for line in file:
                length = len(line)
                if length > min_length and length <= max_length + 1:
                    write_to.write(line)


def check_file(min_length, max_length):
    pass


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


extract_possible_words(10, 12, "words.txt")
# print(get_random_word("test.txt"))
