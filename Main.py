

# This function reads the input file line by line and saves its content in a list
def file_reader(input_file_name, input_list):
    input_file = open(input_file_name, "rt")
    for line in input_file:
        input_list.append(line)


# This function generates the bigram dictionary of words which contains each word and its repetition and each two adjacent words
def bigram_dictionary_generator(sentences_list, words_dictionary):
    for sentence in sentences_list:
        words_list = sentence.split()
        for word in words_list:
            if word == "." or word == "," or word == "  " or word == ";" or word == "\"" or word == "\'" or word == "*" or word == "(" or word == ")":
                words_list.remove(word)

        # Adding each useful word to the dictionary
        for word in words_list:
            if word in words_dictionary:
                words_dictionary[word] += 1
            else:
                words_dictionary[word] = 1

        # Adding to adjacent words to the dictionary
        i = 0
        while i < (len(words_list) - 1):
            new_word = words_list[i] + " " + words_list[i + 1]
            if new_word in words_dictionary:
                words_dictionary[new_word] += 1
            else:
                words_dictionary[new_word] = 1
            i += 1














# Main part of the code starts here
negative_comments_list = []
positive_comments_list = []
file_reader("rt_polarity_positive.txt", positive_comments_list)
file_reader("rt_polarity_negative.txt", negative_comments_list)
positive_words_dictionary = {}
negative_words_dictionary = {}
bigram_dictionary_generator(positive_comments_list, positive_words_dictionary)
bigram_dictionary_generator(negative_comments_list, negative_words_dictionary)
























