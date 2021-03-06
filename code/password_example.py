import bcrypt

#Example 1: hash as password
passwd=b'MarksPassword'#b means treat as bytes

salt=bcrypt.gensalt()
digest=bcrypt.hashpw(passwd,salt)
print("Digest 1:\n",digest)

#Example 2: Same password, different digest
passwd1=b'password123'
passwd2=b'password123'

salt1=bcrypt.gensalt()
digest1=bcrypt.hashpw(passwd1,salt1)
salt2=bcrypt.gensalt()
digest2=bcrypt.hashpw(passwd2,salt2)
print("Copy 1:\n",digest1)
print("Copy 2:\n",digest2)

#Example 3: Checking a password
passwd=b'CoolPassword'
salt=bcrypt.gensalt()
digest=bcrypt.hashpw(passwd,salt)
if bcrypt.checkpw(passwd,digest):
	print("Password Matches")
else:
	print("Password does not match.")
