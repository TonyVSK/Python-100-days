def encode(message, number, alphabet):
    newmessage = []
    for letter in message:
        for i in range(0, len(alphabet)):
            if alphabet[i] == letter:
                newmessage.append(alphabet[i+number])
    newmessage = ''.join(newmessage)
    print(f'The encode message is {newmessage}')


def decode(message, number, alphabet):
    newmessage = []
    for letter in message:
        for i in range(0, len(alphabet)):
            if alphabet[i] == letter:
                newmessage.append(alphabet[i-number])
    newmessage = ''.join(newmessage)
    print(f'The decode message is {newmessage}')

print("""
▄█▄    ██   ▄███▄     ▄▄▄▄▄   ██   █▄▄▄▄     
█▀ ▀▄  █ █  █▀   ▀   █     ▀▄ █ █  █  ▄▀     
█   ▀  █▄▄█ ██▄▄   ▄  ▀▀▀▀▄   █▄▄█ █▀▀▌      
█▄  ▄▀ █  █ █▄   ▄▀ ▀▄▄▄▄▀    █  █ █  █      
▀███▀     █ ▀███▀                █   █       
         █                      █   ▀        
        ▀                      ▀             
▄█▄    ▄█ █ ▄▄   ▄  █ ▄███▄   █▄▄▄▄          
█▀ ▀▄  ██ █   █ █   █ █▀   ▀  █  ▄▀          
█   ▀  ██ █▀▀▀  ██▀▀█ ██▄▄    █▀▀▌           
█▄  ▄▀ ▐█ █     █   █ █▄   ▄▀ █  █           
▀███▀   ▐  █       █  ▀███▀     █            
            ▀     ▀            ▀                                                                                       
""")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = 'yes'
while answer == 'yes':
    decision = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input('Type your message:\n').lower()
    number = int(input('Type the shift number:\n'))


    if decision == 'encode':
        encode(message, number, alphabet)
    else:
        decode(message, number, alphabet)
    answer = input("Type 'yes' if you want again. Otherwise type 'no':\n").lower()
if answer == 'no':
    print('End of program')