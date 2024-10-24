def match_words(words) :
    count = 0
    for word in words :
        if len(word) > 1 and word[0] == word[-1] :
            count += 1
    return count
words = ['abc', 'xyz', 'aba', '1221','ababa', 'ababaaba']
print(match_words(words))