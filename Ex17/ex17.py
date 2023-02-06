def generate_numbs():
    squares = [x**2 for x in range(6, 31)]
    return squares

rez = generate_numbs()
print("Ganerated from 1 to 30, without the first 5 elements: ", rez)