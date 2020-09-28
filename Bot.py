import telepot # BIBLIOTECA RESPONSAVEL DOS COMANDOS EXISTENTES
import pyrebase
from datetime import datetime

config = {
  "apiKey": "AIzaSyD_ke-7MnRL3SUk1tJ8reNsXwSjXcv0aqg",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://heimdall-6e62b.firebaseio.com/",
  "storageBucket": "gs://heimdall-6e62b.appspot.com"

}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("william@hackbrightacademy.com", "mySuperStrongPassword")

# Get a reference to the database service
db = firebase.database()


bot = telepot.Bot('948606588:AAEifEtfWsm8U7VHgshlHKjXHQ2U9lMrGqg') #BOT DE BACK UP2
#bot = telepot.Bot('903074246:AAGSRnjBo_39KVCj-OuxHsWLCGkj3EteSI0') #API DO BOT NO TELEGRAM

id_chat = 594114579 #id chat do ADM do bot
#id_chat = -352685425 #id chat do ADM do bot
#id_chat = -340067400 #id chat do ADM do bot


def recebendo(msg): #FUNÇÃO QUE RECEBE A MENSAGEM QUE O BOT RECEBE

    print(bot.getUpdates())

    msg_texto = msg['text'] # ARMAZENA A MENSAGEM QUE ENVIARAM AO BOT
    msg_id = msg['chat']['id']  # ARMAZENA O ID DO CHAT DA PESSOA QUE MANDOU MENSAGEM AO BOT

    print(msg_texto)

    if msg_texto == '/1': # Caso seja 1 a mensagem enviada ele abre a fechadura
        print(bot.getUpdates())
        msg_user = msg['from']['first_name'] + " " + msg['from']['last_name']
        msg_date = msg['date']

        your_time_stamp = int(msg_date)
        human_date = datetime.fromtimestamp(your_time_stamp).strftime('%d-%m-%Y')
        human_hour = datetime.fromtimestamp(your_time_stamp).strftime('%H:%M:%S')
        print(human_date)

        data = {
            "usuario": msg_user,
            "comando": "abrir",
            "data": human_date,
            "hora": human_hour,
        }
        db.child("Status").push(data, user['idToken'])
        bot.sendMessage(id_chat, "STATUS ATUALIZADO")

    if msg_texto == '2': # Caso 2, captura novamente uma foto
        bot.sendMessage(id_chat, "FOTO TIRADA")

    if msg_texto == '/3': # Caso 3,  envia os dados do banco de dados sobre todas as aberturas da fechadura

        hist = db.child("Status").order_by_child("data").get(user['idToken'])
        print(hist.val())

        bot.sendMessage(id_chat, "HISTÓRICO!\n")
        bot.sendMessage(id_chat, hist.val())

    if msg_texto == '4':  # Caso 5, cadastro de loogine senha
        bot.sendMessage(id_chat, "INSIRA SEU NOME:")


        #bot.sendMessage(id_chat, "INSIRA SEU NUMERO:")
        #password = telepot.password(msg)
        #auth.create_user_with_email_and_password(email, password)


def envia_msg (admin): # função para enviar mensagem ao adm do bot

    # bot.sendPhoto(admin, "FOTO A SER ENVIADA PARA A PESSOA") <- aqui será enviado a foto para o bot

    bot.sendMessage(admin, "INSTRUÇÕES:\n\n"
                           "1- \tABRIR FECHADURA\n\n"
                           "2- \tFECHAR FECHADURA\n\n"
                           "3- \tHISTÓRICO DA FECHADURA\n\n"
                           "4- \tFOTO\n\n" # MUDEI O VALOR DA FOTO instruções de como vai funcionar o comando para o bot
                           "5- \tADICIONAR USUARIO\n\n")



envia_msg(id_chat)

telegram = bot.message_loop(recebendo) #loop para ficar recebendo tudo do bot


while True:
        pass
