def modulus(tocompute,modulo):
    result = 0
    for i in tocompute:
        result = (result*10 + int(i))%modulo
    return result


base = int(input("Enter base"))
exponent = int(input("Enter exponent"))
print(modulus(str(base**exponent),23))
