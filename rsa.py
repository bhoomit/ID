from Crypto.PublicKey import RSA
import requests

def random_org_str(n):
    print(n)
    url = "https://www.random.org/strings/?num={0}&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new"
    response = requests.get(url.format((n/20) + 1))
    return ''.join(response.text.split('\n'))[:n].encode('utf-8')

bits = 2048
new_key = RSA.generate(bits, e=65537, randfunc=random_org_str)
publicKey = new_key.publickey().exportKey("PEM")
privateKey = new_key.exportKey("PEM")
print("Public Key: ", publicKey)
print("Private Key: ", privateKey)
