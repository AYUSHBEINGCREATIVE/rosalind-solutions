with open("rosalind_dna.txt") as f:
    s = f.read().strip()

print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))