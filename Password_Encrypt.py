from hashlib import sha256

password = input("Please enter your password:")
hashed_password = sha256(password.encode('utf-8')).hexdigest()
print("Your Encryted Password:", hashed_password)