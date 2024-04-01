alphabet = (
    'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
    'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'ь', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї',
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', ',', '.', '+', '-', '/', '*', '–', '—', '(',
    ')', ':', ";", '[', ']', '{', '}')

def Caesar_encrypt(text, key):
    encrypt_text = []
    for x in range(0, len(text)):
        encrypt_text.append(alphabet[(alphabet.index(text[x]) + key) % len(alphabet)])
    return encrypt_text


def Caesar_decrypt(ciphertext, key):
    decrypt_text = []
    for x in range(0, len(ciphertext)):
        decrypt_text.append(alphabet[(alphabet.index(ciphertext[x]) - key) % len(alphabet)])
    return decrypt_text

print(Caesar_encrypt("Привіт", 2))
print(Caesar_decrypt("Стїґйф", 2))
