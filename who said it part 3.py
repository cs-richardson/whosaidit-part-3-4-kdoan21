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
    wordTotal = ""
    file = open(filename, "r")

    for i in file:
        i = i.split()
        for j in i:
            j = normalize(j)
            if j != "":
                result_dict[word]
                result_dict.append(j)
    close(filename)        
    return(result_dict)

def predict(userInput, shakespeare_counts, austen_counts):
    shakespeare_score: ""
    austen_score: ""
    userInput = userInput.split()
    for i in userInput:
        i = normalize(i)
        if i != "":
            shakespeare_score = shakespeare_score + get_score(shakespeare_counts)
            austen_score = austen_score + get_score(austen_counts)
# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride_and_prejudice.txt")

userInput = input("Input your text: ")

# Check the contents of the dictionaries
for key in shakespeare_counts:
    print(key + ": " + str(shakespeare_counts[key]))

if austen_score >= shakespeare_score:
    print("I think that was written by Jane Austen")
elif shakespeare_score >= austen_score:
    print("I think that was written by Shakespeare")

print("-----")

for key in austen_counts:
