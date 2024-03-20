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
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            encode_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "3":
            encryption = False
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
