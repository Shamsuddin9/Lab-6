# Name: Shamsuddin Shaikh
# encode function
def encode(password):
    encode_password = ""
    for digit in password:
        encrypted_password = str((int(digit) + 3) % 10)
        encode_password += encrypted_password
    return encode_password


# main function
def main():
    encryption = True
    # Loop
    while encryption is True:
        print("Menu")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_choice = input("Please enter an option: ")
        if menu_choice == '1':
            password = input("Please enter your password to encode: ")
            encode_password = encode(password)
            print("Your password has been encoded and stored!")
        elif menu_choice == '3':
            encryption = False
        # I can't finish the functions due to the decode not being there
        # elif menu_choice == '2':
        # print(f'The encoded password is {encode_password},
        # and the original password is {decode password function name(encode_password)} ')

        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
