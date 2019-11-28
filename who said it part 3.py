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

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    result_dict = {}
    wordTotal = 0
    file = open(filename, "r")

    for i in file:
        i = i.split()
        for j in i:
            j = normalize(j)
            if j != "":
                if j in result_dict:
                    result_dict[j] = result_dict[j] + 1
                    wordTotal = wordTotal + 1
                else:
                    result_dict[j] = 1
                    wordTotal = wordTotal + 1
        result_dict["_total"] = wordTotal
    file.close()       
    return(result_dict)

def predict(userInput, shakespeare_counts, austen_counts):
    shakespeare_score = 0
    austen_score = 0
    userInput = userInput.split()
    for i in userInput:
        i = normalize(i)
        if i != "":
            shakespeare_score = shakespeare_score + get_score(i,shakespeare_counts)
            austen_score = austen_score + get_score(i,austen_counts)
    if austen_score > shakespeare_score:
        return("I think that was written by Jane Austen")
    elif shakespeare_score > austen_score:
        return("I think that was written by Shakespeare")

# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride-and-prejudice.txt")
austen_score = 0
shakespeare_score = 0

userInput = input("Input your text: ")
print(predict(userInput, shakespeare_counts, austen_counts))

# Check the contents of the dictionaries

print("-----")

