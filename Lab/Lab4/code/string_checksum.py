# Mark Boady CS260 - Summer 2020
import hashlib

digest = hashlib.sha256()
digest.update(b'Hello. I am a string.')
print(digest.hexdigest())


if __name__=="__main__":
    print(b'pa'.decode())