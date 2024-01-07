from collections import deque

def main():
    pol_word = input("Enter word to check: ")

    d = deque(pol_word.lower().replace(" ", ""))

    while len(d) > 1:
        a = d.pop()
        b = d.popleft()
        if a != b:
            print(f"'{pol_word}' is not palindrome")
            break
    else:
        print(f"'{pol_word}' is a palindrome")
    
if __name__ == "__main__":
    main()
    
    """
    abccba
    ab ccba
    abcdcba
    ABCdcba
    ######
    ABCdcbaa
    ABCcdcba
    """