def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()


    def word_counter(super_string):
        words = super_string.split()
        final_word_number = len(words)
        return final_word_number
    

    def char_count(super_string):
        all_lower_case = super_string.lower()
        letter_count = {}
        for letter in all_lower_case:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        final_list = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
        return final_list
        

    def report_printer(a_count,a_path,a_list):
        print(f"--- Begin report of {a_path} ---\n{a_count} words found in the document\n")
        for i in a_list:
            letter = i[0]
            value = i[1]
            print(f"The '{letter}' character was found {value} times")
        print("--- End report ---")
    
    report_printer(word_counter(file_contents) ,path, char_count(file_contents))
    

if __name__ == "__main__":
    main()