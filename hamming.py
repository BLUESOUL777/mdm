def take_input():
    data = list(map(int, input("Enter 7 data bits (space separated): ").split()))
    if len(data) != 7:
        raise ValueError("Please enter exactly 7 bits.")
    return data

def generate_hamming(data):
    hamming = [0] * 12

    j = 0
    for i in range(1, 12):
        if i not in [1, 2, 4, 8]:
            hamming[i] = data[j]
            j += 1

    hamming[1] = hamming[3] ^ hamming[5] ^ hamming[7] ^ hamming[9] ^ hamming[11]
    hamming[2] = hamming[3] ^ hamming[6] ^ hamming[7] ^ hamming[10] ^ hamming[11]
    hamming[4] = hamming[5] ^ hamming[6] ^ hamming[7]
    hamming[8] = hamming[9] ^ hamming[10] ^ hamming[11]

    return hamming

def error_detection_and_correction(hamming):
    pos = int(input("\nEnter position (1-11) to introduce error (0 for no error): "))

    if pos != 0:
        hamming[pos] ^= 1

    print("\nHamming Code with Error:")
    print(*reversed(hamming[1:12]))

    p1 = hamming[1] ^ hamming[3] ^ hamming[5] ^ hamming[7] ^ hamming[9] ^ hamming[11]
    p2 = hamming[2] ^ hamming[3] ^ hamming[6] ^ hamming[7] ^ hamming[10] ^ hamming[11]
    p4 = hamming[4] ^ hamming[5] ^ hamming[6] ^ hamming[7]
    p8 = hamming[8] ^ hamming[9] ^ hamming[10] ^ hamming[11]

    error_position = p1 * 1 + p2 * 2 + p4 * 4 + p8 * 8

    if error_position == 0:
        print("\nNo error detected.")
    else:
        print(f"\nError detected at position: {error_position}")
        hamming[error_position] ^= 1
        print("Error corrected!")

    return hamming

data_bits = take_input()
hamming_code = generate_hamming(data_bits)

print("\nGenerated Hamming Code:")
for i in range(11, 0, -1):
    print(hamming_code[i], end=" ")
print()

corrected_code = error_detection_and_correction(hamming_code)

print("\nCorrected Hamming Code:")
for i in range(11, 0, -1):
    print(corrected_code[i], end=" ")
print()