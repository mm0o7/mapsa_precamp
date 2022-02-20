def convert_num(text: str) ->list:
    text.upper()
    num_list = [ord(char) - 65 for char in text]
    return num_list

def convert_text(nums: list) ->str:
    text_string = "".join([chr(num + 65) for num in nums])
    return text_string

def cesar_encrypt(text: str, offset: int) ->str:
    number_of_text = convert_num(text)
    encrypt_number = []
    for x in number_of_text:
        encrypt_number.append((x + offset) % 26)
    encrypt_text = convert_text(encrypt_number)
    return encrypt_text

def cesar_decrypt(text: str, offset: int) ->str:
    number_of_text = convert_num(text)
    decrypt_number = []
    for x in number_of_text:
        decrypt_number.append((x - offset) if x >= offset else 26 + x - offset)
    decrypt_text = convert_text(decrypt_number)
    return decrypt_text

if __name__ == "__main__":
    print(cesar_encrypt(input("text: "), int(input("offset: "))))
    print(cesar_decrypt(input("encrypted text: "), int(input("offset: "))))
    