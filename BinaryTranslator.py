
error_not_binary = " Make sure you have entered a binary text! "


def binary_to_ascii(binary):
    new_text = []
    for binary_num in binary.split():
        is_binary = all([i == "1" or i == "0"
                         for i in str(binary_num)])
        if is_binary is True:
            try:
                new_text.append(chr(sum(int(n)*int(2**i)
                                        for i, n in enumerate(reversed(str(binary_num))))))
            except ValueError:
                new_text.append('')
        else:
            return error_not_binary
    return "".join(new_text)


def ascii_to_binary(text):
    binary_text = []
    for letter in text:
        converted = ''
        number = ord(letter)

        while number > 0:
            converted = str(number % 2) + converted
            number //= 2

        binary_text.append(
            converted.zfill(8))

    return " ".join(binary_text)


def binary_format(binary_code):
    new_format1 = []

    for i, b in enumerate(binary_code.split()):
        new_format1.append(b + '\n' if (i + 1) % 3 == 0 else b + ' ')

    try:
        new_format1[0] = ' ' + new_format1[0]
    except IndexError: pass

    for i, b in enumerate(new_format1):
        if i != len(new_format1) - 1:
            if '\n' in b:
                new_format1[i + 1] = ' ' + new_format1[i + 1]
    return ''.join(new_format1)




