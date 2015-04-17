from collections import Counter


def anagrams(words):
    """
    We get a list of normalized values.  We loop over the
    normalized values and the count the number of times each of those
    values appears. Finally, we zip over the words and normalized.
    """
    normalized = [''.join(sorted(w)) for w in words]

    d = Counter(normalized)

    return [w for w, n in zip(words, normalized) if d[n] > 1]

if __name__ == '__main__':

    with open('wordsEn.txt') as f:
        w_list = f.read().split()
        anagrams(w_list)
