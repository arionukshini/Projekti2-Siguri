from otp_algorithm import OTPAlgorithm

otpa = OTPAlgorithm("rrjetatkompjuterike")

enc = otpa.encrypt("Pershendetje")
print(enc)

dec = otpa.decrypt(enc)
print(dec)
