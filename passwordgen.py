import random
import string
def generate_password(length):
    if length < 1:
        return "Error! Password length must be at least 1."
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all_characters = lower + upper + digits + punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password
def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()
