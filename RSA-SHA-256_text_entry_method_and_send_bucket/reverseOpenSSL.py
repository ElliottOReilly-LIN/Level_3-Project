import subprocess


# 5. - --- If user B has the ciphetext.bin and the signiture.bin from user A, he can now decrypt
# ---- using is own private Key
# openssl pkeyutl - decrypt - in ciphertext.bin - inkey privkeyB.pem - out recieved - msg.txt

# 6. - --- User B can now verify the file is genuine, and from user A be verification
# openssl dgst - verify pubkeyA.pem - signature signiture.bin recieved - msg.txt


def reverseDecrypt():
    # 5. - --- If user B has the ciphetext.bin and the signiture.bin from user A, he can now decrypt
    # ---- using is own private Key
    # openssl pkeyutl -decrypt -in RSAciphertext.bin -inkey privkeyA.pem -out RSAhiddenot.txt
    subprocess.run(["openssl", "pkeyutl", "-decrypt", "-in", "RSAciphertext.bin", "-inkey", "privkeyA.pem",
                    "-out", "RSAhiddenOutVerify.txt", ])

    myfile = open('RSAhiddenOutVerify.txt', 'r')
    pt = myfile.read()

    print('\nYour original secret message was: {}'.format(pt))
