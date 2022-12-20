from sequence_sub import sequence_sub
from smallest import smallest

quantifier = int(input('Insert the amount of bacteries sequences: '))

initial_sequences = []

print('\nInsert your sequences below')

# receives sequences (quantifier) times
initial_sequences = [input(f'[{i + 1}] > '.upper()) for i in range(quantifier)]

# for each sequence calls the function passing the sequence
resulting_sequences = [sequence_sub(initial_sequences[i]) for i in range(len(initial_sequences))]

# stores the smallest sequence in resulting_sequences
smallest_sequence = smallest(resulting_sequences)

print(f'\n{smallest_sequence}')