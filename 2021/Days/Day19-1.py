with open('../Input/Day19input.txt') as f:
    lines = f.read().split('\n')

class Scanner():
    def __init__(self):
        self.beacons = {}
        self.beacons[0] = (0, 0)
        self.beaconCount = 1
        
    def addBeacon(self, beacon):
        self.beacons[self.beaconCount] = tuple(map(int, beacon.split(',')))
        self.beaconCount += 1
        
    def getRelativePositions(self):
        self.relativity = {}
        self.relatives = set()
        for i in range(self.beaconCount):
            for j in range(i):
                x = [abs(self.beacons[i][k] - self.beacons[j][k]) for k in range(2)]
                self.relatives.add(tuple(x))
                self.relativity[(i, j)] = x
                self.relativity[(j, i)] = x
        
    def overlap(self, other):
        return True if len(self.relatives.intersection(other.relatives)) >= 12 else False
        
Scanners = []
for line in lines:
    if line[0:3] == '---':
        curentScanner = Scanner()
        Scanners.append(curentScanner)
    elif line != '':
        curentScanner.addBeacon(line)
    else:
        curentScanner.getRelativePositions()
beacons = {}
scanners = {}
for i in range(len(Scanners)):
    for j in range(i):
        print(i, j)
        print(Scanners[i].overlap(Scanners[j]))