def slices(series, length):
    seg_size = len(series)
    if length > seg_size or length <= 0:
        raise ValueError(f'Length needs to be more than 0 and less than {seg_size+1} with current series.')
    return [ series[x:x+length] for x in range((seg_size - length)+1) ]