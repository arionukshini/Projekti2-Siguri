from keystream import generate_keystream
from otp_cipher import OTPCipher

class OTPAlgorithm:
    def __init__(self, seed):
        self.seed = seed
        
    def encrypt(self, plaintext):
        ks = generate_keystream(len(plaintext.encode('utf-8')), self.seed)
        cipher = OTPCipher(ks)
        return cipher.encrypt(plaintext)
    
    