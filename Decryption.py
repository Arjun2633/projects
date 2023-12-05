from cryptography.fernet import Fernet
def decrypt(path,key):
    
    #key=b'bHYUDZ0X_htVFzapnv438PJv4zqvevH6Dg0iAE-KQHE='
    fernet = Fernet(key)
    with open(path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\Decrypted\decrypted.jpg",'wb') as f:
        f.write(decrypted_data)
#path=r"C:\Users\karth\OneDrive\Desktop\Mini Project\Encrypted\encrypted.jpg"
#decryption(path)