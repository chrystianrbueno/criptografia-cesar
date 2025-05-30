# Nomes: Chrystian e Jayme
# alfabeto permitido
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?()@ "
# tamanho limite da chave a ser utilizada
LIMIT = len(ALPHABET) - 1


def caesar_cipher(text, key, mode='encrypt'):
    # Inicializa a variável de resultado
    result = ""

    # Para cada caractere na mensagem
    for char in text:
        # Pega o índice do caractere no alfabeto
        index = ALPHABET.index(char)
        if mode == 'encrypt':
            # Avança no alfabeto com base na chave
            new_index = (index + key) % len(ALPHABET)
        else:
            # Retrocede no alfabeto com base na chave
            new_index = (index - key) % len(ALPHABET)
        result += ALPHABET[new_index]
    return result


def get_valid_key():
    while True:
        key_input = input(f"Entre com a chave entre 1 e {LIMIT}: ")
        # recebe entrada do usuário e verifica se é um número
        # enquanto não for um número válido, continua solicitando
        if not key_input.isdigit():
            print("Entrada inválida apenas numeros são aceitos.")
            continue
        # converte a entrada para inteiro e verifica se está dentro do limite
        # se estiver fora do limite, solicita novamente
        key = int(key_input)
        if 1 <= key <= LIMIT:
            return key
        else:
            print(f"Chave inválida. Apenas números entre 1 e {LIMIT}.")

if __name__ == "__main__":
    # menu para o usuário escolher entre criptografar, descriptografar ou sair
    while True:
        print("\n=== Cifra de César ===")
        print("1. Criptografar mensagem")
        print("2. Descriptografar mensagem")
        print("3. Sair")

        option = input("Escolha a opção: ")

        # verifica a opção escolhida pelo usuário
        if option == "1":
            message = input("Entre com a mensagem a ser criptografada: ")
            # verifica se a mensagem contém apenas caracteres permitidos
            if not all(char in ALPHABET for char in message):
                print(f"A mensagem contém caracteres inválidos, os caracteres permitidos são: {ALPHABET}")
                continue
            # solicita a chave ao usuário
            key = get_valid_key()
            # criptografa a mensagem usando a cifra de César
            encrypted = caesar_cipher(message, key, mode='encrypt')
            print("Mensagem criptografada:", encrypted)

        elif option == "2":
            message = input("Entre com a mensagem a ser descriptografada: ")
            # verifica se a mensagem contém apenas caracteres permitidos
            if not all(char in ALPHABET for char in message):
                print(f"A mensagem contém caracteres inválidos, os caracteres permitidos são: {ALPHABET}")
                continue
            # solicita a chave ao usuário
            key = get_valid_key()
            # descriptografa a mensagem usando a cifra de César
            decrypted = caesar_cipher(message, key, mode='decrypt')
            print("Mensagem descriptografada:", decrypted)

        elif option == "3":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
