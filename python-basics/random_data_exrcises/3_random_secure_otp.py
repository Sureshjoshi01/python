# Generate 6 digit Random Secure OTP

import secrets
import random


secretsGenerator = secrets.SystemRandom()

otp = []
for i in range(5):
    random_number = secretsGenerator.randint(0,9)
    otp.append(random_number)

for i in otp: 
    print(i,end="")
