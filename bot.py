# -*- coding: utf-8 -*-
import telepot
import time
import os
import random
import datetime

# bot initialisation
token = os.environ['TOKEN']
bot = telepot.Bot(token)
received_messages = []
for x in bot.getUpdates():
    try:
        check = x['message']
        received_messages.append(x)
    except KeyError:
        pass
messages_num = len(received_messages)
print('Messages received:', messages_num)
previous_message = received_messages[-1]['update_id']
disservizi = -243280032
offset = 0

russia = ["FC Abinsk", "FC Agan Raduzhny", "FC Agidel Ufa", "FC Agrokomplekt Ryazan",
           "FC Akademiya Dimitrovgrad", "FC Akademiya Togliatti", "FC Alania-2 Vladikavkaz",
           "FC Alania Vladikavkaz", "FC Aleks Angarsk", "FC Aleks Gatchina", "FC Almaz Moscow",
           "FC Alnas Almetyevsk", "FC Altair-Khelling Derbent", "FC Amkar Perm", "FC Amur Blagoveshchensk",
           "FC Amur-Energia Blagoveshchensk", "FC Amur Komsomolsk-on-Amur", "FC Anapa", "FC Angara Angarsk",
           "FC Angara Boguchany", "FC Angusht Malgobek", "FC Angusht Nazran", "FC Anzhi-2 Kaspiysk",
           "FC Anzhi Makhachkala", "FC APK Azov", "FC APK Morozovsk", "FC Argo Kaspiysk",
           "FC Arsenal-2 Tula", "FC Arsenal Tula", "FC Arzamas", "FC Asmaral Kislovodsk",
           "FC Asmaral Moscow", "FC Astrakhan", "FC Astrateks Astrakhan", "FC Atommash Volgodonsk",
           "FC Avangard Kamyshin", "FC Avangard Kolomna", "FC Avangard-Kolos Taganrog",
           "FC Avangard-Kortek Kolomna", "FC Avangard Kursk", "FC Avangard Podolsk",
           "FC Avtodor-BMK Vladikavkaz", "FC Avtodor-Olaf Vladikavkaz", "FC Avtodor Vladikavkaz",
           "FC Avtomobilist Noginsk", "FC Avtomobilist Yuzhno-Sakhalinsk", "FC Avtopribor Oktyabrsky",
           "FC Avtozapchast Baksan", "FC Azamat Cheboksary", "FC Balakovo", "FC Baltika-2 Kaliningrad",
           "FC Baltika Kaliningrad", "FC Baltika-Tarko Kaliningrad", "FC Bashinformsvyaz-Dynamo Ufa",
           "FC Bataysk-2007", "FC Baysachnr Elista", "FC Berezniki", "FC Beshtau Lermontov",
           "FC Beslan-FAYUR Beslan", "FC Biokhimik-Mordovia Saransk", "FC BSK Spirovo",
           "FC Bulat Cherepovets", "FC Chelyabinsk", "FC Chernomorets-2 Novorossiysk",
           "FC Chernomorets Novorossiysk", "FC Chertanovo Moscow", "FC Chita",
           "FC Chkalovets-1936 Novosibirsk", "FC Chkalovets Novosibirsk", "FC Chkalovets-Olympic Novosibirsk",
           "FC CSKA-2 Moscow", "FC CSKA Moscow", "FC CSK VVS-Kristall Smolensk", "FC Dagdizel Kaspiysk",
           "FC Derbent", "FC Devon Oktyabrsky", "FC Diana Volzhsk", "FC Dmitrov", "FC Dnepr Smolensk",
           "FC Don Novomoskovsk", "FC Druzhba Budyonnovsk", "FC Druzhba Maykop", "FC Druzhba Yoshkar-Ola",
           "FC Dynamo-2 Moscow", "FC Dynamo Barnaul", "FC Dynamo Bryansk", "FC Dynamo-Gazovik Tyumen",
           "FC Dynamo-Imamat Makhachkala", "FC Dynamo Izhevsk", "FC Dynamo Izobilny", "FC Dynamo Kemerovo",
           "FC Dynamo Kirov", "FC Dynamo Kostroma", "FC Dynamo Makhachkala", "FC Dynamo-Mashinostroitel Kirov",
           "FC Dynamo Mikhaylovka", "FC Dynamo Moscow", "FC Dynamo Omsk", "FC Dynamo Perm",
           "FC Dynamo Saint Petersburg", "FC Dynamo Stavropol", "FC Dynamo Tula", "FC Dynamo Vologda",
           "FC Dynamo Voronezh", "FC Dynamo Yakutsk", "FC Dynamo-Zhemchuzhina-2 Sochi", "FC Elektron Almetyevsk",
           "FC Elektronika Nizhny Novgorod", "FC Elektron Vyatskiye Polyany", "FC Elista", "FC Energetik Uren",
           "FC Energia Chaykovsky", "FC Energia Kamyshin", "FC Energia Pyatigorsk"]

quotes = ["Icurdi o Icardi?", "Chi aula?", "Klose dell'altro mondo", "Siete dei calcinacci",
          "Cosa avevi in mente? Tutta un'altra vita", "Che fantastica storia è la vita", "Rozzi",
          "Trabbi\nCosa ne pensi di NCIS 9x10?", "Leonardo\nCosa ne pensi dei credenti?",
          "Sto andando a fare ripe", "Dio can", "Grande André\nHai ficcato?", "Ma Ruffi\nDormivi?",
          "Dio can frau", "Frocia", "Nico Ago sei merda con bisturi", "Ca' Fosfati",
          "Massimo\nPensi di aver raggiunto il successo nella vita?", "Massimo\nCosa significa per te avere successo?",
          "Grande Gigi", "Vali meno del calcio alle olimpiadi", "Vabbè Leonardo", "Vali meno del trofeo TIM",
          "Vali meno di Papi", "Frau sei Amadeus", "Non vali nulla", "Dio can\nE anche oggi in Torre Archimede",
          "Ma che cazzo vuoi\nFallito di merda", 'AAA cercasi coerenza', "Troppo triste pendando all'11 settembre",
          "Nico Ago\nVali meno del cestino degli scarti ospedalieri", "Porco dio vali meno della carta del prosciutto",
          "Dio can persa anche questa al fanta", "Leonardo\nSecondo te l'economia è una scienza?",
          "Yoses\nPensi di essere comunista?", "Frau che fa tesi sui pedalò", 'Rimettere Borto',
          "Porci ma quando esce articolo di ultimo uomo su Akinfeev?", "Stai buono", "Stai fermo",
          "Frau\nRimetti Nadali", "Frau\nButta fuori Trabbi", 'Yoses comunista che vota Monti',
          'Nadali togli Zuca', 'Che fantastica storia è la vita', 'Dio can', 'È sempre il solito teatrino',
          'È sempre il solito teatrino', 'Nadali, ti prego trovami le radici reali di x^2+1=0',
          'Prendiamo cinque stronzi fatti bene', 'Ha avuto ptutto', 'Tutti i CV bombi', 'Consare pencosticine',
          'Incontrato merde cartolaie', 'Non mi gasa ragazza puttana', 'Madonna brutta pellegrina\nAiutatemi',
          'Grazie, Boutique Raphaelle!', 'Considerato: buono', 'Considerato: cattivo',
          'Non come qualcun altro Agostini']

# this dictionary is used to send personalized messages. It contains one sub-set for each user, 'id' is
# the Telegram ID of that user, 'messages' is the list of possible personalized messages, and
# 'last_sent' hold the last personalised messages that were to that person (to check for repetitions)
personalized_messages = {
    'Porci': {'id': 44834863,
              'messages': ["Porci ma quando esce articolo di ultimo uomo su Akinfeev?"],
              'last_sent': []},
    'Leo': {'id': 24030913,
            'messages': ["Leonardo\nCosa ne pensi dei credenti?", "Vabbè Leonardo",
                         "Leonardo\nSecondo te l'economia è una scienza?", 'Nadali togli Zuca',
                         'Nadali, ti prego trovami le radici reali di x^2+1=0'],
            'last_sent': []},
    'Beppe': {'id': 20344105,
              'messages': ["Rozzi"],
              'last_sent': []},
    'Frau': {'id': 38976241,
             'messages': ["Dio can frau", "Frau sei Amadeus", "Frau che fa tesi sui pedalò",
                          "Frau\nRimetti Nadali", "Frau\nButta fuori Trabbi", 'Frau ebreo',
                          'Frau sei Enrico Papi'],
             'last_sent': []},
    'Mex': {'id': 54573695,
            'messages': ["Massimo\nPensi di aver raggiunto il successo nella vita?",
                         "Massimo\nCosa significa per te avere successo?"],
            'last_sent': []},
    'Fora': {'id': 80692823,
             'messages': ["Frocia"],
             'last_sent': []},
    'Luca': {'id': 24510037,
             'messages': ["Ma Ruffi\nDormivi?", 'Luca\nTi gasa ragazza puttana?'],
             'last_sent': []},
    'Gigi': {'id': 308878806,
             'messages': ["Grande Gigi"],
             'last_sent': []},
    'Nico Ago': {'id': 0,
                 'messages': ["Nico Ago sei merda con bisturi", 'Non come qualcun altro Agostini',
                              "Nico Ago\nVali meno del cestino degli scarti ospedalieri"],
                 'last_sent': []},
    'Trabucco': {'id': 0,
                 'messages': ["Trabbi\nCosa ne pensi di NCIS 9x10?"],
                 'last_sent': []},
    'Marassi': {'id': 0,
                'messages': ["Grande André\nHai ficcato?"],
                'last_sent': []},
    'Yoses': {'id': 0,
              'messages': ["Yoses\nPensi di essere comunista?", 'Yoses comunista che vota Monti',
                           'Ma Yoses, sei stupido?', 'AAA cercasi coerenza',
                           'Non come qualcun altro Agostini'],
              'last_sent': []},
    'Cevallos': {'id': 1168808856,
                 'messages': ['Dio can Ceva'],
                 'last_sent': []},
    'Zuca': {'id': 323998218,
             'messages': ['Nadali, togli Zuca'],
             'last_sent': []}}


# checks if 'x' is within 'start' and 'end', used to see if it's time for the LateShow
def is_time_in_range(start, end, x):
    # true if x is in range
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


# this function is used to send a personalised message
def send_personalized_message(message):

    # checks if the user who sent the message is in the dictionary "personalized_messages"
    personalized = False
    reply_to = ''
    for user in personalized_messages:
        if personalized_messages[user]['id'] == message['from']['id']:
            personalized = True
            reply_to = user

    # if the user is not in the dictionary, just send a random message, otherwise choose appropriately
    if personalized is False:
        output_message = random.choice(quotes)
    else:
        output_message = random.choice(personalized_messages[reply_to]['messages'])

        # checks if the chosen message has already been sent recently to that user
        while output_message in personalized_messages[reply_to]['last_sent']:
            output_message = random.choice(personalized_messages[reply_to]['messages'])

        # updates 'last_sent' to only keep the last messages
        personalized_messages[reply_to]['last_sent'].append(output_message)
        personalized_messages[reply_to]['last_sent'] = personalized_messages[reply_to]['last_sent'][-4:]

    # if ZucaBot is replying to Zuca, there is a chance it will just repeat what he said
    if reply_to == 'Zuca':
        dice_roll = random.randint(1, 5)
        if dice_roll < 5:
            output_message = message['text']

    bot.sendMessage(chat, output_message)


# this is the function that will be called every time ZucaBot receives a new message
def interaction(message):

    # try to see if the received message contains any text, if so interacts, otherwise do nothing
    try:
        text = message['text']

        # checks if the last 3 messages are the same (quindi siamo in una catena), if so reply the same
        try:
            if received_messages[-1]['message']['text'] == received_messages[-2]['message']['text'] and \
               received_messages[-2]['message']['text'] == received_messages[-3]['message']['text']:
                bot.sendMessage(chat, text)
        except KeyError:
            pass

        # answer based on the text
        if 'russia' in text.lower():
            bot.sendMessage(chat, random.choice(russia))
        elif 'massimone' in text.lower():
            bot.sendMessage(chat, 'Papirone')
        elif 'papirone' in text.lower():
            bot.sendMessage(chat, 'Massimone')
        elif 'frau' in text.lower():
            dice_roll = random.randint(1, 4)
            if dice_roll == 1:
                bot.sendMessage(chat, 'Ebreo')
        elif 'scherzo' in text.lower():
            bot.sendMessage(chat, 'Sei un grande')
        elif 'é' in text.lower() and 'perché' not in text.lower():
            bot.sendMessage(chat, '*è')
        elif "qual'è" in text.lower():
            bot.sendMessage(chat, '*qual è')
        elif "perchè" in text.lower():
            bot.sendMessage(chat, '*perché')
        elif 'italia' in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                bot.sendMessage(chat, 'Il paese che amk')
        elif 'togli zuca' in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                bot.sendMessage(chat, 'Stai buono')
        elif 'salvini' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                bot.sendMessage(chat, 'Considerato: cattivo')
        elif 'berlusconi' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                bot.sendMessage(chat, 'Considerato: cattivo')
        elif 'renzi' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                bot.sendMessage(chat, 'Considerato: buono')
        elif "ca" in text.lower() and "foscari" in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                bot.sendMessage(chat, "Ca' Fosfati")
        elif 'zuca, sei' in text.lower() or 'zuca sei' in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                bot.sendMessage(chat, "Ma che cazzo vuoi\nFallito di merda")
        elif 'boldrini' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                bot.sendMessage(chat, random.choice(['Considerata: buona',
                                                     'Ceva cosa ne pensi della Boldrini?']))
        elif 'bebe' in text.lower() and 'vio' in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                bot.sendMessage(chat, random.choice(['Sì, ma con le protesi',
                                                     'Sì, ma senza protesi']))
        elif 'hahaha' in text.lower() or 'ahhah' in text.lower():
            dice_roll = random.randint(1, 20)
            if dice_roll == 1:
                bot.sendMessage(chat, random.choice(['Ma cosa ridi deficiente?',
                                                     "L'unica cosa che fa ridere è la tua vita"]))
        elif 'zuca' in text.lower():
            dice_roll = random.randint(1, 100)
            if dice_roll < 5:
                bot.sendMessage(chat, random.choice(quotes))
            elif 4 <= dice_roll < 6:
                send_personalized_message(message)
        # if nobody wants ZucaBot, send a message anyway with some probability
        else:
            dice_roll = random.randint(1, 1000)
            if 1 <= dice_roll < 5:
                bot.sendMessage(chat, random.choice(quotes))
            elif 5 <= dice_roll < 7:
                send_personalized_message(message)

    except KeyError:
        pass

# prints information on the received message
x = [print() for _ in range(10)]
for message in received_messages:
    print('\n\n\n\n\n\n\n\n\n\n')
    print(message)
    for key in message['message']:
        print(key)
        print(message['message'][key])


# main loop
while True:
    # repeats the loop every 1 seconds
    loop_cycle = 1  # number of seconds between loops
    time.sleep(loop_cycle)

    # variable that stores most recent messages
    received_messages = []
    for x in bot.getUpdates(offset=offset):
        try:
            check = x['message']
            received_messages.append(x)
        except KeyError:
            pass
    print(received_messages[-1])

    # saves the ID of the chat who wrote the last message
    chat = received_messages[-1]['message']['chat']['id']
    # saves the ID of the last message
    new_message = received_messages[-1]['update_id']

    # if it's late in the night, has a small chance to ask 'Chi late?'
    start = datetime.time(1, 0, 0)
    end = datetime.time(3, 0, 0)
    if is_time_in_range(start, end, datetime.datetime.time(datetime.datetime.now())):
        dice_roll = random.randint(1, 14.400/loop_cycle)
        if dice_roll == 1:
            bot.sendMessage(disservizi, 'Chi Late?')
    # if it's early in the morning, has a small chance to ask '7.54 qualcuno?'
    start = datetime.time(6, 30, 0)
    end = datetime.time(7, 30, 0)
    if is_time_in_range(start, end, datetime.datetime.time(datetime.datetime.now())):
        dice_roll = random.randint(1, 14.400/loop_cycle)
        if dice_roll == 1:
            bot.sendMessage(disservizi, '7.54 qualcuno?')

    # checks if ZucaBot received a new message
    if new_message != previous_message:
        print('NEW MESSAGE RECEIVED')

        # interacts
        interaction(received_messages[-1]['message'])

        # prints information on the received message
        x = [print() for _ in range(10)]
        print('\n\n\n\n\n\n\n\n\n\n')
        for key in received_messages[-1]['message']:
            print(key)
            print('___________________', received_messages[-1]['message'][key])

        # discards the last message and gets ready to receive a new one
        previous_message = new_message
        offset = received_messages[-1]['update_id'] - 50  # only sees the last 50 messages
        if offset < 0:
            offset = 1
