# for each line, remove the \n at the end, and split it by spaces
with open("data/00-trailer.txt", "r") as file:
    list1 = [line.rstrip('\n').split(' ') for line in file.readlines()]

# convert everything to int
list1 = [[int(column) if column.isdigit() else column for column in row] for row in list1]

columns, rows, goldenPointsCount, silverPointsCount, tileTypes = list1[0]

def listToDict(list2,keys):
    return [dict(zip(keys, row)) for row in list2]

goldenPoints = list1[1:goldenPointsCount+1]
goldenPoints = listToDict(goldenPoints,["x","y"])

silverPoints = list1[goldenPointsCount+1:goldenPointsCount+1+silverPointsCount]
silverPoints = listToDict(silverPoints,["x","y","score"])

tiles = list1[goldenPointsCount+1+silverPointsCount:goldenPointsCount+1+silverPointsCount+tileTypes]
tiles = listToDict(tiles,["id","cost","types"])

tileToDirection = {
    "3":{"w","e"},
    "5":{"s","e"},
    "6":{"s","w"},
    "7":{"s","e","w"},
    "9":{"n","e"},
    "A":{"w","n"},
    "B":{"w","n","e"},
    "C":{"n","s"},
    "D":{"n","s","e"},
    "E":{"n","s","w"},
    "F":{"n","s","w","e"}
}

for tile in tiles:
    tile["direction"]=tileToDirection[str(tile["id"])]