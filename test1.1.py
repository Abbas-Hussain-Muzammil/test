import string
import sys

def count_words(filename):
    mydict = {}
    
    with open(filename, "r") as sentences:
        for line in sentences:
            line = line.translate(str.maketrans("", "", string.punctuation))
            words = line.split()
            for word in words:
                if word in mydict:
                    mydict[word] += 1
                else:
                    mydict[word] = 1
    
    return mydict

if __name__ == '__main__':

    #check wheather necessary commands are provided or not
    if len(sys.argv) != 2:
        print("Give a filename")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        #Opening the file

        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"An error occured: {str(e)}")

    # filename = "C:/Users/abbas/Documents/Notepad Texts/sample.txt"
    word_count = count_words(filename)
    
    for key in sorted(word_count.keys()):
        print(key, ":", word_count[key])
