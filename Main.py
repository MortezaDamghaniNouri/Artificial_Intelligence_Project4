

# This function reads the input file line by line and saves its content in a list
def file_reader(input_file_name, input_list):
    input_file = open(input_file_name, "rt")
    for line in input_file:
        input_list.append(line)


# This function generates the bigram dictionary of words which contains each word and its repetition and each two adjacent words
def bigram_dictionary_generator(sentences_list, words_dictionary):
    for sentence in sentences_list:
        words_list = sentence.split()
        redundant_words_index = []
        i = 0
        while i < len(words_list):
            if words_list[i] == "." or words_list[i] == "," or words_list[i] == "  " or words_list[i] == ";" or words_list[i] == "\"" or words_list[i] == "\'" or words_list[i] == "*" or words_list[i] == "(" or words_list[i] == ")" or words_list[i] == "--" or words_list[i] == "-"\
                    or words_list[i] == "?" or words_list[i] == "!" or words_list[i] == "&" or words_list[i] == ":" or words_list[i] == "." or words_list[i] == "و":
                redundant_words_index.append(words_list[i])

            i += 1
        for i in redundant_words_index:
            words_list.remove(i)

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
# Sorting two generated dictionaries
positive_words_list = sorted(positive_words_dictionary.items(), key=lambda x: x[1], reverse=True)
negative_words_list = sorted(negative_words_dictionary.items(), key=lambda x: x[1], reverse=True)
# Removing top ten words
i = 0
while i < 9:
    positive_words_list.remove(positive_words_list[i])
    i += 1
i = 0
while i < 9:
    negative_words_list.remove(negative_words_list[i])
    i += 1


positive_words_dictionary = {}
for i in positive_words_list:
    positive_words_dictionary[i[0]] = [i[1]]
negative_words_dictionary = {}
for i in negative_words_list:
    negative_words_dictionary[i[0]] = [i[1]]

redundant_words = []
for i in positive_words_dictionary:
    if positive_words_dictionary[i][0] <= 2:
        redundant_words.append(i)
for i in redundant_words:
    positive_words_dictionary.pop(i)

redundant_words = []
for i in negative_words_dictionary:
    if negative_words_dictionary[i][0] <= 2:
        redundant_words.append(i)
for i in redundant_words:
    negative_words_dictionary.pop(i)



# Dictionary printer
# output_file = open("output.txt", "wt")
# for i in positive_words_dictionary:
#     output_file.write(i + ": " + str(positive_words_dictionary[i][0]) + "\n")
# output_file.close()




















