def hamming_detect(data):
    # Determine the number of parity bits
    k = 0
    while 2**k < len(data) + k + 1:
        k += 1
    parity_bits = [0] * k

    # The parity bits
    for i in range(k):
        bit_pos = 2**i - 1
        bits = [data[j] for j in range(len(data)) if (j+1) & (bit_pos+1)]
        parity_bits[i] = sum(bits) % 2

    # Syndrome 
    syndrome = 0
    for i in range(k):
        bit_pos = 2**i - 1
        if parity_bits[i] != 0:
            syndrome += bit_pos+1

    if syndrome != 0:
        error_pos = syndrome - 1
        print(f"Error detected in bit {error_pos}")
    else:
        print("No errors detected.")


if __name__ == "__main__":
    data = input("Enter the data bits (0s and 1s only) : ")
    data =  list(map(int, data))

    print(data)
    hamming_detect(data)
