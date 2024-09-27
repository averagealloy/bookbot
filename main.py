def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
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
        final_list = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
        return final_list
        print(f"I am in char count {final_list}")
        # ^ it returns a list, but now its returning twice
    # print(f" I am calling the function{char_count(file_contents)}")

    the_freaking_list = char_count(file_contents)
        


    def report_printer(a_path,a_list):
        print(a_path)
        print(a_list)
    
    report_printer(path, the_freaking_list)
    



if __name__ == "__main__":
    main()
    
