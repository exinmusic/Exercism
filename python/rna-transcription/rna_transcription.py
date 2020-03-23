def to_rna(dna_strand):
    compliment = {'G':'C','C':'G','T':'A','A':'U'}
    return ''.join([ compliment[nucleotide] for nucleotide in dna_strand ])