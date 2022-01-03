with open('../Input/Day4input.txt') as f:
    lines = f.readlines()

mark = set()


class board():
    def __init__(self, rows):
        self.rows = rows

    def isWinner(self):
        for r in self.rows:
            if set(r).issubset(mark):
                return True
        for pos in range(0, 5):
            if set([r[pos] for r in self.rows]).issubset(mark):
                return True
        return False

    def printWinner(self):
        for r in self.rows:
            if set(r).issubset(mark):
                return set(r)
        for pos in range(0, 5):
            if set([r[pos] for r in self.rows]).issubset(mark):
                return set([r[pos] for r in self.rows])

    def sumUnMarked(self):
        total = 0
        for r in self.rows:
            for n in r:
                if n not in mark:
                    total += int(n)
        return total


numbers = lines[0].split(',')

boards = []
for p in range(2, len(lines), 6):
    boards.append(board([lines[x].split() for x in range(p, p+5)]))

for draw in numbers:
    mark.add(draw)
    for b in boards:
        if b.isWinner():
            print(int(draw) * b.sumUnMarked())
            exit()
