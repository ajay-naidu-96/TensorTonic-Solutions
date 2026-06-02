import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    vm = {}
    for i, v in enumerate(vocab):
        vm[v] = i

    res = [0] * len(vocab)

    for i, t in enumerate(tokens):
        if t in vm.keys():
            res[vm[t]] += 1

    return np.array(res, dtype=int)