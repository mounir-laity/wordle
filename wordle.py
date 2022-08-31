from random import randint
from colorama import Fore, Style
from time import sleep


def extract_possible_words(min_length=5, max_length=8, in_file="dictionnary.txt"):
    out_file_name = "words.txt"
    with open(in_file, "r+") as file:
        with open(out_file_name, "w+") as write_to:
            for line in file:
                length = len(line)
                if length > min_length and length <= max_length + 1:
                    write_to.write(line)
    return out_file_name


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


def guess(guess: str, solution: str):
    states = []
    guess = guess.upper()
    solution = solution.upper()
    if len(guess) != len(solution):
        return None
    else:
        occurencies_solution = get_occurencies(solution)
        found_occurencies = dict()
        buffer: list[tuple[str, int]] = []
        for index, letter in enumerate(guess):
            if not is_in_word(letter, solution):
                states.append(-1)
            elif is_correctly_placed(letter, index, solution):
                states.append(1)
                if letter not in found_occurencies:
                    found_occurencies[letter] = 1
                else:
                    found_occurencies[letter] += 1
            else:
                buffer.append((letter, index))
        for element in buffer:
            if element[0] not in found_occurencies:
                states.insert(element[1], 0)
                found_occurencies[element[0]] = 1
            elif found_occurencies[element[0]] < occurencies_solution[element[0]]:
                found_occurencies[element[0]] += 1
                states.insert(element[1], 0)
            else:
                states.insert(element[1], -1)
    return states


def get_occurencies(word):
    occurencies = dict()
    for letter in word:
        if letter not in occurencies:
            occurencies[letter] = 1
        else:
            occurencies[letter] += 1
    return occurencies


def guess_exists(guess: str, file_name: str):
    with open(file_name, "r+") as file:
        for line in file:
            if guess.strip().upper() == line.strip().upper():
                return True
    return False


def is_in_word(letter: str, word: str):
    return letter.upper() in word.upper()


def is_correctly_placed(letter: str, letter_pos: int, word: str):
    return letter.upper() == word[letter_pos].upper()


def choose_min_size():
    min_size_chosen = False
    while not min_size_chosen:
        try:
            min_size = int(input("How many letters should your word be at least ?\n"))
            if min_size < 1 or min_size > 25:
                raise ValueError
            min_size_chosen = True
            print("Your word will be of at least", str(min_size), "letters long.")
        except ValueError:
            print("Please enter a number.")
    return min_size


def choose_max_size(min_size):
    max_size_chosen = False
    while not max_size_chosen:
        try:
            max_size = int(input("How many letters should your word be at most ?\n"))
            if max_size < min_size or max_size > 25:
                raise ValueError
            max_size_chosen = True
            print("Your word will be of at most", str(max_size), "letters long.")
        except ValueError:
            print("Please enter a number.")
    return max_size


if __name__ == "__main__":
    max_tries = 6
    tries = 0
    min_size = choose_min_size()
    max_size = choose_max_size(min_size)
    word = get_random_word(
        extract_possible_words(min_length=min_size, max_length=max_size)
    )
    word_length = len(word)

    print("Your word will have", str(word_length), "letters.")
    print("*" * word_length)
    discovered = []
    for i in range(word_length):
        discovered.append("*")
    try:
        while tries <= max_tries:
            word_guess = input(
                f"You have {str(max_tries - tries)} tries left. Please enter a guess.\n"
            )
            if word_guess is not None and word_guess.upper() == word.upper():
                print("Great job ! The word was indeed", word_guess.upper(), "!")
                exit(0)
            if not guess_exists(word_guess, "words.txt"):
                print("Please enter a valid word !")
                continue
            states = guess(word_guess, word)
            if states is None:
                print("Your guess must have", str(word_length), "letters !")
                continue
            result = ""
            for index, state in enumerate(states):
                letter = word_guess[index]
                if state == -1:
                    result = f"{Fore.RED}{letter}{Style.RESET_ALL}"
                    print(result, end="", flush=True)
                    sleep(0.5)
                elif state == 0:
                    result = f"{Fore.YELLOW}{letter}{Style.RESET_ALL}"
                    print(result, end="", flush=True)
                    sleep(0.5)
                else:
                    result = f"{Fore.GREEN}{letter}{Style.RESET_ALL}"
                    discovered[index] = result
                    print(result, end="", flush=True)
                    sleep(0.5)
            tries += 1
            print()
            print("".join(discovered))
        print("Game over ! The word was", word, "!")
    except KeyboardInterrupt:
        print("The word was", word, "!")
