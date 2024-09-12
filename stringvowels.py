
def Check_Vow(string, vowels):

    #the term "casefold" is used to refer the method of ignoring cases.
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)
    #To count the Vowels
    for character in string:
    #checking the vowel string in if condition
        if character in count:
    #incrementing the vowel character
            count[character] += 1

    return count

#Driver Code

vowels = "aeiou"
string = "Guvi Geeks Network Private Limited"
print (Check_Vow(string, vowels))


