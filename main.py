# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    # separating word into letters
    word_letters = [letter for letter in word]

    #knowing the length of word. Anagram must have same length too
    length_of_word = len(word)
    length_of_anagram = len(anagram)

    # Checking to see that they are anagrams before continuing
    if length_of_word != length_of_anagram:
        print('These 2 words are not anagrams. Try again')

    # Once they are anagram, continue    
    else:

        #starting point of while loop
        a = 0
        # Empty list to append the result of each condition
        b = []

        # loop for the length of word
        while a < length_of_word:

            # if the first letter is in the anagram, append 'True' to the list
            if word_letters[a] in anagram:
                b.append('True')
            
            #else append 'False'
            else:
                b.append('False')

            #increment till it loops 4 times    
            a += 1

        #if False in the list, it means a letter in word didn't match with anagram letters, so return False    
        if 'False' in b:
            return False

        # else they are anagrams    
        else:
            return True


