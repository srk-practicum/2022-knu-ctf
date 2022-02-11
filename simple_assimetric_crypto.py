# Childish RSA
e = 65537
p = 1680613444652105838344133706142211604381500993652031705380909307238347587888162431490921255465344239
q = 2143532995881162829855694296384103840144300960388531553947710050014176459461784664429637761367242287
c = 1921902980210977295270519710634709719343372281625129194637780159651252905527903923450045434239794433327822136581724693103107581315471305119544244907185643235873825200596556268483571243342863955690176

phi_n = (p-1)*(q-1)
d = pow(e, -1, phi_n)
n = p*q
encode = str(hex(pow(c, d, n)))[2:]
print(encode)
mes = bytes.fromhex(encode)
mes = mes.decode("ascii")
print(mes)
