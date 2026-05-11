with open("rosalind_hamm.txt") as f:
    lines = f.read().strip().split('\n')
    seq1 = lines[0]
    seq2 = lines[1]
count = 0
for a, b in zip(seq1, seq2):
    if a !=b:      # fill in the blank - not equal
        count += 1  # fill in the blank - add 1
print(count)
