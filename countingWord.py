input_string=input("Enter The String:")
character_count=0
word_count=1
for i in input_string:
    character_count += 1
    if(i==" "):
        word_count +=1
print("Number of Word in the String:",word_count)        
print("Number of characters in the String:",character_count)        