# - *- coding: utf- 8 - *-
from config import token
from Google import gsearch
from Instagram import instsearch
from Twitter import twittersearch
import telebot

bot = telebot.TeleBot(token)

class Language:
    start = {'ukrainian':'''
👏 Привіт!

🤖 Цей бот створений для запитів з різних соцмереж за ключовим словом

📝 Спробуй ввести будь-яке слово  і ви отримаєте відповіді на цей запит із різних соцмереж 

''',
'english':
'''
👏 Hello!

🤖 This bot was made for searching queries in social networks

📝 Try to enter any word and you will get answers to this query from different social networks

''' }
    start2 = {'ukrainian':'''
🔄 Стартувати бота заново
''',
    'english':'''
🔄 Start bot again
'''}
    choiceforsearch = {'ukrainian':'''
📜 Виберіть соціальну мережу в якій ви бажаєте шукати інформацію по запиту, натиснувши на відповідну кнопку знизу
''',
    'english':'''
📜 Select the social network in which you want to search for information by clicking on the appropriate button below
'''}
    choiceforsearch2 = {'ukrainian':'''
📃 Виберіть джерело для пошуку: 
''',
  'english': '''
📃 Select a source for your search: 
'''}
    selectwritten = {'ukrainian':'''
⤴️ Вибрати вже написане слово
''',
  'english':'''
⤴️ Choose the word already written
'''}
    source = {'english':'''
🧾 Select a source for your search:
''',
  'ukrainian':'''
🧾 Виберіть джерело для пошуку:
'''}
    newword =  {'ukrainian':'''
🆕 Ввести нове слово
''',
  'english':'''
🆕 Enter a new word
'''}
    search = {'ukrainian':'''
🔍 Пошук в {} буде здійснюватись за словом/хештегом: 
''',
  'english':'''
🔍 {} will be searched by word / hashtag:
'''}
    wait10 = {'ukrainian':'''
Зачекайте ще 10 посилань за даним запитом в {}\nЦе займає деякий час ⌛
''',
  'english':'''
Wait for 10 more links for this query in {}\nIt takes some time ⌛
'''}
    wait = {'ukrainian':'''
Зачекайте ваш запит в {} обробляється.\nЦе займає деякий час ⌛
''',
  'english':'''
Wait for your {} request to be processed.\nIt takes some time ⌛
'''}
    click10 = {'ukrainian':'''
🖲️ Натисніть, для отримання ще 10 посилань
''',
  'english': '''
🖲️ Click to get 10 more links
'''}
    clicktochange = {'ukrainian':'''
🔃 Натисніть, для зміни джерела пошуку
''',
  'english': '''
🔃 Click to change the social network source
'''}
    writeword = {'ukrainian':'''
🖊 Напишіть слово за яким ви бажаєте шукати інформацію в {}
''',
  'english': '''
🖊 Type the word you want to use to search for information on {}
'''}
    choose = {'ukrainian':'''
🔘 Виберіть, який пошуковий запит ви збираєтесь використувати: 
''',
  'english': '''
🔘 Choose which search query you want to use:
'''}

keyboard2 = telebot.types.InlineKeyboardMarkup()
google = telebot.types.InlineKeyboardButton(text="Google",callback_data="google")
twitter = telebot.types.InlineKeyboardButton(text="Twitter",callback_data="twitter")
instagram = telebot.types.InlineKeyboardButton(text="Instagram",callback_data="instagram")
keyboard2.add(google)
keyboard2.add(twitter)
keyboard2.add(instagram)

keyboard7 = telebot.types.InlineKeyboardMarkup()
english = telebot.types.InlineKeyboardButton(text="🇬🇧 English", callback_data="english")
ukranian = telebot.types.InlineKeyboardButton(text="🇺🇦 Ukrainian", callback_data="ukrainian")
keyboard7.add(english)
keyboard7.add(ukranian)

def name(fn,ln):
    if fn and ln:
        ln = ' ' + ln
    if fn == None:
        fn = ''
    if ln == None:
        ln = ''
    return fn, ln


numbers = {}
choice = {}
users = {}
msg = {}
language = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    global choice
    choice.update({message.chat.id: None})
    global users
    users.update({message.chat.id: None})
    global language
    language.update({message.chat.id: None})
    bot.send_message(message.chat.id, text = Language.start['english'])
    bot.send_message(message.chat.id, text = 'Choose language: ', reply_markup=keyboard7)

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        if language[message.chat.id] == None:
            bot.send_message(message.chat.id, text = 'Choose language: ', reply_markup=keyboard7)
            return None
    except:
        bot.send_message(message.chat.id, 'Choose language: ', reply_markup=keyboard7)
        choice.update({message.chat.id: None})
        users.update({message.chat.id: None})
        return None
    try:
        if choice[message.chat.id] == None:
            bot.send_message(message.chat.id, text = choiceforsearchukr2 if language[message.chat.id] == 'ukrainian' else choiceforsearcheng2, reply_markup=keyboard2)
            return None
    except:
        bot.send_message(message.chat.id, Language.choiceforsearch[language[message.chat.id]], reply_markup=keyboard2)
        return None
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    bot.send_message(message.chat.id, '*{}{}*'.format(name(first_name, last_name)[0],name(first_name, last_name)[1]) +', ' +('з' + Language.wait[language[message.chat.id]][2:] if language[message.chat.id] == 'ukrainian' else 'w' + Language.wait[language[message.chat.id]][2:]).format(choice[message.chat.id].title()), parse_mode = 'Markdown')
    startsearch(message)
    msg.update({message.chat.id:message})
    
def startsearch(message, flag = 0):
    global keyboard1
    global keyboard3
    global keyboard5
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    key = telebot.types.InlineKeyboardButton(text=Language.click10[language[message.chat.id]],callback_data="googlesearch")
    switch = telebot.types.InlineKeyboardButton(text=Language.clicktochange[language[message.chat.id]], callback_data="switch")
    start = telebot.types.InlineKeyboardButton(text=Language.start2[language[message.chat.id]], callback_data="start")
    keyboard1.add(key)
    keyboard1.add(switch)
    keyboard1.add(start)

    keyboard3 = telebot.types.InlineKeyboardMarkup()
    key3 = telebot.types.InlineKeyboardButton(text=Language.click10[language[message.chat.id]], callback_data="twittersearch")
    keyboard3.add(key3)
    keyboard3.add(switch)
    keyboard3.add(start)

    keyboard5 = telebot.types.InlineKeyboardMarkup()
    key5 = telebot.types.InlineKeyboardButton(text=Language.click10[language[message.chat.id]], callback_data="instsearch")
    keyboard5.add(key5)
    keyboard5.add(switch)
    keyboard5.add(start)

    if flag == 1:
        bot.send_message(message.chat.id, (Language.wait[language[message.chat.id]]).format(choice[message.chat.id].title()))
    if choice[message.chat.id] == 'google':
        links = gsearch(message.text,1,1,language[message.chat.id])
        if links[:1] == '😢':
            bot.send_message(message.chat.id, links)
        else:
            bot.send_message(message.chat.id, links, reply_markup=keyboard1, disable_web_page_preview = True)
        
    elif choice[message.chat.id] == 'twitter':
        bot.send_message(message.chat.id, twittersearch(message.text, 1, language[message.chat.id]), reply_markup=keyboard3, disable_web_page_preview = True)
    elif choice[message.chat.id] == 'instagram':
        bot.send_message(message.chat.id, instsearch(message.text, 1,language[message.chat.id]),  reply_markup=keyboard5, disable_web_page_preview = True)
    
    users.update({message.chat.id : message.text})
    numbers.update({message.text: 2})
    
    

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'ukrainian':
        bot.send_message(call.message.chat.id, 'Ви вибрали 🇺🇦 українську мову для користування')
        bot.send_message(call.message.chat.id, Language.start['ukrainian'], reply_markup = keyboard2)
        language.update({call.message.chat.id: 'ukrainian'})
    if call.data == 'english':
        bot.send_message(call.message.chat.id, 'You choose 🇬🇧 English language')
        bot.send_message(call.message.chat.id, Language.choiceforsearch['english'], reply_markup=keyboard2)
        language.update({call.message.chat.id: 'english'})
    keyboard6 = telebot.types.InlineKeyboardMarkup()
    start = telebot.types.InlineKeyboardButton(text= Language.start2[language[call.message.chat.id]], callback_data="start")
    key6 = telebot.types.InlineKeyboardButton(text= Language.selectwritten[language[call.message.chat.id]], callback_data="Yes")
    key7 = telebot.types.InlineKeyboardButton(text= Language.newword[language[call.message.chat.id]], callback_data="No")
    switch = telebot.types.InlineKeyboardButton(text = Language.clicktochange[language[call.message.chat.id]], callback_data="switch")
    keyboard6.add(key6)
    keyboard6.add(key7)
    keyboard6.add(switch)
    keyboard6.add(start)
    if call.data == 'start':
        choice.update({call.message.chat.id: None})
        users.update({call.message.chat.id: None})
        language.update({call.message.chat.id: None})
        numbers.update({call.message.chat.id: None})
        msg.update({call.message.chat.id: None})
        bot.send_message(call.message.chat.id, text = Language.start['english'])
        bot.send_message(call.message.chat.id, text = 'Choose language: ', reply_markup=keyboard7)
    if call.data == 'Yes':
        bot.send_message(call.message.chat.id, (Language.search[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))
        bot.send_message(call.message.chat.id, text= users[call.message.chat.id])
        startsearch(msg[call.message.chat.id], flag = 1)
    
    if call.data == 'No':
        bot.send_message(call.message.chat.id, text= (Language.writeword[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))

    if call.data == 'switch':
        bot.send_message(call.message.chat.id, text = Language.source[language[call.message.chat.id]], reply_markup=keyboard2)

    if call.data == 'google':
        choice.update({call.message.chat.id: 'google'})
        if users[call.message.chat.id] == None: 
            bot.send_message(call.message.chat.id, text=(Language.choose[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))
        else:
            bot.send_message(call.message.chat.id, text = Language.choose[language[call.message.chat.id]], reply_markup=keyboard6)
    
    if call.data == 'twitter':
        choice.update({call.message.chat.id: 'twitter'})
        if users[call.message.chat.id] == None:  
            bot.send_message(call.message.chat.id, text=(Language.choose[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))
        else:
            bot.send_message(call.message.chat.id, text = Language.choose[language[call.message.chat.id]], reply_markup=keyboard6)

    if call.data == 'instagram':
        choice.update({call.message.chat.id: 'instagram'})
        if users[call.message.chat.id] == None: 
            bot.send_message(call.message.chat.id, text=(Language.choose[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))
        else:
            bot.send_message(call.message.chat.id, text = Language.choose[language[call.message.chat.id]], reply_markup=keyboard6)

    if call.data == 'googlesearch': 
        bot.send_message(call.message.chat.id, (Language.wait10[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))  
        bot.send_message(call.message.chat.id, gsearch(users[call.message.chat.id],1+10*(numbers[users[call.message.chat.id]]-1),1+10*(numbers[users[call.message.chat.id]]-1),language[call.message.chat.id]), reply_markup=keyboard1, disable_web_page_preview = True)
        numbers.update({users[call.message.chat.id]: numbers[users[call.message.chat.id]]+1})
    if call.data == 'instsearch':
        bot.send_message(call.message.chat.id, (Language.wait10[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))
        bot.send_message(call.message.chat.id, instsearch(users[call.message.chat.id],numbers[users[call.message.chat.id]],language[call.message.chat.id]), reply_markup=keyboard5, disable_web_page_preview = True)
        numbers.update({users[call.message.chat.id]: numbers[users[call.message.chat.id]]+1})
    if call.data == 'twittersearch':
        bot.send_message(call.message.chat.id, (Language.wait10[language[call.message.chat.id]]).format(choice[call.message.chat.id].title()))
        bot.send_message(call.message.chat.id, twittersearch(users[call.message.chat.id],numbers[users[call.message.chat.id]],language[call.message.chat.id]), reply_markup=keyboard3, disable_web_page_preview = True)
        numbers.update({users[call.message.chat.id]: numbers[users[call.message.chat.id]]+1})

if __name__ == '__main__':
    bot.polling(none_stop=True)