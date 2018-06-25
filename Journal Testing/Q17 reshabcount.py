def main():
    filename = "hello.txt"
    file = open(filename, "a+")
    print ("This program calculates the number of words in a sentence")
    print
    p= raw_input("Enter a sentence: ")
    words = str.split(p)
    count = len(words)
    print (("The total word count is:"),count)
main()
