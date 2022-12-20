import re

def sequence_sub(sequence):
    # Initial pattern
    virus = r"([T][C][G][A])"
    
    # If theres a matching to the initial pattern, then substitute that match with nothing, sequence receives the resulting string then calls the function again 
    if re.search(virus, sequence) != None:
        sequence = re.sub(virus, '', sequence)
        return sequence_sub(sequence)

    # If there isn't a matching, then return the final sequence
    else:
        return sequence