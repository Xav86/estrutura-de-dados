#palavra palíndroma "o galo ama o lago"

def palindromo(palavra):

    if (len(palavra)) <= 1:
        return True

    if (palavra[0] != palavra[-1]):
        return False

    return palindromo(palavra[1:-1])


palavra1 = palindromo("radar")
print(palavra1)

palavra2 = palindromo("python")
print(palavra2)

palavra3 = palindromo("ogaloamaolago")
print(palavra3)