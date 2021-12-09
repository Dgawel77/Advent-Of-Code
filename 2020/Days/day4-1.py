import re
with open("Day4Input.txt", "r") as f:
    lines = re.split(r'[\s\n]', f.read())
count, total = 0, 0
for line in lines:
    if line == "":
        if total == 7:
            count += 1
        total = 0
    if line != "":
        tag = line[0:3]
        rest = line[4:]
        if tag == "byr":
            if int(rest) >= 1920 and int(rest) <= 2002:
                total += 1
        elif tag == "iyr":
            if int(rest) >= 2010 and int(rest) <= 2020:
                total += 1
        elif tag == "eyr":
            if int(rest) >= 2020 and int(rest) <= 2030:
                total += 1
        elif tag == "hgt":
            if rest[-2:] == "cm":
                if int(rest[:-2]) >= 150 and int(rest[:-2]) <= 193:
                    total += 1
            elif rest[-2:] == "in":
                if int(rest[:-2]) >= 59 and int(rest[:-2]) <= 76:
                    total += 1
        elif tag == "hcl":
            if rest[1:].isalnum() and rest[0] == "#":
                total += 1
        elif tag == "ecl":
            colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            for color in colors:
                if rest == color:
                    total += 1
                    break
        elif tag == "pid":
            if len(rest) == 9:
                total += 1
print(count)
