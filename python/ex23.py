# import sys module 
import sys 

# sys. argv is a list in Python that contains all the command-line arguments passed to the script
script, input_encoding, error = sys.argv

# function main with three arguments "language_file, encoding , errors"
def main(language_file, encoding, errors):
    #The readline() method returns one line from the file
    # in this case using the language_file argument
    line = language_file.readline()

    # if statement  if line exists 
    if line:
        #Pass the arguments "line" , "encoding" and "errors" to the "print_line" function 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# function "print_line" with three arguments "line, encoding, errors"
def print_line(line, encoding, errors):
    # next_lang performs the .strip() method
    # The strip() method removes any leading, and trailing whitespaces
    next_lang = line.strip()
    # a local variable called "raw_bytes" 
    # The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
    # option for errors as well 
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # This method is used to convert from one encoding scheme, in which the argument string is encoded to the desired encoding scheme.
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    # print the results of the two variables for a single line from the text file 
    print(raw_bytes, "<===>", cooked_string)

# variable languages opens the "langauge.txt" file and has encoding="utf-8" ??
languages = open("languages.txt", encoding="utf-8")


# the code operation starts when this function is ran 
main(languages, input_encoding, error)

