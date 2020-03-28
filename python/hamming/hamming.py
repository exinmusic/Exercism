def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        return sum([1 for step in zip(strand_a,strand_b) if step[0] != step[1]])
    else:
        raise ValueError("Defined for sequences of equal length.")