alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt():
        maxShift = len(alphabet)
        textArray = list(text)
        newMessageArray = []
        for letter in textArray:
            index = alphabet.index(letter)
            newIndex = index + shift
            if newIndex > maxShift:
                newIndex = newIndex - maxShift
            newLetter = alphabet[newIndex]
            newMessageArray.append(newLetter)
        newMessage = ''.join(newMessageArray)
        print(f"The encoded text is {newMessage}")

def decrypt(shift):
   maxShift = len(alphabet)
   textArray = list(text)
   decrypMessageArray = []
   for char in textArray:
       index = alphabet.index(char)
       newIndex = index - shift
       if newIndex < 0:
           newIndex = newIndex + maxShift
       newLetter = alphabet[newIndex]
       decrypMessageArray.append(newLetter)
   newMessage = ''.join(decrypMessageArray)
   print(f"The decoded text is {newMessage}")

if (direction == 'encode'):
    encrypt()
elif (direction == 'decode'):
    decrypt(shift)
else:
    print("Invalid input")
print("type 'yes' if you want to continue, type 'no' if you want to exit")
answer = input()
while answer == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if (direction == 'encode'):
        encrypt()
    elif (direction == 'decode'):
        decrypt(shift)
    else:
        print("Invalid input")
    print("type 'yes' if you want to continue, type 'no' if you want to exit")
    answer = input()


