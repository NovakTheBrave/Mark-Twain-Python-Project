#Nicholas Novak Sample Python Code
#Mark Twain Lab Solution

##Random library 
import random
from string import ascii_letters

file_name = "Baron_Lab6.txt" #Name of chosen downloaded file

##Open chosen file in read only mode
file_input = open(file_name,"r")
lines_of_file = file_input.readlines()
file_input.close()


from string import ascii_lowercase
from string import ascii_uppercase
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def mark_twain_function(string_input):
    final = ""
    
    for letter_line in string_input:
        if letter_line not in letters:
            return("") #Disregards all ',-_,etc.
        
    if len(string_input) <= 3:
        return(string_input) #Returns exception case where the word cannot be modified by this process
    
    else:
        rand1 = random.randint(1,len(string_input)-2)
        rand2 = random.randint(1,len(string_input)-2)
        
        while rand1 == rand2:
            rand1 = random.randint(1,len(string_input)-2)
        w = max(rand1,rand2)
        i = min(rand1,rand2)
        sep = ""
        
        if string_input[rand1] == string_input[rand2]:
            sep = "\\"
            
        return(string_input[:i:]+sep+string_input[max(rand1,rand2)]+string_input[i+1:w:]+string_input[min(rand1,rand2)]+string_input[w+1:]) #Return all combined components
    

#-----------------------------------------------------------------

#Utility to check if the function works (provided with assignment)
#Assuming distinct letters, number of words we can generate is P(n,2)/2,
#where n is the length of the string minus 2

word_list = []

for i in range(1000):
    x = mark_twain_function("hello")
    if x not in word_list:
        word_list.append(x)
        
##Both lists are sorted to compare to compare since random numbers are generated and aren't guranteed the same order
print("First test passed?:",sorted(['hlleo', 'he\\llo', 'hlelo'])==sorted(word_list))

word_list = []
for i in range(1000):
    x = mark_twain_function("help")
    if x not in word_list:
        word_list.append(x)
##In this case, the letters can only switch from el -> le
print("Second test passed?:",word_list==["hlep"])

word_list = []
for i in range(10000):
    x = mark_twain_function("abcdefghijkl")
    if x not in word_list:
        word_list.append(x)
        
#Utility checks to ensure proper function operation:
print("Third test passed?:",len(word_list)==45)

print("Fourth test passed?:",mark_twain_function("hello!")=="")

print("Fifth test passed?:", mark_twain_function("42 is the answer")=="")

#--------------------------------
#Now, the word jumbling function was built

def word_replacer(string):
    output_string = ""
    temp_word = ""
    
    ##We know we've "seen a word" when we find the first non-alpha character after finding some prior letters
    for character in string:
        #If it's not alpha, we merely need to preserve it
        if character in ascii_letters:
            temp_word+=character
        else:
            #First find the word
            #Finally reset the temp word 
            flipped_word = mark_twain_function(temp_word)
            output_string+=mark_twain_function(temp_word)+character
            temp_word = ""
    #Handle last character not being newline and we currently have a word
    output_string+=mark_twain_function(temp_word)    
    return output_string



#Process the file here
#This is where we will write our transformed text too

import os
try:
    os.remove(file_name[0:len(file_name)-4]+"_output.txt")

except:
    print("File did not exist, can't delete!")

#Open the output file ready to append to it notice the a instead of r
file_output = open(file_name[0:len(file_name)-4]+"_output.txt","a")

#Write our new "scrambled" words to the output file
for i in lines_of_file:
    #Call our word function
    result = word_replacer(i)
    #Notice the print isn't viewable by you!  That's because it's writing to the file
    print(result,file=file_output)
    
file_output.close()   


#Check to make sure the swaps actually occured
output_file = open(file_output.name,"r")

out_lines = output_file.readlines()

out_lines_first_30 = out_lines[:30:]

for i in out_lines_first_30:
    print(i)
