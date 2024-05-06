from faker import Faker

with open ("./exp7/passwords/passwords.txt", "w") as f:
    fakr = Faker()
    for _ in range(10):
        f.write(fakr.password())
        f.write("\n")