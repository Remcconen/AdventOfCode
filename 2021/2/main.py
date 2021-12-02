class Command:
    def __init__(self, func, amount):
        self.func = func
        self.amount = amount

class Position1:
    def __init__(self):
        self.hpos = 0
        self.depth = 0
    
    def forward(self, amount):
        self.hpos += amount

    def down(self, amount):
        self.depth += amount

    def up(self, amount):
        self.depth -= amount

class Position2:
    def __init__(self):
        self.hpos = 0
        self.depth = 0
        self.aim = 0
    
    def forward(self, amount):
        self.hpos += amount
        self.depth += (self.aim * amount)

    def down(self, amount):
        self.aim += amount

    def up(self, amount):
        self.aim -= amount

def parse_input(path):
    f = open(path, "r")
    lines = f.readlines()
    result = []
    for line in lines:
        command = line.split(" ")
        result.append(Command(command[0], int(command[1])))
    return result

def solve(pos, commands):
    for command in commands:
        getattr(pos, command.func)(command.amount)

    return pos.hpos * pos.depth


print("Solution 1:",solve(Position1(), parse_input("2021/2/input.txt")))
print("Solution 2:",solve(Position2(), parse_input("2021/2/input.txt")))