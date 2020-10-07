def parse_to_chr(text):
    digits = ''
    for digit in text:
        if not str(digit).isdigit():
            break

        digits += digit

    ascii_value = int(digits)
    chr_value = chr(ascii_value)
    new_word = text.replace(digits, chr_value)
    return new_word


def replace_in_text(text):
    temp = list(text)
    temp[1], temp[-1] = temp[-1], temp[1]
    return ''.join(temp)


def decipher(text):
    res = parse_to_chr(text)
    res = replace_in_text(res)
    return res


words = input().split(' ')
new_text = [decipher(word) for word in words]
print(' '.join(new_text))