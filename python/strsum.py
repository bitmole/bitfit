'''
Silly interview problem:
Sum up a string:
    Consonants evaluate to their positive ASCII code
    Vowels evaluate to their negative ASCII code
    Ignore spaces, numbers, special chars
'''

VOWELS = 'aeiou'

def is_vowel(c):
    return c.isalpha() and c in VOWELS

def is_consonant(c):
    return c.isalpha() and not is_vowel(c)

def score(c):
    if is_vowel(c):
        return -ord(c)
    elif is_consonant(c):
        return ord(c)
    else:
        return 0

def main():
    scores = [score(c) for c in 'why and how']
    print(scores)
    print(sum(scores))


if __name__ == "__main__":
    main()
