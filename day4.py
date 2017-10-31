from hashlib import md5



count = 1
while True:
    secret_key = 'ckczppom'
    secret_key += str(count)
    hashed = md5(secret_key.encode('utf-8')).hexdigest()
    count += 1
    if hashed.startswith('00000'):
        break
print(secret_key) #117946


