# -*- coding: utf-8 -*-
import telepot
import time
import os
import random

# bot initialisation
token = os.environ['TOKEN']
bot = telepot.Bot(token)
received_messages = [x for x in bot.getUpdates()]
previous_message = received_messages[-1]['update_id']
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
          "Dio can frau", "Frocia", "Nico Ago sei merda con bisturi",
          "Massimo\nPensi di aver raggiunto il successo nella vita?", "Massimo\nCosa significa per te avere successo?",
          "Grande Gigi", "Vali meno del calcio alle olimpiadi", "Vabbè Leonardo", "Vali meno del trofeo TIM",
          "Vali meno di Papi", "Frau sei Amadeus", "Non vali nulla", "Dio can\nE anche oggi in Torre Archimede",
          "7.54 qualcuno?", "Ma che cazzo vuoi\nFallito di merda",
          "Nico Ago\nVali meno del cestino degli scarti ospedalieri", "Porco dio vali meno della carta del prosciutto",
          "Dio can persa anche questa al fanta", "Leonardo\nSecondo te l'economia è una scienza?",
          "Yoses\nPensi di essere comunista?", "Frau che fa tesi sui pedalò",
          "Porci ma quando esce articolo di ultimo uomo su Akinfeev?", "Stai buono", "Stai fermo",
          "Frau\nRimetti Nadali", "Frau\nButta fuori Trabbi", 'Yoses comunista che vota Monti',
          'Nadali togli Zuca', 'Che fantastica storia è la vita']

personalized_messages = {
    'Porci': {'id': 44834863, 'messages': ["Porci ma quando esce articolo di ultimo uomo su Akinfeev?"]},
    'Leo': {'id': 24030913, 'messages': ["Leonardo\nCosa ne pensi dei credenti?", "Vabbè Leonardo",
                                         "Leonardo\nSecondo te l'economia è una scienza?", 'Nadali togli Zuca']},
    'Beppe': {'id': 20344105, 'messages': ["Rozzi"]},
    'Frau': {'id': 38976241, 'messages': ["Dio can frau", "Frau sei Amadeus", "Frau che fa tesi sui pedalò",
                                          "Frau\nRimetti Nadali", "Frau\nButta fuori Trabbi"]},
    'Mex': {'id': 0, 'messages': ["Massimo\nPensi di aver raggiunto il successo nella vita?",
                                  "Massimo\nCosa significa per te avere successo?"]},
    'Fora': {'id': 80692823, 'messages': ["Frocia"]},
    'Luca': {'id': 24510037, 'messages': ["Ma Ruffi\nDormivi?"]},
    'Gigi': {'id': 308878806, 'messages': ["Grande Gigi"]},
    'Nico Ago': {'id': 0, 'messages': ["Nico Ago sei merda con bisturi",
                                       "Nico Ago\nVali meno del cestino degli scarti ospedalieri"]},
    'Trabucco': {'id': 0, 'messages': ["Trabbi\nCosa ne pensi di NCIS 9x10?"]},
    'Marassi': {'id': 0, 'messages': ["Grande André\nHai ficcato?"]},
    'Yoses': {'id': 0, 'messages': ["Yoses\nPensi di essere comunista?", 'Yoses comunista che vota Monti']}}


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

    bot.sendMessage(last_user, output_message)


# this is the function that will be called every time ZucaBot receives a new message
def interaction(message):

    # try to see if the received message contains any text, if so interacts, otherwise do nothing
    try:
        text = message['text']

        # answer based on the text
        if 'russia' in text.lower():
            bot.sendMessage(last_user, random.choice(russia))
        elif 'massimone' in text.lower():
            bot.sendMessage(last_user, 'Papirone')
        elif 'papirone' in text.lower():
            bot.sendMessage(last_user, 'Massimone')
        elif 'frau' in text.lower():
            dice_roll = random.randint(1, 4)
            if dice_roll == 1:
                bot.sendMessage(last_user, 'ebreo')
        elif 'scherzo' in text.lower():
            bot.sendMessage(last_user, 'Sei un grande')
        elif 'zuca' in text.lower():
            dice_roll = random.randint(1, 16)
            if dice_roll == 1:
                bot.sendMessage(last_user, random.choice(quotes))
            elif 2 <= dice_roll <= 3:
                send_personalized_message(message)
        # if nobody wants ZucaBot, send a message anyway with some probability
        else:
            dice_roll = random.randint(1, 80)
            if dice_roll == 1:
                bot.sendMessage(last_user, random.choice(quotes))
            elif 2 <= dice_roll <= 4:
                send_personalized_message(message)

    except KeyError:
        pass

# prints information on the received message
x = [print() for _ in range(10)]
for message in received_messages:
    print('\n\n\n\n\n\n\n\n\n\n')
    for key in message['message']:
        print(key)
        print(message['message'][key])


# main loop
while True:
    # repeats the loop every 1 seconds
    time.sleep(1)

    # variable that stores most recent messages
    received_messages = [x for x in bot.getUpdates(offset=offset)]

    # saves the ID of the user who wrote the last message
    last_user = received_messages[-1]['message']['chat']['id']
    # saves the ID of the last message
    new_message = received_messages[-1]['update_id']

    # checks if ZucaBot received a new message
    if new_message != previous_message:

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
        offset = received_messages[-1]['update_id'] - 10000  # only sees the last 10000 messages
        if offset < 0:
            offset = 0
