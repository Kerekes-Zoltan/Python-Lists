import itertools

def generate_permutaions(elements):
    permutations = list(itertools.permutations(elements))
    return permutations

elements = [1, 2, 3, 4]
rez = generate_permutaions(elements)

print("Generated all permutaions in the list: ", rez)