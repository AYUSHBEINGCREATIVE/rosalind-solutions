with open("rosalind_revc.txt") as f:
    s = f.read().strip()

complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
print(''.join(complement[base] for base in reversed(s)))