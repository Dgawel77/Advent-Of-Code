with open("Advent2020\Day20Input.txt") as f:
    blocks = f.read().split("\n\n")

class Tile:
    def __init__(self, tileList):
        self.id = tileList[0][5:-1]
        self.top = tileList[1]
        self.bottom = tileList[-1]
        self.right = "".join(list(map(lambda x: x[0], tileList[1:])))
        self.left = "".join(list(map(lambda x: x[-1], tileList[1:])))
    
    def __str__(self):
        answer = ""
        for x in self.__dict__:
            answer += x + "\n" + self.__dict__[x] + "\n"
        return(answer)

    def get(self):
        answer = ""
        for x in self.__dict__:
            if x != "id":
                answer += self.__dict__[x]
        return(answer)

    def flipRight(self):
        temp = self.right
        self.right = self.left
        self.left = self.right

    def flipUp(self):
        temp = self.top
        self.top = self.bottom
        self.bottom = self.top

tiles = {}
for block in blocks:
    splitBlock = block.split("\n")
    tiles[splitBlock[0][5:-1]] = Tile(splitBlock)

for tile in tiles:
    print(tiles[tile])
    print(tiles[tile].get())