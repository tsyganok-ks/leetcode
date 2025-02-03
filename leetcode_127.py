from collections import deque


def ladderLength(beginWord, endWord, wordList):
    """
    Return the number of words in the shortest transformation
    sequence from beginWord to endWord, or 0
    :param beginWord: start word
    :param endWord: end word
    :param wordList: all possible words between start and end
    :return: count of transformation
    """
    if endWord not in wordList:
        return 0

    wordList = set(wordList)

    values = set(''.join(wordList))

    queue = deque()
    queue.append((beginWord, 1))

    while queue:
        curr_word, count = queue.popleft()
        if curr_word == endWord:
            return count

        for i, ch in enumerate(curr_word):
            for val in values:
                if ch != val:
                    new_word = curr_word[:i] + val + curr_word[i+1:]
                    if new_word in wordList:
                        queue.append((new_word, count + 1))
                        wordList.remove(new_word)

    return 0


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladderLength(beginWord, endWord, wordList))


if __name__ == '__main__':
    main()