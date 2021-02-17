import subprocess
# openssl enc - des-cbc - d - in ciphertext.enc - out recieved.txt - nosalt - iv 0000000000000000 - K 16822e5f63c237d2

# Pipe the ciphertext into a page code format that the the LSB algorithm can accept
# subprocess.run(["xxd", "-p", "hexcodeCiph.enc", "ciphertext.enc", ])

subprocess.run(["openssl", "enc", "-des", "-d", "-in", "ciphertext.enc", "-out", "recievedDecoded.txt",
                "-nosalt", "-iv", "0000000000000000", "-k", "des_key8b"])

myfile = open('recievedDecoded.txt', 'r')
pt = myfile.read()

print('\nYour original secret message was: {}'.format(pt))
