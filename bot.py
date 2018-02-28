# -*- coding: utf-8 -*-
import telepot
import time
import os
import random
import datetime

# bot initialisation
token = os.environ['ZUCABOT_TOKEN']
bot = telepot.Bot(token)
received_messages = []
authors = []
for x in bot.getUpdates():
    try:
        check = x['message']
        received_messages.append(x)
        authors.append(x['message']['from']['id'])
    except KeyError:
        pass
print(authors)
messages_num = len(received_messages)
print('Messages received:', messages_num)
previous_message = received_messages[-1]['update_id']
last_message_datetime = time.time()
disservizi = -243280032
leonardo = 24030913
progetto_zucabot = -171074079
test_group = -307834730
offset = 0
chain = ''

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
          "Trabbi\nCosa ne pensi di NCIS 9x10?", "Sto andando a fare ripe", "Dio can",
          "Dio can frau", "Frocia", "Nico Ago merda con bisturi", "Ca' Fosfati", 'Ospe\ndale',
          "Vali meno del calcio alle olimpiadi", "Vabbè", "Vali meno del trofeo TIM",
          "Vali meno di Papi", "Frau Amadeus", "Non vali nulla", "Dio can\nE anche oggi in Torre Archimede",
          "Ma che cazzo vuoi\nFallito di merda", 'AAA cercasi coerenza', "Troppo triste pendando all'11 settembre",
          "Porco dio vali meno della carta del prosciutto", "Dio can persa anche questa al fanta",
          "Frau che fa tesi sui pedalò", 'Rimettere Borto', "Porci ma quando esce articolo di ultimo uomo su Akinfeev?",
          "Stai buono", "Stai fermo", "Frau\nRimetti Nadali", "Frau\nButta fuori Trabbi",
          'Yoses comunista che vota Monti', 'Nadali togli Zuca', 'Che fantastica storia è la vita', 'Dio can',
          'È sempre il solito teatrino', 'È sempre il solito teatrino',
          'Nadali, ti prego trovami le radici reali di x^2+1=0', 'Siete dei calcinacci',
          'Prendiamo cinque stronzi fatti bene', 'Ha avuto ptutto', 'Tutti i CV bombi', 'Consare pencosticine',
          'Incontrato merde cartolaie', 'Non mi gasa ragazza puttana', 'Occhiale o non occhiale?',
          'Grazie, Boutique Raphaelle!', 'Considerato: \nbuono', 'Considerato: \ncattivo',
          'Non come qualcun altro Agostini', 'Madonna brutta pellegrina\nAiutatemi', 'Nadali rimetti Porci',
          'A che ora passa il Nadali-Stringari?', 'È già passato lo Stringari-Frociadori?',
          'Nadali fammi entrare nella Sadness', 'Fora che per scopare deve andare in paesi del terzo mondo']

offese = ["Ma Ruffi\nDormivi?", "Nico Ago merda con bisturi", "Vali meno del calcio alle olimpiadi",
          "Vali meno del trofeo TIM", "Vali meno di Papi", "Frau Amadeus", "Non vali nulla",
          "Ma che cazzo vuoi\nFallito di merda", "Nico Ago\nVali meno del cestino degli scarti ospedalieri",
          "Porco dio vali meno della carta del prosciutto", 'Yoses comunista che vota Monti',
          'Nadali, ti prego trovami le radici reali di x^2+1=0', 'Non come qualcun altro Agostini',
          'Fora che per scopare deve andare in paesi del terzo mondo', "Frau sei Amadeus",
          "Frau che fa tesi sui pedalò", 'Frau ebreo', "Frau cosa ci fai qua? Non è il giorno dell'umido",
          "Nico Ago sei merda con bisturi", "Agostini cosa ci fai qua? Non è il giorno dell'umido",
          'Ma Yoses, sei stupido?', "Yoses comunista con l'iphone",
          'Mamma del Miuro è sinonimo di puttana, quindi puoi metterla in qualsiasi contesto']

complimenti = ["Che fantastica storia è la vita", "Leonardo\nCosa ne pensi dei credenti?", "Grande Gigi",
               "Leonardo\nSecondo te l'economia è una scienza?", "Yoses\nPensi di essere comunista?",
               'Non mi gasa ragazza puttana', 'Luca\nTi gasa ragazza puttana?', 'I <3 Sebach',
               'La mamma dei Miur è sempre incinta']

# this dictionary is used to send personalized messages. It contains one sub-set for each user, 'id' is
# the Telegram ID of that user, 'messages' is the list of possible personalized messages, and
# 'last_sent' hold the last personalised messages that were to that person (to check for repetitions)
personalized_messages = {
    'Porci': {'id': 44834863,
              'messages': ["Porci ma quando esce articolo di ultimo uomo su Akinfeev?"],
              'last_sent': []},
    'Leo': {'id': 24030913,
            'messages': ["Leonardo\nCosa ne pensi dei credenti?", "Vabbè Leonardo", "Vabbè Leonardo",
                         "Leonardo\nSecondo te l'economia è una scienza?", 'Nadali togli Zuca',
                         'Nadali, ti prego trovami le radici reali di x^2+1=0', 'Leonardino Fuffolo',
                         'Leonardino Fuffolo', 'Nadali togli Zuca',
                         'Nadali, ti prego trovami le radici reali di x^2+1=0'],
            'last_sent': []},
    'Beppe': {'id': 20344105,
              'messages': ["Rozzi"],
              'last_sent': []},
    'Frau': {'id': 38976241,
             'messages': ["Dio can frau", "Frau sei Amadeus", "Frau che fa tesi sui pedalò",
                          "Frau\nRimetti Nadali", "Frau\nButta fuori Trabbi", 'Frau ebreo', 'Ospe\ndale'
                          'Frau sei Enrico Papi', "Frau cosa ci fai qua? Non è il giorno dell'umido"],
             'last_sent': []},
    'Mex': {'id': 54573695,
            'messages': ["Massimo\nPensi di aver raggiunto il successo nella vita?",
                         "Massimo\nCosa significa per te avere successo?"],
            'last_sent': []},
    'Fora': {'id': 80692823,
             'messages': ["Frocia", 'Başakbanchi', 'Fora che per scopare deve andare in paesi del terzo mondo',
                          'Frociadori'],
             'last_sent': []},
    'Luca': {'id': 24510037,
             'messages': ["Ma Ruffi\nDormivi?", 'Luca\nTi gasa ragazza puttana?', 'Luca, vali meno di Papi'],
             'last_sent': []},
    'Gigi': {'id': 308878806,
             'messages': ["Grande Gigi"],
             'last_sent': []},
    'Nico Ago': {'id': 0,
                 'messages': ["Nico Ago sei merda con bisturi", 'Non come qualcun altro Agostini',
                              "Nico Ago\nVali meno del cestino degli scarti ospedalieri",
                              "Agostini cosa ci fai qua? Non è il giorno dell'umido"],
                 'last_sent': []},
    'Trabucco': {'id': 0,
                 'messages': ["Trabbi\nCosa ne pensi di NCIS 9x10?"],
                 'last_sent': []},
    'Marassi': {'id': 129705113,
                'messages': ["Grande André\nHai ficcato?"],
                'last_sent': []},
    'Yoses': {'id': 62613803,
              'messages': ["Yoses\nPensi di essere comunista?", 'Yoses comunista che vota Monti',
                           'Ma Yoses, sei stupido?', 'AAA cercasi coerenza',
                           'Non come qualcun altro Agostini', "Yoses comunista con l'iphone"],
              'last_sent': []},
    'Cevallos': {'id': 1168808856,
                 'messages': ['Dio can Ceva', 'Occhiale o non occhiale?'],
                 'last_sent': []},
    'Zuca': {'id': 323998218,
             'messages': ['Nadali, togli Zuca', 'Questo bot fa schifo', 'Nadali hai aggiunto nuove frasi a Zuca?'],
             'last_sent': []},
    'Seba': {'id': 25331042,
             'messages': ['Sebach', 'I <3 Sebach', 'Sebach'],
             'last_sent': []},
    'Tazio': {'id': 92110842,
              'messages': ['stazione'],
              'last_sent': []},
    'Carlo Marchetto': {'id': 29315826,
                        'messages': [],
                        'last_sent': []},
    'Miur': {'id': 0,
             'messages': ['Mamma del Miuro è sinonimo di puttana, quindi puoi metterla in qualsiasi contesto',
                          'No porno Miur', 'La mamma dei Miur è sempre incinta'],
             'last_sent': []},
    'Immaginary_bot': {'id': 25331042,
                       'messages': ['Sebach', 'I <3 Sebach', 'Sebach'],
                       'last_sent': []}}


# checks if 'x' is within 'start' and 'end', used to see if it's time for the LateShow
def is_time_in_range(start, end, x):
    # true if x is in range
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def send_message(output_message, receiver):
    if output_message != '':
        bot.sendMessage(receiver, output_message)
    # has a change to send a double message
    dice_roll = random.random()
    if dice_roll < 0.33:
        if output_message in complimenti:
            bot.sendMessage(receiver, 'Serio, no sfottò')
        elif output_message in offese:
            bot.sendMessage(receiver, 'Scherzo, sei un grande')


# a function that sends messages based on what time of the day it is
# CAREFUL, I am using two time formats here: to check which time of the day it is I am using
# -datetime- librabry, while to calculate elapsed time I am using -time- library
def time_based_messages(datetime_of_last_message, clock, chat):
    now = datetime.datetime.time(datetime.datetime.now())

    # if it's late in the night, has a small chance to ask 'Chi late?'
    start = datetime.time(1, 0, 0)
    end = datetime.time(3, 0, 0)
    if is_time_in_range(start, end, now):
        dice_roll = random.randint(1, int(14400/loop_cycle))
        if dice_roll == 1:
            bot.sendMessage(disservizi, 'Chi Late?')

    # if it's early in the morning, has a small chance to ask '7.54 qualcuno?'
    start = datetime.time(6, 30, 0)
    end = datetime.time(7, 30, 0)
    if is_time_in_range(start, end, now):
        dice_roll = random.randint(1, int(14400/loop_cycle))
        if dice_roll == 1:
            bot.sendMessage(disservizi, '7.54 qualcuno?')

    # if it's been a long time since someone wrote something, has a chance to write a message
    start = datetime.time(11, 0, 0)
    end = datetime.time(23, 0, 0)
    if is_time_in_range(start, end, now):
        # probability (every second) to send a message if nobody wrote anything in the last 30 minutes
        if time.time() - datetime_of_last_message < 30*60:
            probability = (1/99999999)*clock
        # probability (every second) to send a message if nobody wrote anything in the last hour
        elif time.time() - datetime_of_last_message < 60*60:
            probability = (1/100000)*clock
        # probability (every second) to send a message if nobody wrote anything in the last three hours
        elif time.time() - datetime_of_last_message < 180*60:
            probability = (1/40000)*clock
        # probability (every second) to send a message if nobody wrote anything in the last twelve hour
        else:
            probability = (1/20000)*clock

        inv_prob = int(1/probability)
        if inv_prob < 1:
            inv_prob = 1
        dice_roll = random.randint(1, inv_prob)
        if dice_roll == 1:
            output_message = random.choice(quotes + complimenti)
            send_message(output_message, chat)


# this function is used to choose a personalized message
def personalized_message(input_message, author):
    print(author)
    print('personalizing')

    # checks if the user who sent the message is in the dictionary "personalized_messages"
    personalized = False
    reply_to = ''

    for user in personalized_messages:
        if personalized_messages[user]['id'] == author:
        # if True:
            personalized = True
            reply_to = user

    print('ci siamo?')
    print(reply_to)
    print(personalized)
    print()

    # if the user is not in the dictionary, or it has no associated messages, just send a random message.
    # Otherwise choose appropriately
    if personalized is False or personalized_messages[reply_to]['messages'] == []:
        output_message = random.choice(quotes)
    else:
        output_message = random.choice(personalized_messages[reply_to]['messages'])
        print('1', output_message)

        # checks if the chosen message has already been sent recently to that user, if so chooses another one
        while output_message in personalized_messages[reply_to]['last_sent']:
            print('changing')
            if set(personalized_messages[reply_to]['messages']) <= set(personalized_messages[reply_to]['last_sent']):
                output_message = random.choice(quotes)
            else:
                # selects either a quote from the general list or one from the personal list
                dice_roll = random.random()
                if dice_roll < 60:
                    output_message = random.choice(personalized_messages[reply_to]['messages'])
                else:
                    output_message = random.choice(quotes)

        print('2', output_message)
        # updates 'last_sent' to only keep the last messages
        personalized_messages[reply_to]['last_sent'].append(output_message)
        personalized_messages[reply_to]['last_sent'] = personalized_messages[reply_to]['last_sent'][-5:]

    print('3', output_message)
    print('fin qui tutto ok?')
    # in some cases, based on who ZucaBot is replying to, sends special messages
    text = input_message['text'].lower()
    if reply_to == 'Zuca':
        # has a random chance to just repeat what Zuca said
        dice_roll = random.randint(1, 5)
        if dice_roll < 4:
            output_message = input_message['text']
    if reply_to == 'Leo':
        if text[-1] == '?':
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                output_message = 'Forse dovresti chiederlo a un costituzionalista'

    print('4', output_message)

    return output_message


# this is the function that will be called every time ZucaBot receives a new message
def interaction(received_message, chat, authors):
    global chain
    output_message = ''

    # try to see if the received message contains any text, if so interacts, otherwise do nothing
    try:
        text = received_message['text']

        try:
            # checks if the last 3 messages are the same (quindi siamo in una catena), if so reply the same
            if received_messages[-1]['message']['text'].lower() == received_messages[-2]['message']['text'].lower() and \
               received_messages[-2]['message']['text'].lower() == received_messages[-3]['message']['text'].lower():
                # checks if the last 3 messages were from different people
                if authors[-1] != authors[-2] and authors[-2] != authors[-3]:
                    # checks if ZucaBot already partecipated in that chain
                    if text != chain:
                        bot.sendMessage(chat, text)
                        chain = text
        except KeyError:
            pass

        lower_text = text.lower()
        # answer based on the text
        if 'russia' in text.lower():
            output_message = random.choice(russia)
        elif 'massimone' in text.lower():
            output_message = 'Papirone'
        elif 'papirone' in text.lower():
            output_message = 'Massimone'
        elif 'frau' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'Ebreo'
        elif 'scherzo' == text.lower():
            dice_roll = random.randint(1, 3)
            if dice_roll == 1:
                output_message = 'Sei un grande'
        elif 'grande' == text.lower():
            dice_roll = random.randint(1, 4)
            if dice_roll == 1:
                output_message = 'Sei uno scherzo'
        elif 'é' in text.lower() and 'ché' not in text.lower() and\
                'né' not in text.lower() and 'sé' not in text.lower():
            output_message = '*è'
        elif 'sè' in text.lower():
            output_message = '*sé'
        elif 'dò' in text.lower():
            output_message = '*do'
        elif "qual'è" in text.lower():
            output_message = '*qual è'
        elif "perchè" in text.lower():
            output_message = '*perché'
        elif 'italia' in text.lower() or 'lo stivale' in text.lower():
            dice_roll = random.randint(1, 5)
            if dice_roll == 1:
                output_message = 'Il paese che amk'
        elif 'ma ruffi' == text.lower() or 'ma luca' == text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                output_message = 'Dormivi?'
        elif 'togli zuca' in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                output_message = 'Stai buono'
        elif 'madre' in text or 'mamma' in text:
            if message['from']['id'] == personalized_messages['Miur']['id']:
                dice_roll = random.random()
                if dice_roll < 0.5:
                    output_message = random.choice(['Nuova questa Miur!',
                                                    'Miur, è dalla terza media che non fa ridere',
                                                    'La mamma dei Miur è sempre incinta'])
        elif 'salvini' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'considerato: cattivo'
        elif 'merkel' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'Considerata: buona'
        elif 'berlusconi' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'Considerato: cattivo'
        elif 'mussolini' in text.lower() or 'duce' in text.lower() or \
                        'ducie' in text.lower() or 'dux' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'Considerato: cattivo'
        elif 'trump' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'considerato: \ncattivo'
        elif 'erdogan' in text.lower() or 'tayyip' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'Considerato : \ncattivo'
        elif 'renzi' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = 'Considerato: buono'
        elif "ca" in text.lower() and "foscari" in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                output_message = "Ca' Fosfati"
        elif 'zuca, sei' in text.lower() or 'zuca sei' in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                output_message = "Ma che cazzo vuoi\nFallito di merda"
        elif 'boldrini' in text.lower():
            dice_roll = random.randint(1, 6)
            if dice_roll == 1:
                output_message = random.choice(['Considerata: buona',
                                                'Ceva cosa ne pensi della Boldrini?'])
        elif 'bebe' in text.lower() and 'vio' in text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                output_message = random.choice(['Sì, ma con le protesi',
                                                'Sì, ma senza protesi',
                                                'Con o senza protesi?'])
        elif 'hahaha' in text.lower() or 'ahhah' in text.lower() or 'rido' == text.lower():
            dice_roll = random.randint(1, 60)
            if dice_roll == 1:
                output_message = random.choice(['Ma cosa ridi deficiente?',
                                                "L'unica cosa che fa ridere è la tua vita",
                                                'Ridi ridi\ncoglione',
                                                'Non fa ridere, idiota',
                                                'Ridi perché ti sei guardato allo specchio?'])
        elif 'eh?' == text.lower():
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                output_message = 'Suca'
        elif 'dimmi' in text.lower() and 'zuca' in text.lower():
            output_message = random.choice(quotes)
        elif 'dicci' in text.lower() and 'zuca' in text.lower():
            output_message = random.choice(quotes)
        elif 'zuca' in text.lower():
            dice_roll = random.randint(1, 1)
            print('\n\n\n')
            print(dice_roll)
            if dice_roll == 1:
                output_message = personalized_message(received_message, authors[-1])
        # if nobody wants ZucaBot, send a message anyway with some probability
        else:
            dice_roll = random.randint(1, 60)
            if dice_roll == 1:
                output_message = personalized_message(received_message, authors[-1])

        send_message(output_message, chat)

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
    loop_cycle = 2  # number of seconds between loops
    time.sleep(loop_cycle)

    # variable that stores most recent messages
    received_messages = []
    authors = []
    for x in bot.getUpdates(offset=offset):
        try:
            check = x['message']
            received_messages.append(x)
            authors.append(x['message']['from']['id'])
        except KeyError:
            pass

    received_message = received_messages[-1]['message']
    # saves the ID of the chat who wrote the last message
    chat = received_messages[-1]['message']['chat']['id']
    # saves the ID of the last message
    received_message_id = received_messages[-1]['update_id']

    time_based_messages(last_message_datetime, loop_cycle, chat)

    # checks if ZucaBot received a new message
    if received_message != previous_message:

        # saves the time at which last message was received
        last_message_datetime = time.time()

        # interacts
        interaction(received_message, chat, authors)

        # prints information on the received message
        x = [print() for _ in range(10)]
        print('\n\n\n\n\n\n\n')
        print('NEW MESSAGE RECEIVED')
        for key in received_messages[-1]['message']:
            print(key)
            print('___________________', received_messages[-1]['message'][key])

        # discards the last message and gets ready to receive a new one
        previous_message = received_message
        offset = received_messages[-1]['update_id'] - 80  # only sees the last 80 messages
        if offset < 0:
            offset = 1
