from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def decrypt(text, shift):
        cipher = ""
        for letter in text:
            if letter in alphabet:
                new_text = alphabet[(alphabet.index(letter) - shift) % len(alphabet)]
                cipher += new_text
            else:
                cipher += letter
        print(f"Your decrypted message is: {cipher}")

    def encrypt(text, shift):
        cipher = ""

        for letter in text:
            if letter in alphabet:
                new_text = alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
                cipher += new_text
            else:
                cipher += letter
        print(f"Your encrypted message is: {cipher}")

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    if restart == "no":
        should_continue = False
        print("Goodbye!")


