import hashlib
for x in range(0, 100000000000):
    result = hashlib.md5(("bgvyzdsv" + str(x).ljust(5, "0")).encode()).hexdigest()
    if result[:6] == "000000":
        print(x)
        break
