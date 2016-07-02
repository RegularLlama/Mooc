word = raw_input()

word_rev = reversed(word)


if list(word) == list(word_rev):
    print'True, it is a palindrome'
else:
    print'False, this is''t a plindrome'

'''str(n) == str(n)[::-1]'''