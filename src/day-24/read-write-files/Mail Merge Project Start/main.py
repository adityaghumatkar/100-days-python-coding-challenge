#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt") as input_file:
    content = input_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

for name in names_list:
    stripped_name = name.strip()
    invitation_body = content.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/Invitation_to_{stripped_name}.txt", mode="w") as invitation_mail:
        invitation_mail.write(invitation_body)
