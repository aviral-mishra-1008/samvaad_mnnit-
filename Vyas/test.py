def generate_ngrams(text, n=2):
    """
    Generates n-grams (subsequences of words) from the input text.
    Args:
        text (str): The input text.
        n (int): The size of n-grams (default is 2 for bigrams).
    Returns:
        list: A list of n-grams.
    """
    words = text.split()
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = " ".join(words[i:i + n])
        ngrams.append(ngram)
    return ngrams

def compute_ngram_overlap(text1, text2, n=2):
    """
    Computes the N-gram overlap between two texts.
    Args:
        text1 (str): The first input text.
        text2 (str): The second input text.
        n (int): The size of n-grams (default is 2 for bigrams).
    Returns:
        float: The Jaccard similarity score based on N-gram overlap.
    """
    ngrams1 = set(generate_ngrams(text1, n))
    ngrams2 = set(generate_ngrams(text2, n))
    intersection = len(ngrams1 & ngrams2)
    union = len(ngrams1 | ngrams2)
    similarity = intersection / union if union > 0 else 0.0
    return similarity

# Example usage:
article1 = "Django is a powerful web framework."
article2 = "Django is a nice and powerful framework"
article1 = article1.lower().replace(" ","")
article2 = article2.lower().replace(" ","")
similarity_score = compute_ngram_overlap(article1, article2)
print(f"N-gram overlap similarity: {similarity_score:.2f}")
