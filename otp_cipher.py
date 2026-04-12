class OTPCipher:
   

    def __init__(self, keystream):
        
        self.keystream = keystream

    def _validate_length(self, data_length):
        
        if len(self.keystream) < data_length:
            raise ValueError("Keystream eshte me i shkurter se te dhenat!")

    def _xor_bytes(self, data_bytes):
        
        return bytes([
            b ^ k for b, k in zip(data_bytes, self.keystream)
        ])

    def encrypt(self, plaintext):
        
        data_bytes = plaintext.encode('utf-8')

        self._validate_length(len(data_bytes))

        cipher_bytes = self._xor_bytes(data_bytes)
        return cipher_bytes

    def decrypt(self, cipher_bytes):
        
        self._validate_length(len(cipher_bytes))

        decrypted_bytes = self._xor_bytes(cipher_bytes)
        return decrypted_bytes.decode('utf-8')


if __name__ == "__main__":
    
    keystream = [12, 45, 78, 23, 56, 89, 90, 123, 11, 22, 33, 44]

    otp = OTPCipher(keystream)

    message = "Pershendetje"

    print("Mesazhi origjinal:", message)

    encrypted = otp.encrypt(message)
    print("Encrypted:", encrypted)

    decrypted = otp.decrypt(encrypted)
    print("Decrypted:", decrypted)