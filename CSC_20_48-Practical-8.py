def transposition(key, message):
    table = [[] for _ in range(key)]
    for i, c in enumerate(message):
        table[i % key].append(c)
    return ''.join([''.join(row) for row in table])

if __name__ == '__main__':
    message = input("Enter the text message : ")
    key = int(input("Enter the key : "))
    print(transposition(key, message))
