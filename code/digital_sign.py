#Mark Boady 2020 - Drexel University
#Create a digital Signature for this code.
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

#Generate keys
length=1024
privatekey=RSA.generate(length,Random.new().read)
publickey=privatekey.publickey()
print("Public Key:",publickey)

#I want to sign this string
contents=b'This is the email I want to sign.'
#Make a signature
S=(privatekey.sign(contents,''))[0]
S=str(S).encode()
S=base64.b64encode(S)
print("Signature:",S)


#Someone wants to verify my signature
#We use base 64 since the signature would be sent
#Via email/slack/txt etc
#Not in the same file
res=publickey.verify(contents,(int(base64.b64decode(S)),))
print("Result:",res)