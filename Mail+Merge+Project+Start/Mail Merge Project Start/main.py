#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Letters/starting_letter.txt","r") as starting_letter:
    letter = starting_letter.read()
    # print(letter)

with open("./Input/Names/invited_names.txt","r") as invited_names:
    name_list = invited_names.readlines()
    # print(name_list)

#Replace the [name] placeholder with the actual name.
for name in name_list:
    stripped_name = name.strip()
    personalise_letter = letter.replace("[name]",stripped_name)

#Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx","w") as new_file:
        new_file.write(personalise_letter)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp