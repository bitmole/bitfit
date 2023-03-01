'''
Silly interview problem:
Sum up all numeric palindromes in numbers up to 10000.
    909 is a palindrome, that reads same from the left as from the right.
'''

def ispalin(s):
    return s == reverse(s)

def reverse(s):
    return s[::-1]

def main():
    total = 0

    for n in range(0, 10000):
        if ispalin(str(n)):
            total += n

    print(total)

if __name__ == "__main__":
    main()
