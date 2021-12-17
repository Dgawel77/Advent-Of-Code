with open('Python\\Advent-Of-Code\\2021\\Input\\Day16input.txt') as f:
    packet = f.read().strip()

bits = format(int(packet, 16), "0{}b".format(4*len(packet)))


class Packet():
    def __init__(self, length, x):
        self.length = length
        self.vals = x

    def increareLength(self, length):
        self.length += length

    def add(self, other):
        self.vals += other.vals

    def sum(self):
        self.vals = [sum(self.vals)]

    def product(self):
        product = self.vals[0]
        for x in self.vals[1:]:
            product = product * x
        self.vals = [product]

    def min(self):
        self.vals = [min(self.vals)]

    def max(self):
        self.vals = [max(self.vals)]

    def greaterThan(self):
        if self.vals[0] > self.vals[1]:
            self.vals = [1]
        else:
            self.vals = [0]

    def lessThan(self):
        if self.vals[0] < self.vals[1]:
            self.vals = [1]
        else:
            self.vals = [0]

    def equalTo(self):
        if self.vals[0] == self.vals[1]:
            self.vals = [1]
        else:
            self.vals = [0]


def parseOperator(x, packetLength):
    start = x
    mode = bits[x]
    thisPacket = Packet(packetLength, [])
    if mode == '0':
        subpacketLength = int(bits[start+1: start+16], 2)
        thisPacket.increareLength(16 + subpacketLength)
        start += 16
        actualLength = 0
        while actualLength < subpacketLength:
            returnedPacket = whatPacket(start)
            actualLength += returnedPacket.length
            start += returnedPacket.length
            thisPacket.add(returnedPacket)
        return thisPacket
    elif mode == '1':
        numSubPackets = int(bits[start+1: start+12], 2)
        thisPacket.increareLength(12)
        start += 12
        for _ in range(numSubPackets):
            returnedPacket = whatPacket(start)
            thisPacket.increareLength(returnedPacket.length)
            thisPacket.add(returnedPacket)
            start += returnedPacket.length
        return thisPacket


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
    return Packet(packetLength, [int(number, 2)])


def whatPacket(x):
    version = bits[x:x+3]
    packetID = int(bits[x+3:x+6], 2)
    packetLength = 6
    if packetID == 4:
        return parseLiteral(x+6, packetLength)
    else:
        returnedPacket = parseOperator(x+6, packetLength)
        # I tried to use a dictionary to store the functions,
        # but It did not want to work.
        if packetID == 0:
            returnedPacket.sum()
        elif packetID == 1:
            returnedPacket.product()
        elif packetID == 2:
            returnedPacket.min()
        elif packetID == 3:
            returnedPacket.max()
        elif packetID == 5:
            returnedPacket.greaterThan()
        elif packetID == 6:
            returnedPacket.lessThan()
        elif packetID == 7:
            returnedPacket.equalTo()
        return returnedPacket


print(whatPacket(0).vals[0])
