# function which is checking if string is palindrome

def palindrome(string):
    return string == string[::-1]

string = "kamilślimak"
answer = palindrome(string)

if answer:
    print("Yes")
else:
    print("No")

string = "krupnik"
answer = palindrome(string)

if answer:
    print("Yes")
else:
    print("No")
