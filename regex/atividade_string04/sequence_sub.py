import re

def sequence_sub(sequence: str) -> list:
    # initial pattern
    virus = r"([T][C][G][A])"
    
    # if theres a matching to the initial pattern, then substitute that match with nothing, sequence receives the resulting string then calls the function again 
    if re.search(virus, sequence) is not None:
        sequence = re.sub(virus, '', sequence)
        return sequence_sub(sequence)

    # if there isn't a matching, then return the final sequence
    else:
        return sequence