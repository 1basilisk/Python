def main():
    # input
    text = input("Text: ")

    # doing all operations
    letters = countLetters(text)
    words = countWords(text)
    sent = countSent(text)
    grade(letters, words, sent)
    
# counting [a-z] and [A-Z]
def countLetters(str):
    letters = 0
    for i in range(0, len(str), 1):
    
        if str[i].isalpha():
        
            letters += 1
    print(f"letters:  {letters}")
    return letters
    
# counting spaces to xount words
def countWords(str):
    words = 0
    spaces = 0
    for i in range(0, len(str), 1):
        if str[i].isspace() == True:
            spaces += 1
    words = spaces + 1
    print(f"words:  {words}")
    return words

# .?! marks a sent.
def countSent(str):
    sent = 0
    for i in range(0, len(str), 1):
        if (str[i] == '.' or str[i] == '!' or str[i] == '?'):
            sent += 1
    print(f"sent: {sent}")
    return sent

# grading by Coleman-Liau
def grade(l, w, s):
    print
    L = (l / w) * 100
    S = (s / w) * 100
    index = (0.0588 * L) - (0.296 * S) - 15.8
    grade = round(index)
       
    if index < 1:
        print("Before Grade 1")
    
    elif index > 16:
        print("Grade 16+")
    
    else:
        print(f"Grade: {grade}")
    return index

#main function
if __name__ == "__main__":
    main()