

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
redundant_words_list = []
i = 0
while i < 9:
    redundant_words_list.append(positive_words_list[0][0])
    positive_words_list.remove(positive_words_list[0])
    i += 1

positive_words_dictionary = {}
for i in positive_words_list:
    positive_words_dictionary[i[0]] = i[1]

redundant_pairs_list = []
for i in redundant_words_list:
    redundant_word = i + " "
    for j in positive_words_dictionary:
        if j.find(redundant_word) != -1:
            redundant_pairs_list.append(j)

for i in redundant_pairs_list:
    positive_words_dictionary.pop(i)



redundant_words_list = []
i = 0
while i < 9:
    redundant_words_list.append(negative_words_list[0][0])
    negative_words_list.remove(negative_words_list[0])
    i += 1

negative_words_dictionary = {}
for i in negative_words_list:
    negative_words_dictionary[i[0]] = i[1]

redundant_pairs_list = []
for i in redundant_words_list:
    redundant_word = i + " "
    for j in negative_words_dictionary:
        if j.find(redundant_word) != -1:
            redundant_pairs_list.append(j)

for i in redundant_pairs_list:
    negative_words_dictionary.pop(i)



positive_words_list = sorted(positive_words_dictionary.items(), key=lambda x: x[1], reverse=True)
negative_words_list = sorted(negative_words_dictionary.items(), key=lambda x: x[1], reverse=True)

positive_words_dictionary = {}
for i in positive_words_list:
    positive_words_dictionary[i[0]] = []
    positive_words_dictionary[i[0]].append(i[1])
negative_words_dictionary = {}
for i in negative_words_list:
    negative_words_dictionary[i[0]] = []
    negative_words_dictionary[i[0]].append(i[1])

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



m_variable_positive_dictionary = 0  # The number of repetition of all words in positive dictionary is stored here
for i in positive_words_dictionary:
    m_variable_positive_dictionary += positive_words_dictionary[i][0]

m_variable_negative_dictionary = 0  # The number of repetition of all words in negative dictionary is stored here
for i in negative_words_dictionary:
    m_variable_negative_dictionary += negative_words_dictionary[i][0]


# Finding the probability of each word in each dictionary
positive_words_keys = list(positive_words_dictionary)
i = 0
while i < len(positive_words_keys):
    if positive_words_keys[i].find(" ") != -1:
        words = positive_words_keys[i]
        words_list = words.split()
        first_word = words_list[0]
        positive_words_dictionary[positive_words_keys[i]].append(positive_words_dictionary[positive_words_keys[i]][0] / positive_words_dictionary[first_word][0])
    else:
        positive_words_dictionary[positive_words_keys[i]].append(positive_words_dictionary[positive_words_keys[i]][0] / m_variable_positive_dictionary)
    i += 1


negative_words_keys = list(negative_words_dictionary)
i = 0
while i < len(negative_words_keys):
    if negative_words_keys[i].find(" ") != -1:
        words = negative_words_keys[i]
        words_list = words.split()
        first_word = words_list[0]
        negative_words_dictionary[negative_words_keys[i]].append(negative_words_dictionary[negative_words_keys[i]][0] / negative_words_dictionary[first_word][0])
    else:
        negative_words_dictionary[negative_words_keys[i]].append(negative_words_dictionary[negative_words_keys[i]][0] / m_variable_negative_dictionary)
    i += 1



# Dictionary printer
output_file = open("positive_output.txt", "wt")
for i in positive_words_dictionary:
    output_file.write(i + ": " + str(positive_words_dictionary[i]) + "\n")
output_file.close()
output_file = open("negative_output.txt", "wt")
for i in negative_words_dictionary:
    output_file.write(i + ": " + str(negative_words_dictionary[i]) + "\n")
output_file.close()



















