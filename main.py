import sys



def Caesar():
    # input shift value
    n = sys.argv
    plain_txt = input("Input Text: \n")
    #for spacing 
    print("---------Processing-----------")
    print("Cipher 0utput: \n")
    #using a helper function fo calculations
    #because n is made a list by my program, I am retrieving the value of the element in index 1 because like I said the input is brought in as a list as such:
    #['main.py', '1']
    caesar = helper(plain_txt, int(n[1]))

    # Since lines are 5 x 10  we loop 50 iterations
    for start in range(0, len(caesar), 50):
        current = caesar[start : start + 50]
        for next_line_start in range(0, len(current), 5):
            new_line = caesar[start + next_line_start : start + next_line_start + 5]
            #amalgamating the strings
            print("".join(new_line), end=" ")
        #a new entry for every line
        print()


def helper(plain, n):
    # make the plain text into uppercase as instructed
    plain = plain.upper()
    # a list for storing the caesar txt
    caesar_txt = []
    for letter in plain:
        #if the letters are really letters
        if not letter.isalpha():
          #skipping
            continue
        # ord("A") = 65
        current = ord(letter) - 65
        # using modulo to keep ascii between the right values
        ci = (current + n) % 26
        #adding the correct text
        #chr() does the reverse of ord()
        caesar_txt.append(chr(ci + 65))
    return caesar_txt

if __name__ == "__main__":
    Caesar()
