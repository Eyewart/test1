"""programs to detect the palindromes stored in a file"""

file=open("dico.txt","r")
lines=file.readlines()

def palindrome(word):
    word_list=list(word)
    word_list_reverse=word_list
    word_list_reverse.reverse()
    word_reverse="".join(word_list_reverse)

    if (word==word_reverse):
        return(True)
    else:
        return(False)

for word in lines:
    word=word.replace("\n", "")

    if(palindrome(word)):
        print(word)

