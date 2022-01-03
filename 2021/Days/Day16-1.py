with open('../Input/Day16input.txt') as f:
    packet = f.read().strip()

bits = format(int(packet, 16), "0{}b".format(4*len(packet)))


def parseOperator(x, packetLength):
    start = x
    mode = bits[x]
    if mode == '0':
        subpacketLength = int(bits[start+1: start+16], 2)
        packetLength += 16 + subpacketLength
        start += 16
        actualLength = 0
        while actualLength < subpacketLength:
            returnedLength = whatPacket(start)
            actualLength += returnedLength
            start += returnedLength
        return packetLength
    elif mode == '1':
        numSubPackets = int(bits[start+1: start+12], 2)
        packetLength += 12
        start += 12
        for _ in range(numSubPackets):
            length = whatPacket(start)
            packetLength += length
            start += length
        return packetLength


def parseLiteral(x, packetLength):
    global bits
    number = ''
    start = x
    while True:
        group = bits[start: start+5]
        number += group[1:]
        start += 5
        packetLength += 5
        if group[0] == '0':
            break
    return packetLength


versionSum = 0


def whatPacket(x):
    global versionSum
    version = bits[x:x+3]
    versionSum += int(version, 2)
    packetID = bits[x+3:x+6]
    packetLength = 6
    if int(packetID, 2) == 4:
        return parseLiteral(x+6, packetLength)
    else:
        return parseOperator(x+6, packetLength)


whatPacket(0)
print(versionSum)
