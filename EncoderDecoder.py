                  #******* FUNCTIONS ********#    
def coding(message,key,group):                  # This function is to Encode / Decode the message
    output=[]
    for i in message:
        if i.islower():
            index=ALPHABET.index(i)             # getting the index of the current letter
            if group=="encoding":
                new_index=index+key
                if new_index>25:
                    new_index-=26               # to keep the index in range
            elif group=="decoding":
                new_index=index-key
            output.append(ALPHABET[new_index])  # appending the new letter to the list
        else:
            output.append(i)
    return output

def display(output,text):                       # This function is to Display the final Output
    print("    ",text, "message . . . .\n")
    print("     >>> Result : ",end="")
    for i in output :
        print(i,end="")     
    print("\n\n")
    

def code(user_input):                           # This function is to get Valid Input from the user
    done_coding=False
    while done_coding==False:
        if user_input =="e": 
            group="encoding"
        if user_input =="d":
            group="decoding"
        message = input("     Enter a message : ")
        try:                                    # checking if the key is a numeric value
            key= int(input("     Enter the shift value : ")) 
        except:
            print("     Invalid input( Enter a number between 1-25 )\n")
            continue
        while key>0 and key<26:                 # checking if it is in the range
            new_message=coding(message,key,group) # Calling the function to Encode / Decode
            done_coding=True
            break
            
        else:
            print("     Invalid Key... (out of range)\n")
            continue
        display(new_message,group)              # Calling the function to display the result
    
                  #*******THE BEGINNING ********#
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
status=True
print("..............WELCOME................")
while status:
    new_message=[]
    print("• ‘e’ to encode a string \n• ‘d’ to decode a string \n• ‘p’ to find the encoded text with a plain-text \n• ‘q’ to quit ")
    print("choose ur option ...")
    user_input = input()

#---ENCODING-------------------------------------------------------------
    if user_input == "e" :
        print("``````ENCODE YOUR TEXT HERE``````\n")
        code(user_input)                                    #Calling the main function

#---DECODING-------------------------------------------------------------
    elif user_input == "d" :
        print("``````DECODE YOUR TEXT HERE``````\n")
        code(user_input)                                    #Calling the main function
           
        
#---FIND USING PLAIN TEXT-------------------------------------------------
    elif user_input == "p":
        print("``````FIND THE ENCODED TEXT HERE``````\n")
        code1= input("     Enter the encoded message ")
        text=input("     Enter the plain text ")
        turn=0
        while True:
            if text in code1:                               # To check whether plain text is found
                print("\n     >>> Number of Rotation : ",turn,"\n")
                new_message=coding(code1,turn,"decoding")   # Calling the function to decode it by the rotation
                display(new_message,"decoding")             # Calling the function to display the decoded msg         
                break
            else:
                text=coding(text,1,"encoding")              # Else encode the plain text by 1
                text=''.join(text)                          # Conveting list to a string
                turn+=1                                     # Increasing no of Rotation by 1
            if turn>25 :                                    # Coming to a conclusion if the plain text is in the code
                print("\n     Plain text NOT FOUND\n")      # Checking with the possible maximum no of rotations
                break
                
#---EXIT-------------------------------------------------------------
    elif user_input == "q" :                                # Option q = End the program
        print(">>> You chose 'Quit'\n Thank You..")
        status=False

#---INCORRECT LETTER---------------------------------------------------
    else:                                                   #Invalid option = will continue and ask for a valid input
        print("\nXx Error.. type the correct letter.. xX\n")
        continue
            
