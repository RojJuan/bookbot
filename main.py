def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words_count()
        character_count()
        report()


def words_count():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))


def character_count():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_filecontents = file_contents.lower()
        char_count = {}

        for char in lowered_filecontents:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        print(char_count)


def sort_on(dict):
    return dict["num"]


def report():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_filecontents = file_contents.lower()
        char_count = {}

        for char in lowered_filecontents:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        char_list = [{"char": key, "num": value} for key, value in char_count.items()]
        char_list.sort(key=sort_on, reverse=True)

        print("\n--- Begin report of books/frankenstein.txt ---")
        word_count = len(file_contents.split())
        print(f"{word_count} were found in the document\n")

        for item in char_list:
            char = item["char"]
            count = item["num"]
            print(f"The '{char}' character was found {count} times")

        print("--- End report ---")


main()
