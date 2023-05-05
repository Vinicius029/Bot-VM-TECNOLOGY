from telebot import TeleBot
import datetime
from information import BOT_TOKEN_API

BOT_TOKEN = BOT_TOKEN_API

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['VM'])
def servicos(message):
    bot.send_photo(message.chat.id, photo=open(r'images\apresentacaoVM.jpeg','rb'))
    texto = """
    Acesse nossas rede sociais e fique por dentro de tudo da
VM-TECHNOLOGY!

https://idolink.com/VMTechnology
    """
    bot.send_message(message.chat.id, texto)
  

@bot.message_handler(commands=['servicos'])
def servicos(message):
    servicos = """
    Confira os nossos serviços detalhadamente...

1. Currículo Online

    - Fazemos seu currículo da melhor maneira possível.
    - Dicas de como mandar bem na hora da entrega.

2. Formatação de PCs

    - Instalação do Windows, programas.

3. Assistência Web

    - Realização de cadastramento em geral, como qualquer 
    outro trabalho que precisar.

4. Prestação de Ajuda Computacional

    - Ajudar a tirar dúvidas em relação as dificuldades web.
    - Apoio em serviços online.

5. Aulas Particular de Informática

    - trodução à Informática, principais componentes de um
    computador, funcionamento básico de um computador.
    - Sistema operacional Windows, noções básicas do Sistema 
    Operacional Windows.
    - Introdução à Internet.
    - Prática de navegação pela WEB.
    """
    bot.send_message(message.chat.id, servicos)
   

@bot.message_handler(commands=['valores'])
def valores_dos_servicos(message):
    bot.send_message(message.chat.id, "Confira os preços do nossos serviços!")
    bot.send_photo(message.chat.id, photo=open(r'images\valoresVM.jpeg','rb'))


def hora_do_dia():
    hora = datetime.datetime.now().hour
    if hora >= 5 and hora <= 12:
        return 'Bom Dia'
    elif hora >12 and hora <= 17:
        return 'Boa Tarde'
    else:
        return 'Boa Noite'


@bot.message_handler(func=lambda msg: True)
def resposta(message):
    hora = hora_do_dia()
    opcoes = f"""
    Olá, {hora}! 
    
Selecione a opção desejada:

        /VM Sobre nós
        /servicos Nossos Serviços
        /valores  Confira Nossos Valores

Clica sobre a opção contendo "/", ou digite a opção desejada com "/" na inicial.
    """
    bot.send_message(message.chat.id, opcoes)
    
  

bot.infinity_polling()