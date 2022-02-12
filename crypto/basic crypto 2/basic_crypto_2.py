from random import randrange

def gcd(x, y):
	return x if y == 0 else gcd(y, x % y)

def ExtendedGCD(a, b):
    if a == 0:
        return b, 0, 1
    Gcd, x1, y1 = ExtendedGCD(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return Gcd, x, y


def reversal(x, m):
    Gcd, a, b = ExtendedGCD(x, m)
    if Gcd == 1:
        return (a % m + m) % m

#generate key pair
def create_keys(key):
	n = key[0] * key[1] # modulus
	phi = (key[0] - 1) * (key[1] - 1)
	while True:
		#e = randrange(2, phi - 1)
		e = 65537 #use proposed public exponent
		if gcd(e, phi) == 1:
			d = reversal(e, phi)
			if d is None:
				continue
			else:
				return n, e, d
		else:
			continue

#int to bytes python converter
def int_to_bytes(INT):
 return INT.to_bytes((INT.bit_length() + 7) // 8, byteorder='big')

samsung_key = [1680613444652105838344133706142211604381500993652031705380909307238347587888162431490921255465344239 , 2143532995881162829855694296384103840144300960388531553947710050014176459461784664429637761367242287]

n_,e_,d_ = create_keys(samsung_key)

print(n_,e_,d_)

c_ = 1921902980210977295270519710634709719343372281625129194637780159651252905527903923450045434239794433327822136581724693103107581315471305119544244907185643235873825200596556268483571243342863955690176

print(int_to_bytes(pow(c_,d_,n_)).decode())
