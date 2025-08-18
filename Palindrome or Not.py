
def is_palindrome(s):

    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

word = input("Enter a string: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
