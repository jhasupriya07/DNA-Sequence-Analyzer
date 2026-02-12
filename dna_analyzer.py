def analyze_dna(sequence):
    sequence = sequence.upper()
    valid_nucleotides = {'A','T','G','C'}
    if not set(sequence).issubset(valid_nucleotides):
       return "Invalid DNA sequence ! only A,T,G,C allowed."
    
    length = len(sequence)
    
    count_A = sequence.count('A')
    count_T = sequence.count('T')
    count_G = sequence.count('G')
    count_C = sequence.count('C')

    gc_content = ((count_G + count_C)/length)*100
    rna_sequence = sequence.replace ('T', 'U')
    
    result = f"""
DNA Length: {length}
Nucleotide Count:
A: {count_A}
T: {count_T}
G: {count_G}
C: {count_C}

GC Content: {gc_content: .2f}%

RNA sequence:
{rna_sequence}
"""
    return result

def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return "". join(complement[base] for base in reversed(sequence))
dna_input = input("Enter DNA sequence: ")
print(analyze_dna(dna_input))
print("Reverse Complement:", reverse_complement(dna_input))
