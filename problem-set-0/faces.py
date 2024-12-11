# juntar a parte da mensagem que não tem a carinha
# Substituir :) por 😄 ou por ☹️

def convertMessage(message):
    if ':)' in message and ':(' not in message:
        new_message = message.replace(':)', '😄')
        print(new_message)
    
    elif ':(' in message and ':)' not in message:
        new_message = message.replace(':(', '☹️')
        print(new_message)

    elif (':)' and ':(') in message:
        new_message = message.replace(':)', '😄')
        new_message2 = new_message.replace(':(', '☹️')
        print(new_message2)

def main():
    convertMessage('Hello :), good bye :(')
main()