def proteins(strand):
    protein = {
        'AUG' : 'Methionine',
        'UUU' : 'Phenylalanine','UUC' : 'Phenylalanine',
        'UUA' : 'Leucine','UUG' : 'Leucine',
        'UCU' : 'Serine','UCC' : 'Serine','UCA' : 'Serine','UCG' : 'Serine',
        'UAU' : 'Tyrosine','UAC' : 'Tyrosine',
        'UGU' : 'Cysteine','UGC' : 'Cysteine',
        'UGG' : 'Tryptophan',
        'UAA' : 'STOP','UAG' : 'STOP','UGA' : 'STOP'
    }
    codons = [ strand[i:i+3] for i in range(0,len(strand),3) ]
    polypeptide = [] 
    for codon in codons:
        if protein[codon] != 'STOP':
            polypeptide.append(protein[codon])
        else:
            break
    return polypeptide