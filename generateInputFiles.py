import random

# Small (100) ascending
numbers = range(1, 101, 1)
textfile = open("smallAscending.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Medium (1000) ascending
numbers = range(1, 1001, 1)
textfile = open("mediumAscending.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Large (10000) ascending
numbers = range(1, 10001, 1)
textfile = open("largeAscending.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Small (100) descending
numbers = range(100, 0, -1)
textfile = open("smallDescending.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Medium (1000) descending
numbers = range(1000, 0, -1)
textfile = open("mediumDescending.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Large (10000) descending
numbers = range(10000, 0, -1)
textfile = open("largeDescending.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Small (100) random
numbers = random.sample(range(1, 101), 100)
textfile = open("smallRandom.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Medium (1000) random
numbers = random.sample(range(1, 1001), 1000)
textfile = open("mediumRandom.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()

# Large (10000) random
numbers = random.sample(range(1, 10001), 10000)
textfile = open("largeRandom.txt", "w")
for element in numbers:
    textfile.write(str(element))
    textfile.write("\n")
textfile.close()




