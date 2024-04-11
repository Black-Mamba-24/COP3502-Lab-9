##
# this is Parth Patel's file
def encode(password):
    if not password.isdigit() or len(password) != 8:
        raise ValueError("Password should be an 8-digit string containing only integers.")

    encoded_password = ''
    for i in range(len(password)):
        encoded_digit = str((int(password[i]) + 3) % 10)  # Shift each digit up by 3 numbers
        encoded_password += encoded_digit

    return encoded_password

def decode(encoded_password):
    # Assuming the encoded_password is a valid encoded
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)  # Decoding logic
        decoded_password += decoded_digit

    return decoded_password


if __name__ == '__main__':

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    #choice = int(input("Enter your choice: "))

    if int(input("Enter your choice: ")) == 1:
        # Handle encoding here
        password = input("Enter the 8-digit password to encode: ")
        encoded_password = encode(password)
        print(f"Encoded password: {encoded_password}")

    elif int(input("Enter your choice: ")) == 2:
        try:
            original_password = decode(encoded_password)  # Use the most recently encoded password
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        except NameError:
            print("No password has been encoded yet. Please encode a password first.")


    elif int(input("Enter your choice: ")) == 3:
        print("Exiting...")


    else:
        print("Invalid choice. Please enter a valid option.")
    while True:

        break





