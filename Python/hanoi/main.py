counter = 0
n = 12

def tower(n, i, j):
    global counter
    if n == 1:
        counter += 1
        print("Move a disk from stick " + str(i) + " to " + str(j) + " this is move number " + str(counter))
    else:
        tower(n-1, i, 6-i-j)
        tower(1, i, j)
        tower(n-1, 6-i-j, j)

print("Tower of Hanoi with " + str(n) + " discs from stick 1 to stick 3")
tower(n, 1, 3)
print("Finished after " + str(counter) + " moves")