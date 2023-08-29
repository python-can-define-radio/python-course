# Encryption using PyScrypt

This lesson uses the Python Scrypt package: https://github.com/ricmoo/pyscrypt

This is Symmetric Encryption. Readers are encouraged to also learn about Asymmetric Encryption.

```python3
import getpass
import sys
import pyscrypt


originalFilename = "myfile.png"
encryptedFilename = "theFileToSend.scrypt"
outputFileAfterDecrypting = "theDecryptedFile.png"
print()
print(f"About to encrypt '{originalFilename}' as '{encryptedFilename}'")
password_as_str = getpass.getpass("Type password; it won't be shown at all: ")
password_as_bytes = password_as_str.encode()

with open(originalFilename, "rb") as infile:
    contents = infile.read()
print("Encrypting", originalFilename)
with pyscrypt.ScryptFile(encryptedFilename, password_as_bytes, N = 1024, r = 1, p = 1) as f:
    f.write(contents)

dec = input("Done. Would you like to decrypt the file to test that it worked? (y|n)")
if dec != "y":
    print("exiting.")
    sys.exit()

password_as_str = getpass.getpass()
password_as_bytes = password_as_str.encode()
print("Decrypting...")
with pyscrypt.ScryptFile(encryptedFilename, password_as_bytes) as f:
    decrypted = f.read()

with open(outputFileAfterDecrypting, "wb") as outfile:
    outfile.write(decrypted)
print(f"File written to '{outputFileAfterDecrypting}'")

```
