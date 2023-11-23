#this code will be ran in the terminal 

# this functions takes an argument "stuff" in the "break_words" function
def break_words(stuff):
    # print out the string "This function will break up words for us"
    """This function will break up words for us."""
    # run the method split()
    # The split() method splits a string into a list/ array in this case after every space .
    words = stuff.split(' ')
    # return the list of words 
    return words 

# function with name "sort_words" pass the argument words 
def sort_words(words):
    # string pirnt sorts the words not printed 
    """Sorts the words."""
    # return the sorted(words) function 
    # The sorted() function returns a sorted list of the specified iterable object.
    # this is descending or ascending in our case ascending order 
    return sorted(words)

# function with name "print_first_word" pass the argument words
def print_first_word(word):
    """Prints the first word after popping it off."""
    # Pass the arguments words with the method .pop()
    # The pop() method removes the element at the specified position.
    # in our case the first letter 
    word= word.pop(0)
    # print the result 
    print(word)

# function with name "print_last_word" pass the argument words 
def print_last_word(word):
    """Prints the last word after popping it off."""
    # used the pop method on the word argument 
    # in our case grab the last letter
    word = word.pop(-1)
    # print the word when you run the function 
    print(word)

# function with name "sort_sentence" use the argument "sentence"
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # use the break_words function on sentence 
    words = break_words(sentence)
    # sort the list of broken words 
    return sort_words(words)

# function with name "print_first_and_last" with argument sentence
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # breaks the words
    words=break_words(sentence)
    
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
