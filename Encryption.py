from cryptography.fernet import Fernet
def encrypt(otpath):
    key = Fernet.generate_key()
    print(key)
    fernet = Fernet(key)
    with open(otpath ,'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    fv=r"C:\Users\karth\OneDrive\Desktop\Mini Project\Encrypted\encrypted.jpg"
    with open(fv, 'wb') as f:
        f.write(encrypted_data)
    return [fv,key]
#encryption()