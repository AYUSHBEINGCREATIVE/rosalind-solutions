with open("rosalind_rna.txt") as f:
    s = f.read().strip()

print(s.replace('T', 'U'))