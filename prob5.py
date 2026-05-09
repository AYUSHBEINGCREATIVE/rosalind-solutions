with open("rosalind_gc.txt") as f:
    data = f.read().strip().split('>')

best_id = ''
best_gc = 0.0

for entry in data:
    if not entry.strip():
        continue
    lines = entry.strip().split('\n')
    seq_id = lines[0]
    seq = ''.join(lines[1:])
    gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
    if gc > best_gc:
        best_gc = gc
        best_id = seq_id

print(best_id)
print(f"{best_gc:.6f}")