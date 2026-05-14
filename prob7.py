with open("rosalind_iprb.txt") as f:
    s = f.read().strip()
k, m, n = map(int, s.split())
total = k + m + n
p = (k/total * (k-1)/(total-1) * 1        # AA x AA
   + k/total * m/(total-1) * 1            # AA x Aa
   + m/total * k/(total-1) * 1            # Aa x AA
   + k/total * n/(total-1) * 1            # AA x aa
   + n/total * k/(total-1) * 1            # aa x AA
   + m/total * (m-1)/(total-1) * 3/4      # Aa x Aa
   + m/total * n/(total-1) * 1/2          # Aa x aa
   + n/total * m/(total-1) * 1/2          # aa x Aa
   + n/total * (n-1)/(total-1) * 0)       # aa x aa

print(round(p,5))































