def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)


    def word_counter(super_string):
        words = super_string.split()
        # print(len(words))
        
    word_counter(file_contents)

    def char_count(super_string):
        all_lower_case = super_string.lower()
        letter_count = {}
        for letter in all_lower_case:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        # sorted(myDict, key=myDict.get, reverse=True)
        final_sorted = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
        print(final_sorted)
        # ^ it returns a list
    char_count(file_contents)

    



if __name__ == "__main__":
    main()
    
