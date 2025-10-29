'''
A DNA strand segment typically consists of four unique bases: Adenine (A), Thymine (T), Guanine (G), and Cytosine (C). The lab wants to simulate all possible orders in which these bases could mutate over time to identify potentially harmful configurations. Each mutation model considers every possible sequence of a specific length, allowing repeated bases, and the order of bases is important.



To maintain biological safety protocols, the lab has a predefined list of harmful configurations (e.g., known oncogenic or disease-causing patterns). Your task is to simulate all possible encodings and filter out any sequences that match the harmful ones.



Write a function filter_dna_mutations(bases, length, harmful_patterns) that:

Generates all possible sequences of a given length using the input bases
Filters out sequences that match the known harmful patterns
Returns the remaining sequences, sorted in lexicographic order


Input Format

A tuple whose elements, respectively, are
bases (str): Unique uppercase letters representing base options
length (int): Target length of each sequence
harmful_patterns (list of str): Harmful DNA configurations to be excluded


Output Format

A list (list of str) of valid, non-harmful DNA sequences
The list must be sorted in lexicographic order


Constraints

1 ≤ length ≤ 4
1 ≤ len(bases) ≤ 4
All characters in bases are distinct and in uppercase
All harmful patterns are strings of the same length as the sequences
The number of valid sequences will not exceed 10,000


Example Cases



Example Case 1



Input



('AT', 2, ['AA', 'TT'])



Output



['AT', 'TA']



Example Case 2



Input



('AGC', 2, ['GC'])



Output



['AA', 'AC', 'AG', 'CA', 'CC', 'CG', 'GA', 'GG']
'''
# Solution
# Libraries (do not edit)
from ast import literal_eval
from itertools import product

def filter_dna_mutations(bases, length, harmful_patterns):
    # Your code here
    perm= list(product(bases, repeat=length))
    res=[''.join(p) for p in perm]
    return sorted(set(res) - set(harmful_patterns))
    



# Input and output processing (do not edit)
print(filter_dna_mutations(*literal_eval(input())))