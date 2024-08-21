# Importar a biblioteca
import openai

# Definir a chave da API antes de usar a biblioteca
openai.api_key = "digite uma chave válida"

# Função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):

    # Obter resposta do modelo de linguagem
    response = openai.ChatCompletion.create(

        # Modelo utilizado
        model="gpt-4",
        messages=[
            {"role": "user", "content": texto}
        ],

        # Comprimento da resposta
        max_tokens=280,

        # Quantas conclusões gerar para cada prompt
        n=1,

        # Aleatoriedade do texto
        temperature=0.8, 
    )

    # Retornar o conteúdo da resposta
    return response['choices'][0]['message']['content'].strip()

# Função principal
def main():
    print("\nBem-vindo ao GPT-4 ChatBot!")
    print("(Digite 'sair' a qualquer momento para encerrar o chat!)")

    # Loop
    while True:
        # Coleta a pergunta
        user_message = input("\nVocê: ")

        # Finalizar
        if user_message.lower() == "sair":
            break

        # Obter resposta
        chat_response = gera_texto(user_message)

        # Imprime resposta
        print(f"\nChatBot: {chat_response}")

# Executa o programa
if __name__ == "__main__":
    main()