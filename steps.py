import hashlib


def convert_to_utf(number):
    # Step 1: Convert the input number to binary
    binary_str = bin(number)[2:]

    # Step 2: Break the binary string into groups of size 'jump'
    binary_groups = [binary_str[i:i + 7] for i in range(0, len(binary_str), 7)]

    # Step 3: Convert each group into its decimal equivalent
    decimal_values = [int(group, 2) for group in binary_groups]

    hexa_values = [int(str(group + 21), 16) for group in decimal_values]

    # Step 5: Convert each decimal value to UTF-16 encoded bytes
    utf16_bytes = b''
    for value in hexa_values:
        if value < 0x10000:
            utf16_bytes += value.to_bytes(2, byteorder='big')
        else:
            # Convert to surrogate pairs
            high_surrogate = (value - 0x10000) // 0x400 + 0xD800
            low_surrogate = (value - 0x10000) % 0x400 + 0xDC00
            utf16_bytes += high_surrogate.to_bytes(2, byteorder='big') + low_surrogate.to_bytes(2, byteorder='big')

    # Step 6: Decode UTF-16 bytes to obtain the final string
    utf16_string = utf16_bytes.decode('utf-16')

    return utf16_string


def steps(step_count, word, jap_flag=True, l=0):
    sigma = 0
    sigma_r = 0

    for letter in word:
        exp = 1
        while 2 ** (exp + 1) < ord(letter):
            exp += 1
        sigma = (sigma + ord(letter)) * 2 ** exp

    for letter in word[-1::-1]:
        exp = 1
        while 2 ** (exp + 1) < ord(letter):
            exp += 1
        sigma_r = (sigma_r + ord(letter)) * 2 ** exp

    for i in range(step_count):
        sigma = sigma / 2 if not sigma % 2 else 3 * sigma + 1

    sigma = round(sigma) ^ sigma_r

    if jap_flag:
        return convert_to_utf(sigma)
    return stand(sigma, sigma_r, l)


def stand(x, y, l):
    # Convert the two large numbers into binary strings
    binary_str = bin(x)[2:] + bin(y)[2:]

    # Generate a hash from the binary string
    hash_digest = hashlib.sha256(binary_str.encode()).hexdigest()

    # Take the first 'length' characters of the hash digest
    alphanumeric = hash_digest[:l]

    return alphanumeric


print(steps([10, 20], 'digikey'))