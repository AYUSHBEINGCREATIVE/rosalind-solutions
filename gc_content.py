
# with open("rosalind_gc.txt") as f:
#      s= f.read().split('>') #instade of strip we are using split so that we can split the sequence based on symbolll]
#      best_seq=''
#      highest_gc=0
#      for start in s:
#           line= start.split('\n')
#           name=line[0]
         
#           dna_extraction= ''.join(line[1:]) 
          
#           if not dna_extraction:
#                 continue
#           gc =(dna_extraction.count('G')+ dna_extraction.count('C'))/len(dna_extraction)*100
          
#           if gc > highest_gc:
#                highest_gc=gc
#                best_seq= name
# print(best_seq)
# print(f"{highest_gc:.6f}")

def parse_fasta():
     with open("rosalind_gc.txt") as f:
        s= f.read().split('>')
        sequences={}
        for i in s:
             line=i.split('\n')
             name=line[0]
             dna=''.join(line[1:])
             if not dna:
               continue
             sequences[name]= dna
     return sequences


def calculate_gc(dna):
     gc =(dna.count('G')+ dna.count('C'))/len(dna)*100
     return gc


sequences=parse_fasta()
bestname= ''
highest_gc=0

for name,dna in sequences.items():
    gc= calculate_gc(dna)
    if gc > highest_gc:
           highest_gc=gc
           best_seq= name
print(best_seq)
print(f"{highest_gc:6f}")

     
     


          





