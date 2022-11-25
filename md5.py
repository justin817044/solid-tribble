import hashlib

counter = 1

pass_in = input("MD5 Hash: ")

pwfile = open("D:/dictpw/dictpw.txt", 'r', encoding = "utf-8")

for password in pwfile:
    filemd5 = hashlib.md5()
    filemd5.update(password.strip().encode("utf-8"))
    filemd5 = filemd5.hexdigest()
    print("Count Number {} : {}".format(counter, password.strip()))

    counter += 1

    if pass_in == filemd5:
        print("\nPassword Found {}".format(password))
        break
else:
    print("\nPassword NOT Found")
