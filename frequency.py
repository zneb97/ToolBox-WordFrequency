""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import operator


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()

    start_line = 0
    while lines[start_line].find('START OF THIS') == -1:
        start_line += 1

    end_line = 0
    while lines[end_line].find('THE END') == -1:
        end_line += 1

    lines = lines[start_line+1:end_line-1]

    words = []
    for line in lines:
        line = line.lower()
        line = line.translate(line.maketrans("","", string.punctuation))
        line = line.strip()
        linebreak = line.split()
        for word in linebreak:
            words.append(word)
    return words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    topWords = []
    wordDict = {}
    for word in word_list:
        wordDict.update({word:word_list.count(word)})
    wordFreq = wordDict.items()
    wordFreq = sorted(wordFreq, key=lambda x: x[1], reverse = True)

    for i in range(0,n):
        topWords.append(wordFreq[i])
    return topWords

if __name__ == "__main__":
    words = get_word_list('alice.txt')
    topWords = (get_top_n_words(words,100))
    for i in range(0,len(topWords)):
        print(topWords[i])
