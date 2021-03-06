#Mark Boady CS260 - Summer 2020
import hashlib
digest = hashlib.sha256()
#Read through file in binary
with open("file_checksum.py","rb") as f:
    for line in f:
        digest.update(line)
print(digest.hexdigest())