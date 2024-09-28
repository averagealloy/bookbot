def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        # print(file_contents)


    def word_counter(super_string):
        words = super_string.split()
        final_word_number = len(words)
        return final_word_number
        
    # word_counter(file_contents)
    print(f"the words    {word_counter(file_contents)}")
    

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
        


    def report_printer(a_count,a_path,a_list):
        # print(a_count)
        print(f"--- Begin report of {a_path} ---\n{a_count} words found in the document\n")
        # print(a_list)
        for i in a_list:
            letter = i[0]
            value = i[1]
            print(f"The '{letter}' character was found {value} times")
        print("--- End report ---")
    
    report_printer(word_counter(file_contents) ,path, the_freaking_list)
    

if __name__ == "__main__":
    main()



"""
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
The 'i' character was found 24613 times
The 'n' character was found 24367 times
The 's' character was found 21155 times
The 'r' character was found 20818 times
The 'h' character was found 19725 times
The 'd' character was found 16863 times
The 'l' character was found 12739 times
The 'm' character was found 10604 times
The 'u' character was found 10407 times
The 'c' character was found 9243 times
The 'f' character was found 8731 times
The 'y' character was found 7914 times
The 'w' character was found 7638 times
The 'p' character was found 6121 times
The 'g' character was found 5974 times
The 'b' character was found 5026 times
The 'v' character was found 3833 times
The 'k' character was found 1755 times
The 'x' character was found 677 times
The 'j' character was found 504 times
The 'q' character was found 324 times
The 'z' character was found 243 times
--- End report ---
"""
