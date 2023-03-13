def hamming_decode(encoded):
    # Determine the number of parity bits
    k = 0
    while 2**k < len(encoded) + k + 1:
        k += 1

    syndrome = 0
    error = 0

    for i in range(k):
        bit_pos = 2**i - 1
        bits = [encoded[j] for j in range(len(encoded)) if (j+1) & (bit_pos+1)]
        if sum(bits) % 2 != 0:
            syndrome += bit_pos+1

    if syndrome != 0:
        error = syndrome - 1
        encoded[error] = 1 - encoded[error]

    return [encoded[i] for i in range(len(encoded)) if i+1 not in [2**j for j in range(k)]]    


if __name__ == "__main__":
    encoded = input("Enter the encoded data ( 0s and 1s only ) : ")
    encoded = list(map(int,encoded))

    # Decode the data
    decoded = hamming_decode(encoded)
    print("Decoded data:", decoded)