inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

vorigeDiepte = 0
aantalKeerDieper = 0
  
# Strips the newline character
for line in lines:
    diepte = int(line)

    if diepte > vorigeDiepte and vorigeDiepte != 0:
      aantalKeerDieper = aantalKeerDieper + 1
    vorigeDiepte = diepte
    
    #print(diepte)
    #count += 1
    #print("Line{}: {}".format(count, line.strip()))

print(aantalKeerDieper)