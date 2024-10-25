import hashlib

def getHash(password, salt):
  return hashlib.md5((password + salt).encode()).hexdigest()

password = "???"
salt = "???"
