from otp_algorithm import OTPAlgorithm

otpa = OTPAlgorithm("rrjetatkompjuterike")

enc = otpa.encrypt("Ky eshte implementimi i algoritmit One Time Pad ne Python.")
print(enc)

dec = otpa.decrypt(enc)
print(dec)
