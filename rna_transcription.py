def to_rna(dna_strand):
    rna_strand = ''
    for c in dna_strand:
        if c is 'G':
            rna_strand += 'C'
        elif c is 'C':
            rna_strand += 'G'
        elif c is 'T':
            rna_strand += 'A'
        elif c is 'A':
            rna_strand += 'U'
    return rna_strand
