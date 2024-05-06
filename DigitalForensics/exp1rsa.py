import math


class RSA:

    def __init__(self):
        self.e = 257

    def key_pair_generate(self, p, q):
        self.n = p * q
        fi_n = (p - 1) * (q - 1)

        self.d = RSA.ex_gcd(self.e, fi_n)[0]
        while self.d < 0:
            self.d = (self.d + fi_n) % fi_n
        
        return [[self.n, self.e], [self.n, self.d]]

    def encrypt(self, data):
        plaintext = list(data)
        ciphertext = []
        for item in plaintext:
            ciphertext.append(RSA.fast_exp_mod(ord(item), self.e, self.n))
        return ciphertext

    def decrypt(self, key, cipher_text):
        n, e = key
        plaintext = list(cipher_text)
        ciphertext = []
        for item in plaintext:
            ciphertext.append(chr(RSA.fast_exp_mod(item, self.d, self.n)))
        return ciphertext

    # 尝试破解
    def crack(self):
        for i in range(2, int(math.sqrt(self.n))):
            if self.n % i == 0 and RSA.is_prime(i):
                return i, self.n//i
            
    @staticmethod
    def ex_gcd(a, b):
        if not RSA.is_integer(a):
            return False

        if not RSA.is_integer(b):
            return False


        if b == 0:
            return 1, 0
        else:
            q = a // b
            r = a % b
            s, t = RSA.ex_gcd(b, r)
            s, t = t, s - q*t
        return [s, t]
    
    @staticmethod
    def fast_exp_mod(a, e, n):
        if not RSA.is_integer(a):
            return False

        if not RSA.is_integer(e):
            return False

        if not RSA.is_integer(n):
            return False

        d = 1
        while e != 0:
            if e & 1 == 1:
                d = (d * a) % n
            e >>= 1
            a = a * a % n
        return d
    
    @staticmethod
    def is_prime(integer):
        if not RSA.is_integer(integer):
            return False

        sqrt = math.sqrt(integer)

        if integer < 2:
            return False
        elif integer == 2 or integer == 3:
            return True
        elif integer % 2 == 0:
            return False

        for i in range(3, int(sqrt)+1, 2):
            if integer % i == 0:
                return False

        return True
    
    @staticmethod
    def is_integer(number):
        if type(number) != type(1):
            print("pleas input a integer")
            return False
        else:
            return True


if __name__ == '__main__':
    msg = "ATTACK"
    rsa_obj = RSA()
    private_key, public_key = rsa_obj.key_pair_generate(13, 17)
    encrypted_message = rsa_obj.encrypt(msg)
    print(encrypted_message)
    print(rsa_obj.decrypt(private_key, encrypted_message))
    print(rsa_obj.crack())