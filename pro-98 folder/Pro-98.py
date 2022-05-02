from configparser import InterpolationSyntaxError


f = open("test.txt")
f.read()
'this is a test file. this is a simple test .\n'

f = open("test.txt")
fileLines = f.readlines()
for line in fileLines:
    print(line) 


introString = "My name is Ryan, I am 14 years old"
words = introString.split(",")
print(words)

def greet(name):
    print("hello, " + name + ". how are you?")


def countWordsFromFile():
    fileName = input("enter the file name:-  ")
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
        print("numberOfWords: ")
        