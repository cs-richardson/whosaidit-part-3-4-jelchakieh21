import math

# get_score
# -----
# This function takes a word and a dictionary of
# word counts, and it generates a score that
# approximates the relevance of the word
# in the document from which the word counts
# were generated. The higher the score, the more
# relevant the word.
#
# In many cases, the score returned will be
# negative. Note that the "higher" of two
# negative scores is the one that is less
# negative, or the one that is closer to zero.

def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
#shake_dict and aust_dict is defining the dictionaries and starting them out
#as empty dictionaries.

shake_dict = {}
aust_dict = {}

#This takes the input text from the user:

user_input = input("Please enter your text: ")

#This block of code defines the function "predict" with three parameters. This loops through
#the texts and normalizes them. It then takes the score of each text and outputs the one with the
#higher score.

def predict(user_input, shakespeare_counts, austen_counts):
    shakespeare_score = 0
    austen_score = 0
    line_lst = user_input.split(" ")
    for word in line_lst:
        lowerWord = word.lower()
        normalWord = normalize(lowerWord)
        shakespeare_score = shakespeare_score + get_score(normalWord, shakespeare_counts)
        austen_score = austen_score + get_score(normalWord, austen_counts)
    if shakespeare_score > austen_score:
        return ("I think that was written by Shakespeare.")
    else:
        return ("I think that was written by Jane Austen.")

#This function takes the total word count of the text and puts them into a dictionary.

def get_counts(filename, result_dict):

    count = 0
    
    file_obj = open(filename, "r")

    for line in file_obj:
        line_lst = line.split(" ")
        for word in line_lst:
            lowerWord = word.lower()
            normalWord = normalize(lowerWord)
            if normalWord in result_dict:
                result_dict[normalWord] += 1
                count = count + 1
            else:
                result_dict[normalWord] = 1
                count = count + 1

        result_dict["_total"] = count
    return result_dict


# Get the counts for the two shortened versions
# of the texts

shakespeare_counts = get_counts("hamlet.txt", shake_dict)
austen_counts = get_counts("pride-and-prejudice.txt", aust_dict)


print (predict(user_input, shakespeare_counts, austen_counts))


