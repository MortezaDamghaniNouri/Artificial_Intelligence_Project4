

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
# Removing last 10 sentences of lists to save them for testing
i = 0
while i < 9:
    positive_comments_list.pop(len(positive_comments_list) - 1)
    i += 1

i = 0
while i < 9:
    negative_comments_list.pop(len(negative_comments_list) - 1)
    i += 1


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
# output_file = open("positive_output.txt", "wt")
# for i in positive_words_dictionary:
#     output_file.write(i + ": " + str(positive_words_dictionary[i]) + "\n")
# output_file.close()
# output_file = open("negative_output.txt", "wt")
# for i in negative_words_dictionary:
#     output_file.write(i + ": " + str(negative_words_dictionary[i]) + "\n")
# output_file.close()

while True:
    print("Enter the number of probabilistic method you want to use: ")
    print("1) Bigram")
    print("2) Unigram")
    input_probabilistic_method = input()
    if int(input_probabilistic_method) == 1 or int(input_probabilistic_method) == 2:
        break
    else:
        print("Invalid input")


while True:
    input_sentence = input("Enter the sentence: ")
    if input_sentence == "!q":
        print("GOOD LUCK ;))")
        break
    else:
        if input_probabilistic_method == "1":
            # Calculating the probability of the sentence by both dictionaries
            words_list = input_sentence.split()
            redundant_words = []
            i = 0
            while i < len(words_list):
                if words_list[i] == "." or words_list[i] == "," or words_list[i] == "  " or words_list[i] == ";" or \
                        words_list[i] == "\"" or words_list[i] == "\'" or words_list[i] == "*" or words_list[
                    i] == "(" or \
                        words_list[i] == ")" or words_list[i] == "--" or words_list[i] == "-" \
                        or words_list[i] == "?" or words_list[i] == "!" or words_list[i] == "&" or words_list[
                    i] == ":" or \
                        words_list[i] == "." or words_list[i] == "و":
                    redundant_words.append(words_list[i])

                i += 1
            for i in redundant_words:
                words_list.remove(i)

            if words_list[0] in positive_words_dictionary:
                p_w1 = positive_words_dictionary[words_list[0]][1]

            else:
                p_w1 = 0

            lambda1 = 0.1
            lambda2 = 0.4
            lambda3 = 0.5
            epsilon = 0.01
            multiply = 1
            i = 1
            while i < len(words_list):
                last_word = words_list[i - 1]
                pair = last_word + " " + words_list[i]
                if pair in positive_words_dictionary:
                    p_pair = positive_words_dictionary[pair][1]
                else:
                    p_pair = 0

                if words_list[i] in positive_words_dictionary:
                    p_word = positive_words_dictionary[words_list[i]][1]
                else:
                    p_word = 0

                multiply = multiply * (lambda3 * p_pair + lambda2 * p_word + lambda1 * epsilon)
                i += 1

            if p_w1 == 0:
                positive_comment_probability = multiply
            else:
                positive_comment_probability = p_w1 * multiply

            if words_list[0] in negative_words_dictionary:
                p_w1 = negative_words_dictionary[words_list[0]][1]

            else:
                p_w1 = 0

            multiply = 1
            i = 1
            while i < len(words_list):
                last_word = words_list[i - 1]
                pair = last_word + " " + words_list[i]
                if pair in negative_words_dictionary:
                    p_pair = negative_words_dictionary[pair][1]
                else:
                    p_pair = 0

                if words_list[i] in negative_words_dictionary:
                    p_word = negative_words_dictionary[words_list[i]][1]
                else:
                    p_word = 0

                multiply = multiply * (lambda3 * p_pair + lambda2 * p_word + lambda1 * epsilon)
                i += 1

            if p_w1 == 0:
                negative_comment_probability = multiply
            else:
                negative_comment_probability = p_w1 * multiply

            if positive_comment_probability > negative_comment_probability:
                print("not filter this")

            else:
                print("filter this")

        # Unigram method is implemented here
        if input_probabilistic_method == "2":
            words_list = input_sentence.split()
            redundant_words = []
            i = 0
            while i < len(words_list):
                if words_list[i] == "." or words_list[i] == "," or words_list[i] == "  " or words_list[i] == ";" or \
                        words_list[i] == "\"" or words_list[i] == "\'" or words_list[i] == "*" or words_list[
                    i] == "(" or \
                        words_list[i] == ")" or words_list[i] == "--" or words_list[i] == "-" \
                        or words_list[i] == "?" or words_list[i] == "!" or words_list[i] == "&" or words_list[
                    i] == ":" or \
                        words_list[i] == "." or words_list[i] == "و":
                    redundant_words.append(words_list[i])

                i += 1
            for i in redundant_words:
                words_list.remove(i)

            positive_comment_probability = 1
            for word in words_list:
                if word in positive_words_dictionary:
                    positive_comment_probability = positive_words_dictionary[word][1] * positive_comment_probability

            negative_comment_probability = 1
            for word in words_list:
                if word in negative_words_dictionary:
                    negative_comment_probability = negative_words_dictionary[word][1] * negative_comment_probability

            if positive_comment_probability == 1 or negative_comment_probability == 1:
                print("filter this")
                continue

            if positive_comment_probability > negative_comment_probability:
                print("not filter this")

            else:
                print("filter this")






























