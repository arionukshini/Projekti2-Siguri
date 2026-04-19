from otp_algorithm import OTPAlgorithm

otpa = OTPAlgorithm("rrjetatkompjuterike")

enc = otpa.encrypt("Ky eshte implementimi i algoritmit One Time Pad ne Python.")
print("Encrypted: ", enc)

dec = otpa.decrypt(enc)
print("Decrypted: ", dec)
