def generate_sqr_numbs():
    squares = [x**2 for x in range(1, 6)] + [x**2 for x in range(25, 30)]
    return squares

rez = generate_sqr_numbs()
print("Ganerated numbers: ", rez)