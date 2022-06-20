alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def get_data():
    msg = input("Enter your message :")
    msg = msg.lower()
    num = int(input("Enter number to shift alphabets by[1-26] : "))
    if num > 26 or num == 0:
        while num > 26 or num == 0:
            num = int(input("Out of range, please enter a number (1-26): "))
    data = (msg,num)
    return(data)
    
def make_code(msg,num):
    new_word = " "
    for x in msg:
        y = alphabet.index(x)
        y = y + num
        if y > 26: 
            y = y - 27
        char = alphabet[y]
        new_word = new_word + char
    print(new_word)
    print()

def decode(msg,num):
    new_word = " "
    for x in msg:
        y = alphabet.index(x)
        y = y - num
        if y < 0: 
            y = y + 27
        char = alphabet[y]
        new_word = new_word + char
    print(new_word)
    print()

def main():
    again = True
    while again == True:
        print("1) Make a code ")
        print("2) Decode a message ")
        print("3) quit")
        print()
        selection = int(input("Enter your Selection : "))
        if selection == 1: 
            (msg,num) = get_data()
            make_code(msg,num)
        elif selection == 2: 
            (msg,num) == get_data()
            decode(msg,num)
        elif selection == 3:
            again = False
        else: 
            print("Incorrect Selection")

main()            
