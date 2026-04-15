from otp_algorithm import OTPAlgorithm

algo = OTPAlgorithm("mysecretseed")

enc = algo.encrypt("Pershendetje")
print(enc)

dec = algo.decrypt(enc)
print(dec)
