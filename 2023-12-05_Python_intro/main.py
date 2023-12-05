from base64 import b64encode, b64decode
from hashlib import sha512


b64encode(b'hello')
# b'aGVsbG8='

b64decode(b'aGVsbG8=')
# b'hello'

sha512(b'hello').hexdigest()
# '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043'


sha512(b'hello@facebook.com').hexdigest()

# rainbow tables
# solenie haseł
# komputery kwantowe

# passkey
