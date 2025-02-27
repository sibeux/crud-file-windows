# generate palindrome code ai
def is_palindrome(s):
    return s == s[::-1]

def main():
    user_input = input("Enter a word or phrase: ").replace(" ", "").lower()
    if is_palindrome(user_input):
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()