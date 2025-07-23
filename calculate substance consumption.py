def split_into_triplets(sequence):
    return [sequence[i:i+3] for i in range(0, len(sequence), 3)]

# Приклад
seq = "AAAGTCCCCЕ"
triplets = split_into_triplets(seq)
print(triplets)
triplet_str = '-'.join(split_into_triplets(seq))
print(triplet_str)