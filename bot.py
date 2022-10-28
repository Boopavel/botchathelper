import telebot
from telebot import types
import random
import time
import json
import os
import datetime
import pytz
import shutil
import pyowm
#token = '5342339411:AAFaBZmwXM8R11NWRwmDfdxepUd8kA_Cplo'
token="5457377018:AAHfoJ8J1exMNvRaO_WmT2agBgMjbKpFxQM"
bot = telebot.TeleBot(token, threaded=False)
owm=pyowm.OWM('d6fb251ddd6133841dbf6fab3da374b1')
mgr = owm.weather_manager()
"""
##admin= "-1001224226468" #admin group
#admin="-1001757776685" #test group
admin="-1001617137939" #new admin group
jbchat="-1001159325248" #jb chat
#jbchat="-1001586786891" #new chat
d = open("admins.txt", "r")

admins=eval(d.read())

f = open("warns.txt", "r")
warns=eval(f.read())
ff=open("users.txt","r")
users=eval(ff.read())
ghb=open("unreg.txt","r")
unreg=eval(ghb.read())
bolt=open("boltun.txt","r")
boltun=eval(bolt.read())
gamess=open("gamee.txt","r")
gam=int(gamess.read())
almaz=open("almaz.txt","r")
alm=eval(almaz.read())

"""
admset={}
#bot.send_message(525721349, "Бот запущен")
rf=None
gf=None
settingss={}
truewritewelcome={}
truewriterules={}
ca=[]
@bot.callback_query_handler(func=lambda call: True)
def setings(call):
    global settingss,turewritewelcome,truewriterules,ca
    if call.data == "no":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "⛔️ НАСТРОЙКА БОТА ОТМЕНЕНА!!")
    if call.data == "yes":
        bot.delete_message(call.message.chat.id, call.message.message_id)

        sr=bot.send_message(call.message.chat.id, "⌛️ Производится настройка")
        os.mkdir(str(call.message.chat.id))
        os.mkdir(str(call.message.chat.id)+"/warns")
        #f=open(str(call.message.chat.id)+"/admins.txt","w")
        #f.write("['"+call.from_user.username+"']")
        #f.close()

        f=open(str(call.message.chat.id)+"/almaz.txt","w")
        f.write("")
        f.close()


        f=open(str(call.message.chat.id)+"/game.txt","w")
        f.write("0")
        f.close()

        f=open(str(call.message.chat.id)+"/rules.txt","w")
        f.write("")
        f.close()

        f=open(str(call.message.chat.id)+"/welcome.txt","w")
        f.write("")
        f.close()

        f=open(str(call.message.chat.id)+"/weather.txt","w")
        f.write("")
        f.close()


        f=open(str(call.message.chat.id)+"/adminstatus.txt","w")
        f.write("")
        f.close()

        f=open(str(call.message.chat.id)+"/adminchat.txt","w")
        f.write("")
        f.close()

        f=open(str(call.message.chat.id)+"/gamestatus.txt","w")
        f.write("")
        f.close()

        f=open(str(call.message.chat.id)+"/warnstatus.txt","w")
        f.write("")
        f.close()


        bot.edit_message_text(chat_id=sr.chat.id, message_id=sr.message_id, text="✅️ БОТ НАСТРОЕН\n\nТеперь к нему можно обращаться для настройки тут /settings️")






    if call.data == "👋 Приветствие":
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='👀 Посмотреть, то которое сейчас есть', callback_data="readwelcome")
        ke = types.InlineKeyboardButton(text='🛃 Записать новое', callback_data="writewelcome")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Вы выбрали настройку приветствия в группе</b>\n\nПриветствие, это такое событие, когда я автоматически фиксирую то что в группу заходит новый человек и выдаю заранее готовый текст по шаблону.\n\n<b>Как подставить свои значения???</b>\n<code>{0}</code> - Имя, которое отображается у всех\n<code>{1}</code> - Фамилия которая отображается у всех. \n\nВыбери действие кнопками ниже",parse_mode="HTML",reply_markup=kb)
    if call.data == "readwelcome":
        try:
            e=settingss[str(call.from_user.id)]
            f=open(str(e.chat.id)+"/welcome.txt","r")
            er=f.read()
            kb = types.InlineKeyboardMarkup(row_width=2)
            #k = types.InlineKeyboardButton(text='👀 Посмотреть, то которое сейчас есть', callback_data="readwelcome")
            ke = types.InlineKeyboardButton(text='🛃 Записать новое', callback_data="writewelcome")
            key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="👋 Приветствие")
            kb.add(ke)
            kb.add(key)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Приветствие</b>\n\n<em>"+str(er)+"</em>",parse_mode="HTML",reply_markup=kb)
            f.close()
        except Exception as e:
            bot.reply_to(call.message, str(e))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="⚠️Произошла ошибка. \n💡Вот возможные причины:\n\n•Вы не использовали команду /register!\n•Нету приветствия\n\nИли обратитесь в службу поддержки @chaatme_bot")
    if call.data == "truewritewelcome":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/welcome.txt","w")
        f.write(str(truewritewelcome[str(call.from_user.id)]))
        f.close()
        del truewritewelcome[str(call.from_user.id)]
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='👀 Посмотреть приветствие, то которое сейчас есть', callback_data="readwelcome")
        ke = types.InlineKeyboardButton(text='🛃 Записать новое приветствие', callback_data="writewelcome")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="👋 Приветствие")
        kb.add(k)
        kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="✅️Готово\nЯ заменил приветствие в чате <b>"+str(e.chat.title)+"</b>",parse_mode="HTML",reply_markup=kb)
    if call.data == "writewelcome":
        def rt(message):
            global settingss, truewritewelcome
            e=settingss[str(message.from_user.id)]
            f=open(str(e.chat.id)+"/welcome.txt","r")
            kb = types.InlineKeyboardMarkup(row_width=2)
            ke = types.InlineKeyboardButton(text='✅️ Да', callback_data="truewritewelcome")
            key = types.InlineKeyboardButton(text='🤔 Нет, я передумал(а)', callback_data="👋 Приветствие")
            kb.add(ke)
            kb.add(key)

            mes="<b>Вы собираетесь изменить приветствие</b>\nЭтот процес нельзя отменить, проверьте что все правильно.\n\nБыло:\n<em>"+str(f.read())+"</em>\n\nСтанет:\n<em>"+str(message.text)+"</em>\n\nВЫ УВЕРЕНЫ?!"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=mes,parse_mode="HTML",reply_markup=kb)
            truewritewelcome[str(call.from_user.id)]=message.text

        kb = types.InlineKeyboardMarkup(row_width=2)
        ke = types.InlineKeyboardButton(text='👀 Посмотреть, то которое сейчас есть', callback_data="readwelcome")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(ke)
        kb.add(key)
        ers=bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Приветствие</b>\n\nЗапишите тут приветствие, которе будет в группе. Или можете вернуться назад:)\nПоддерживается HTML",parse_mode="HTML",reply_markup=kb)
        bot.register_next_step_handler(ers, rt)
    if call.data == "backtohome":
        message=call.message
        message.from_user.id=call.from_user.id
        e=settingss[str(call.from_user.id)]
        message.chat.title=e.chat.title
        #bot.delete_message(message.chat.id, message.message_id)
        settings(message)

    if call.data == "☀️ Погода с сервиса OpenWeatherMap":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/weather.txt","r")
        bla=f.read()
        if bla == "true":
            bla="✅️ ВКЛ"
        else:
            bla="🚫 ВЫКЛ"
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="weatheron")
        ke = types.InlineKeyboardButton(text='🚫 ВЫКЛ', callback_data="weatheroff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Погода</b>\n\nВо мне есть встроенная функция для получения погоды.\nЯ использую OpenWeatherMap.\n\nЧтобы получить погоду, можно написать <code>погода Киев</code> к примеру.\n\nСейчас статус этой погоды: "+bla+"\nВыберите, нужно ли вам включить это или нет",parse_mode="HTML",reply_markup=kb)
    if call.data == "weatheron":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/weather.txt","w")
        f.write("true")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="weatheron")
        ke = types.InlineKeyboardButton(text='🚫 ВЫКЛ', callback_data="weatheroff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Погода</b>\n\nВо мне есть встроенная функция для получения погоды.\nЯ использую OpenWeatherMap.\n\nЧтобы получить погоду, можно написать <code>/weather Киев</code> к примеру.\n\nСейчас статус этой погоды: ✅️ ВКЛ\nВыберите, нужно ли вам включить это или нет",parse_mode="HTML",reply_markup=kb)

    if call.data == "weatheroff":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/weather.txt","w")
        f.write("")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="weatheron")
        ke = types.InlineKeyboardButton(text='🚫 ВЫКЛ', callback_data="weatheroff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Погода</b>\n\nВо мне есть встроенная функция для получения погоды.\nЯ использую OpenWeatherMap.\n\nЧтобы получить погоду, можно написать <code>/weather Киев</code> к примеру.\n\nСейчас статус этой погоды: 🚫 ВЫКЛ\nВыберите, нужно ли вам включить это или нет",parse_mode="HTML",reply_markup=kb)


    if call.data == "📃 Правила":
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='👀 Посмотреть, те которые сейчас есть', callback_data="readrules")
        ke = types.InlineKeyboardButton(text='🛃 Записать новые', callback_data="writerules")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Вы выбрали настройку правил в группе</b>\n\nПравила чата это четко устанновленные разрешенные и запрещенные действия в чате.\n\nВыбери действие кнопками ниже",parse_mode="HTML",reply_markup=kb)

    if call.data == "readrules":
        try:
            e=settingss[str(call.from_user.id)]
            f=open(str(e.chat.id)+"/rules.txt","r")
            er=f.read()
            kb = types.InlineKeyboardMarkup(row_width=2)
            #k = types.InlineKeyboardButton(text='👀 Посмотреть, то которое сейчас есть', callback_data="readwelcome")
            ke = types.InlineKeyboardButton(text='🛃 Записать новые', callback_data="writerules")
            key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="📃 Правила")
            kb.add(ke)
            kb.add(key)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Правила</b>\n\n<em>"+str(er)+"</em>",parse_mode="HTML",reply_markup=kb)
            f.close()
        except Exception as e:
            bot.reply_to(call.message, str(e))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="⚠️Произошла ошибка. \n💡Вот возможные причины:\n\n•Вы не использовали команду /register!\n•Нету правил\n\nИли обратитесь в службу поддержки @chaatme_bot")

    if call.data == "truewriterules":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/rules.txt","w")
        f.write(str(truewriterules[str(call.from_user.id)]))
        f.close()
        del truewriterules[str(call.from_user.id)]
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='👀 Посмотреть правила, те которые сейчас есть', callback_data="readrules")
        ke = types.InlineKeyboardButton(text='🛃 Записать новые правила', callback_data="writerules")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="📃 Правила")
        kb.add(k)
        kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="✅️Готово\nЯ заменил правила в чате <b>"+str(e.chat.title)+"</b>",parse_mode="HTML",reply_markup=kb)
    if call.data == "writerules":
        def rt(message):
            global settingss, truewriterules
            e=settingss[str(message.from_user.id)]
            f=open(str(e.chat.id)+"/rules.txt","r")
            kb = types.InlineKeyboardMarkup(row_width=2)
            ke = types.InlineKeyboardButton(text='✅️ Да', callback_data="truewriterules")
            key = types.InlineKeyboardButton(text='🤔 Нет, я передумал(а)', callback_data="📃 Правила")
            kb.add(ke)
            kb.add(key)

            mes="<b>Вы собираетесь изменить правила чата</b>\nЭтот процес нельзя отменить, проверьте что все правильно.\n\nБыло:\n<em>"+str(f.read())+"</em>\n\nСтанет:\n<em>"+str(message.text)+"</em>\n\nВЫ УВЕРЕНЫ?!"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=mes,parse_mode="HTML",reply_markup=kb)
            truewriterules[str(call.from_user.id)]=message.text

        kb = types.InlineKeyboardMarkup(row_width=2)
        ke = types.InlineKeyboardButton(text='👀 Посмотреть, те которые сейчас есть', callback_data="readrules")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(ke)
        kb.add(key)
        ers=bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Правила</b>\n\nЗапишите тут правила, которые будут в группе. Или можете вернуться назад:)\nПоддерживается HTML",parse_mode="HTML",reply_markup=kb)
        bot.register_next_step_handler(ers, rt)


    if call.data == "❓️ Список команд для бота":
        kb = types.InlineKeyboardMarkup(row_width=2)
        #k = types.InlineKeyboardButton(text='', callback_data="readrules")
        ke = types.InlineKeyboardButton(text='❔️ Ничего не понятно, написать в поддержку', url="https://t.me/chaatme_bot")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Вы выбрали список команд для бота</b>\n\n<em>Команды, которые в личных сообщениях нужно использовать:</em>\n/start - перезапустить бота\n\n<em>Команды, которые в чате нужно использовать:</em>\n/register - Первоначальная настройка бота в чате(только для администраторов)\n/settings - Настройки бота(только для администраторов)\n/mute sec - выключить звук человеку в секундах(только для администраторов)\n/kick - выгнать/забанить человека(только для администраторов)\n/warn why - дается предупреждение человеку, можно дописать причину(только для администраторов)\n/rules - правила чата\nпогода город - получает данные о погоде\n/game - счетчик игр в чате\n/admin - вызов админов",parse_mode="HTML",reply_markup=kb)



    if call.data == "close":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        try:
            del truewritewelcome[str(call.from_user.id)]
        except:
            pass
        try:
            del truewriterules[str(call.from_user.id)]
        except:
            pass
        try:
            del settingss[str(call.from_user.id)]
        except:
            pass
        try:
            del ca[str(call.from_user.id)]
        except:
            pass



    if call.data == "🆘️ Настройка команды и админ чата":
        #print("true")
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='📴 Управление статусом', callback_data="onoffadmin")
        ke = types.InlineKeyboardButton(text='📶 Настройка чата для администраторов', callback_data="adminchat")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        #kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Вы выбрали настройку команды /admin</b>\n\nЭта команда позволяет участникам вызвать администраторов чата, если что-то произошло в чате.\nТут Вы можете настроить будет ли работать эта команда, и админ-группу",parse_mode="HTML",reply_markup=kb)

    if call.data == "onoffadmin":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/adminstatus.txt","r")
        bla=f.read()
        if bla == "true":
            bla="✅️ ВКЛ"
        else:
            bla="❌️ ВЫКЛ"
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="adminon")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="adminoff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Статус команды /admin</b>\n\n❓️Для чего нужно это меню?\n<em>Это меню нужно для ограничения использования команды вызова администрации чата</em>\n\nВыберите, нужно ли Вам это\n<b>СТАТУС:</b> "+bla,parse_mode="HTML",reply_markup=kb)

    if call.data == "adminon":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/adminstatus.txt","w")
        f.write("true")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="adminon")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="statusoff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Статус команды /admin</b>\n\n❓️Для чего нужно это меню?\n<em>Это меню нужно для ограничения использования команды вызова администрации чата</em>\n\nВыберите, нужно ли Вам это\n<b>СТАТУС:</b> ✅️ ВКЛ",parse_mode="HTML",reply_markup=kb)

    if call.data == "adminoff":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/adminstatus.txt","w")
        f.write("")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="adminon")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="adminoff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Статус команды /admin</b>\n\n❓️Для чего нужно это меню?\n<em>Это меню нужно для ограничения использования команды вызова администрации чата</em>\n\nВыберите, нужно ли Вам это\n<b>СТАТУС:</b> ❌️ ВЫКЛ",parse_mode="HTML",reply_markup=kb)

    mail(call)
    if call.data == "adminchat":
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='🛃 Отправить сообщение в общий чат', callback_data="autoadmin")
        ke = types.InlineKeyboardButton(text='🔧 Вручную прописать айди чата администраторов(для опытных)', callback_data="manualadmin")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="🆘️ Настройка команды и админ чата")
        kb.add(ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Настройка чата администраторов</b>\n\n❓️Как настроить чат для администраторов???\n<em>Сейчас, после того как Вы нажмете на кнопку, бот отправит сообщение с кодом в общий чат. Ваша задача добавить бота с админ правами в чат администраторов без /register и переслать туда сообщение с кодом от бота</em>",parse_mode="HTML",reply_markup=kb)


    if call.data == "manualadmin":
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='🛃 Отправить сообщение в общий чат', callback_data="autoadmin")
        #ke = types.InlineKeyboardButton(text='🔧 Вручную прописать айди чата администраторов(для опытных)', callback_data="manualadmin")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="adminchat")
        #kb.add(k)
        kb.add(key)
        def ew(message):
            global settingss
            try:
               bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id-1, text="<b>Настройка чата администраторов. Внос чата администрации вручную</b>\n\nЯ получил айди:\n<em>"+str(message.text)+"</em>\n\nЯ отправляю сообщение в этот чат, если все работает, дальнейшие действия будут там. Иначе тут",parse_mode="HTML")
               bot.send_message(message.text, "Проверка, проверка!\n✅️Эта группа успешно подключена к чату администратором "+str(message.from_user.first_name))
               e=settingss[str(message.from_user.id)]
               f=open(str(e.chat.id)+"/adminchat.txt","w")
               f.write(str(message.text))
               f.close()

               bot.delete_message(message.chat.id, message.message_id)

            except Exception as e:
                kb = types.InlineKeyboardMarkup(row_width=2)
                k = types.InlineKeyboardButton(text='🛃 Отправить сообщение в общий чат', callback_data="autoadmin")
                #ke = types.InlineKeyboardButton(text='🔧 Вручную прописать айди чата администраторов(для опытных)', callback_data="manualadmin")
                key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="adminchat")
                #kb.add(k)
                kb.add(key)

                bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id-1, text="<b>Настройка чата администраторов. Внос чата администрации вручную</b>\n\nЯ получил айди:\n<em>"+str(message.text)+"</em>\n\nЯ не смог отправить сообщение, проверьте еще раз",parse_mode="HTML",reply_markup=kb)
                #bot.reply_to(message, str(e))
        we=bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Настройка чата администраторов. Внос чата администрации вручную</b>\n\nОтправьте мне айди чата администрации. Айди можно узнать во мне командой /id, я должен состоять в чате администрации и быть с правами админа! Я отправлю тестовое сообщение в тот чат, если все работает, значит настроили. Погнали)",parse_mode="HTML",reply_markup=kb)
        bot.register_next_step_handler(we,ew)


    if call.data == "autoadmin":
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='🔧 Вручную прописать айди чата администраторов(для опытных)', callback_data="manualadmin")
        #ke = types.InlineKeyboardButton(text='🔧 Вручную прописать айди чата администраторов(для опытных)', callback_data="manualadmin")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="adminchat")
        kb.add(k)
        kb.add(key)
        e=settingss[str(call.from_user.id)]
        bot.send_message(e.chat.id, "/adminchatautosetup Это сообщение для настройки админ чата.\nКод: "+str(e.chat.id))
        ca.append(e.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Настройка чата администраторов. Внос чата администрации автоматически</b>\n\nЯ отправил сообщение с кодом в общий чат, перешлите его в админ-чат где я администратор и не использовалась /register",parse_mode="HTML",reply_markup=kb)



    if call.data == "🎮 Счетчик игр":
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='📴 Управление статусом', callback_data="statusgame")
        ke = types.InlineKeyboardButton(text='▶️ Управление количеством игр', callback_data="kolgame")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        #kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Вы выбрали настройку команды /game</b>\n\nЭта команда позволяет считать игры в чате. Допустим если есть в чате мафия, это очень пригодится\nТут Вы можете настроить будет ли работать эта команда, и изменить количество игр",parse_mode="HTML",reply_markup=kb)

    if call.data == "statusgame":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/gamestatus.txt","r")
        bla=f.read()
        if bla == "true":
            bla="✅️ ВКЛ"
        else:
            bla="❌️ ВЫКЛ"
        f.close()

        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="ongame")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="offgame")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="🎮 Счетчик игр")
        kb.add(k,ke)
        #kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Настройка статуса команды /game</b>\n\nТут Вы можете настроить будет ли работать эта команда\n\n<b>СТАТУС:</b> "+bla,parse_mode="HTML",reply_markup=kb)

    if call.data == "ongame":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/gamestatus.txt","w")
        f.write("true")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="ongame")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="offgame")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="🎮 Счетчик игр")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Настройка статуса команды /game</b>\n\nТут Вы можете настроить будет ли работать эта команда\n\n<b>СТАТУС:</b> ✅️ ВКЛ",parse_mode="HTML",reply_markup=kb)

    if call.data == "offgame":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/gamestatus.txt","w")
        f.write("")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="ongame")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="offgame")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="🎮 Счетчик игр")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Настройка статуса команды /game</b>\n\nТут Вы можете настроить будет ли работать эта команда\n\n<b>СТАТУС:</b> ❌️ ВЫКЛ",parse_mode="HTML",reply_markup=kb)

    if call.data=="kolgame":
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb_dog = types.InlineKeyboardButton(text='+1', callback_data='plusgame')
        kb_cat = types.InlineKeyboardButton(text='-1', callback_data='minusgame')
        kb_mouse = types.InlineKeyboardButton(text='✅️Пускай так будет', callback_data='🎮 Счетчик игр')
        kb.add(kb_dog, kb_cat, kb_mouse)
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/game.txt","r")
        numofgame=f.read()
        f.close()

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас игр столько: "+numofgame+"\nХотите изменить?",reply_markup=kb)

    if call.data=="plusgame":
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb_dog = types.InlineKeyboardButton(text='+1', callback_data='plusgame')
        kb_cat = types.InlineKeyboardButton(text='-1', callback_data='minusgame')
        kb_mouse = types.InlineKeyboardButton(text='✅️Пускай так будет', callback_data='🎮 Счетчик игр')
        kb.add(kb_dog, kb_cat, kb_mouse)
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/game.txt","r")
        numofgame=f.read()
        f.close()

        f=open(str(e.chat.id)+"/game.txt","w")
        f.write(str(int(numofgame)+1))
        f.close()
        numofgame=int(numofgame)+1

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас игр столько: "+str(numofgame)+"\nХотите изменить?",reply_markup=kb)

    if call.data=="minusgame":
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb_dog = types.InlineKeyboardButton(text='+1', callback_data='plusgame')
        kb_cat = types.InlineKeyboardButton(text='-1', callback_data='minusgame')
        kb_mouse = types.InlineKeyboardButton(text='✅️Пускай так будет', callback_data='🎮 Счетчик игр')
        kb.add(kb_dog, kb_cat, kb_mouse)
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/game.txt","r")
        numofgame=f.read()
        f.close()

        f=open(str(e.chat.id)+"/game.txt","w")
        f.write(str(int(numofgame)-1))
        f.close()

        numofgame=int(numofgame)+1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас игр столько: "+str(numofgame)+"\nХотите изменить?",reply_markup=kb)

    if call.data == "🇬🇧 Язык бота":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Эта функция будет позже")

    if call.data == "❗️ Предупреждение":
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='📴 Управление статусом', callback_data="statuswarn")
        ke = types.InlineKeyboardButton(text='🛃 Снять варны у всех', callback_data="nowarn")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="backtohome")
        kb.add(k,ke)
        #kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Вы выбрали настройку предупреждений</b>\n\nС помощью этих предупреждений вы можете обезвредить нарушителя в чате\nТут Вы можете настроить будут ли работать эти предупреждения, и снять их у всех",parse_mode="HTML",reply_markup=kb)


    if call.data == "nowarn":
        e=settingss[str(call.from_user.id)]
        shutil.rmtree(str(e.chat.id)+"/warns")
        os.mkdir(str(e.chat.id)+"/warns")
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='📴 Управление статусом', callback_data="statuswarn")
        # ke = types.InlineKeyboardButton(text='🛃 Снять варны у всех', callback_data="nowarn")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="❗️ Предупреждение")
        kb.add(k)
        #kb.add(ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Сброс ВСЕХ предупреждений</b>\n\n✅️Успешно удалены все предупреждения в чате",parse_mode="HTML",reply_markup=kb)


    if call.data == "statuswarn":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/warnstatus.txt","r")
        bla=f.read()
        if bla == "true":
            bla="✅️ ВКЛ"
        else:
            bla="❌️ ВЫКЛ"
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="warnon")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="warnoff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="❗️ Предупреждение")
        kb.add(k,ke)
        kb.add(key)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Статус предупреждений</b>\n\n❓️Для чего нужно это меню?\n<em>Это меню нужно для ограничения использования предупреждений</em>\n\nВыберите, нужно ли Вам это\n<b>СТАТУС:</b> "+bla,parse_mode="HTML",reply_markup=kb)

    if call.data == "warnon":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/warnstatus.txt","w")
        f.write("true")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="warnon")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="warnoff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="❗️ Предупреждение")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Статус предупреждений</b>\n\n❓️Для чего нужно это меню?\n<em>Это меню нужно для ограничения использования предупреждений</em>\n\nВыберите, нужно ли Вам это\n<b>СТАТУС:</b> ✅️ ВКЛ",parse_mode="HTML",reply_markup=kb)

    if call.data == "warnoff":
        e=settingss[str(call.from_user.id)]
        f=open(str(e.chat.id)+"/warnstatus.txt","w")
        f.write("")
        f.close()
        kb = types.InlineKeyboardMarkup(row_width=2)
        k = types.InlineKeyboardButton(text='✅️ ВКЛ', callback_data="warnon")
        ke = types.InlineKeyboardButton(text='❌️ ВЫКЛ', callback_data="warnoff")
        key = types.InlineKeyboardButton(text='🔙 Назад', callback_data="❗️ Предупреждение")
        kb.add(k,ke)
        kb.add(key)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Статус предупреждений</b>\n\n❓️Для чего нужно это меню?\n<em>Это меню нужно для ограничения использования предупреждений</em>\n\nВыберите, нужно ли Вам это\n<b>СТАТУС:</b> ❌️ ВЫКЛ",parse_mode="HTML",reply_markup=kb)

@bot.message_handler(commands=["start"])
def chstart(message):
    if message.chat.type == "private":
        start(message)
def start(message):
    bot.delete_message(message.chat.id, message.message_id)
    kbb = types.InlineKeyboardMarkup(row_width=1)
    kb_mouse = types.InlineKeyboardButton(text='Напиши шефу тут', url="https://t.me/chaatme_bot")
    #hb= types.InlineKeyboardButton(text="Добавить меня в группу", add)
    kbb.add(kb_mouse)

    bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b>!\n\nМеня зовут Chathelper, приятно познакомиться. Я бот для более удобной модерации в чатах Telegram, если возникают вопросы, Вы всегда можете связаться со мной через кнопку ниже.\nДля начала добавь меня в группу и настрой меня чтобы я показал себя во всей красе.\n\n<em>ПРЕДУПРЕЖДАЮ СРАЗУ! Я НЕДАВНО РОДИЛСЯ И МОГУ РАБОТАТЬ ЕЩЕ НЕСТАБИЛЬНО, ЕСЛИ БУДУТ БАГИ, ЛУЧШЕ ПИШИТЕ МОЕМУ ШЕФУ ЧЕРЕЗ КНОПКУ НИЖЕ</em>",parse_mode="HTML", reply_markup=kbb)

@bot.message_handler(commands=["settings"])
def chsettings(message):
    global settingss
    try:
        if message.chat.type == "private":
            bot.reply_to(message, "⛔️ Запустите настройки из группы где Вы являетесь администратором")
        else:
            #f=open(str(message.chat.id)+"/admins.txt","r")
            #ds=eval(f.read())
            #f.close()
            ew=bot.get_chat_member(message.chat.id, message.from_user.id)
            status = ["administrator","creator"]
            if str(ew.status) in status:
                settingss[str(message.from_user.id)]=message

                settings(message)
            else:
                bot.reply_to(message, "⚠️У Вас нету прав для настроек бота.\n\nЕсли Вы считаете что это ошибка, свяжитесь с админами")
    except telebot.apihelper.ApiTelegramException as e:
        if str(e) == "A request to the Telegram API was unsuccessful. Error code: 400. Description: Bad Request: message can't be deleted":
            bot.reply_to(message, "⛔️ Вы еще не дали права администратора мне, дайте мне полные права для корректной работы")
def settings(message):
    global settingss
    bot.delete_message(message.chat.id, message.message_id)
    parame=["🎮 Счетчик игр","🇬🇧 Язык бота","☀️ Погода с сервиса OpenWeatherMap","👋 Приветствие","📃 Правила","🆘️ Настройка команды и админ чата","❗️ Предупреждение","❓️ Список команд для бота"]
    kbb = types.InlineKeyboardMarkup(row_width=2)
    g=0
    gt=[]
    for i in parame:
        if i in gt:
            pass
        else:
            g=g+1
            kb_mouse = types.InlineKeyboardButton(text=str(i), callback_data=str(i))
            gt.append(i)
            if g < len(parame):
                if parame[g] in parame:
                    g=g+1
            try:
                kb = types.InlineKeyboardButton(text=parame[g], callback_data=parame[g])
                kbb.add(kb_mouse,kb)
                gt.append(parame[g])
            except:
                kbb.add(kb_mouse)
    kb_mouse = types.InlineKeyboardButton(text="✅️ Закрыть", callback_data="close")
    kbb.add(kb_mouse)
    bot.send_message(message.from_user.id, "🔧Настройки группы <b>"+message.chat.title+"</b>",parse_mode="HTML", reply_markup=kbb)
#@bot.callback_query_handler(func=lambda call: True)
#def setup(call):

@bot.message_handler(commands=["register"])
def register(message):
    ew=bot.get_chat_member(message.chat.id, message.from_user.id)
    #bot.reply_to(message, str(ew.status))
    #ds=bot.get_chat_administrators(message.chat.id)
    #e=ds[0]
    if str(ew.status) == "creator" or str(ew.status) == "administrator":
        kbb = types.InlineKeyboardMarkup(row_width=1)
        kb_mouse = types.InlineKeyboardButton(text='✅️ ДА!', callback_data='yes')
        hb= types.InlineKeyboardButton(text="🚫 НЕТ, Я ПЕРЕДУМАЛ(А)", callback_data="no")
        kbb.add(kb_mouse,hb)
        bot.reply_to(message, "❓️Вы уверены что хотите настроить бота для чата???", reply_markup=kbb)
    else:
        bot.reply_to(message, "🚫 У ВАС НЕТ ПРАВ")

@bot.message_handler(commands=["mute"])
def mute(message):
    global admins,admin
    if message.from_user.username in admins:
        bot.delete_message(message.chat.id, message.message_id)
        message.message_id=message.reply_to_message.message_id
        if len(message.text.split("/mute ")) == 2:
            mut=message.text.split("/mute ")
            tme=mut[-1]
            mut=time.time()+int(mut[-1])
        else:
            mut=time.time()+3600
            tme=3600
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=mut)
        bot.reply_to(message, "🔇Пользователь <a href='tg://user?id="+str(message.reply_to_message.from_user.id)+"'>"+message.reply_to_message.from_user.first_name+"</a> был обеззвучен\n\n<b>Длительность наказания</b>: "+str(tme)+" секунд",parse_mode="HTML")
        bot.send_message(admin, "🔇Пользователь <a href='tg://user?id="+str(message.reply_to_message.from_user.id)+"'>"+message.reply_to_message.from_user.first_name+"</a> был обеззвучен\n\n<b>Длительность наказания</b>: "+str(tme)+" секунд",parse_mode="HTML")
@bot.message_handler(commands=["rules"])
def rules(message):
    f=open(str(message.chat.id)+"/rules.txt","r")
    bot.reply_to(message, str(f.read()), parse_mode="HTML")
@bot.message_handler(commands=["id"])
def i(message):
    bot.reply_to(message, "user id: "+str(message.from_user.id)+"\nchat id: "+str(message.chat.id)+"\nmessage id: "+str(message.message_id))
def kick(message, ban):
	global admin
	bot.ban_chat_member(message.chat.id, ban)
	bot.send_message(message.chat.id, "Был кик...")
	bot.send_message(admin, "!!!Был кик в чате")
'''@bot.message_handler(commands=["ban"])
def baaan(message):
    global admins
    bot.delete_message(message.chat.id, message.message_id)
    bot.kick_chat_member(message.chat.id, "-1001723238555")
    ''' '''if message.from_user.username in admins:
        mgs=message.text.lower()
        ban=mgs.split("/ban")
        kick(message, str(ban[1]))
        bot.send_message(message.chat.id, "Был кикнут пользователь/канал вручную по айди: "+ban[1])'''
@bot.message_handler(commands=["game"])
def spu(message):
    f=open(str(message.chat.id)+"/gamestatus.txt","r")
    e=f.read()
    f.close()
    if e == "true":
        gamee(message)
    else:
        bot.reply_to(message, "⚠️Счетчик игр отключен администраторами этой группы, игра не засчитана")
def gamee(message):
    #global gam

    f=open(str(message.chat.id)+"/game.txt","r")
    gam=int(f.read())+1
    bot.send_message(message.chat.id, "🎮запущена игра.\n\n№ игры: "+str(gam))
    gggm=open(str(message.chat.id)+"/game.txt","w")
    gggm.write(str(gam))
    f.close()
    gggm.close()
#@bot.message_handler(commands=["start"])
#def notallowed(message):
#	if message.chat.type == "private":
#		bot.delete_message(message.chat.id, message.message_id)
#		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEFgmVi8haL4FAcV8KGVib_vCNHLCYKyAACnh8AAnSRAUn1Wtr3Std48ykE")
#		bot.send_message(message.chat.id, "Этот бот не может использоваться в личных сообщениях.\n\nThis bot cannot use in private messages.")
#	else:
#	    bot.reply_to(message, "🤬‼НЕЛЬЗЯ ЗАПУСКАТЬ ИГРУ РАНЬШЕ ВРЕМЕНИ")


#@bot.callback_query_handler(func=lambda call: True)
def mail(call):
   global admin,rf,gf,warns,admins,alm,jbchat, admset
   if call.data=="troubledone":
   	  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Админы отметили проблему как решенную✅️")
   if call.data=="admins":
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбор был сделан: просмотр админов ️")
       admi=open(str(admset[call.message.chat.id])+"/admins.txt","r")
       kbb = types.InlineKeyboardMarkup(row_width=2)
       kb_mouse = types.InlineKeyboardButton(text='🔙 НАЗАД', callback_data='adminset')
       kbb.add(kb_mouse)

       bot.reply_to(call.message, str(admi.read()),reply_markup=kbb)
       admset.remove(call.message.chat.id)
   if call.data=="adminset":
       message=call.message
       bot.delete_message(message.chat.id, message.message_id)
       #if message.from_user.username == "L1ssab3lla" or message.from_user.username == "postolnypavel":
       kb = types.InlineKeyboardMarkup(row_width=1)
       addd = types.InlineKeyboardButton(text='➕️ добавить админа', callback_data='add')
       remove = types.InlineKeyboardButton(text='➖️ убрать админа', callback_data='remove')
       view = types.InlineKeyboardButton(text='👀 посмотреть админов', callback_data='admins')
       kb.add(addd, remove,view)
       bot.send_message(call.from_user.id, "Выбран режим управления админами бота",reply_markup=kb)
           #bot.send_message(message.chat.id, "<code>Отправлено в лс бота</code>",parse_mode="HTML")
           #admset[message.from_user.id] = message.chat.id

   if call.data=="add":
       def ghv(message):
           #global admins
           global admset
           admins=open(str(admset[message.chat.id])+"/admins.txt","r")
           admi=eval(admins.read())
           admi.append(message.text)
           gb=open(str(admset[message.chat.id])+"/admins.txt","w")
           gb.write(str(admi))
           kbb = types.InlineKeyboardMarkup(row_width=2)
           kb_mouse = types.InlineKeyboardButton(text='🔙 НАЗАД', callback_data='adminset')
           kbb.add(kb_mouse)

           bot.reply_to(message, "Готово\n\n"+str(admi), reply_markup=kbb)
           admset.remove(message.chat.id)
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбор был сделан: добавление админов ️")

       rf=bot.reply_to(call.message, "Введи юзернэйм админа без @")
       bot.register_next_step_handler(call.message, ghv)
   if call.data=="remove":
       def ghv(message):
           #global admins
           f=open(str(admset[call.message.chat.id])+"/admins.txt","r")
           adminss=eval(f.read())
           adminss.remove(message.text)
           gb=open(str(admset[call.message.chat.id])+"/admins.txt","w")
           gb.write(str(adminss))
           kbb = types.InlineKeyboardMarkup(row_width=2)
           kb_mouse = types.InlineKeyboardButton(text='🔙 НАЗАД', callback_data='adminset')
           kbb.add(kb_mouse)

           bot.reply_to(message, "Готово\n\n"+str(adminss), reply_markup=kbb)
           admset.remove(message.chat.id)
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбор был сделан: удаление админов ️")

       rf=bot.reply_to(call.message, "Введи юзернэйм админа без @")
       bot.register_next_step_handler(call.message, ghv)

   if call.data=="skr":
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⏰️Магазин закрыт")

   if call.data=="minusw":
       rey=bot.send_message(call.message.chat.id, "⌛️Подождите пару секунд до завершения транзакции")
       time.sleep(3)
       try:
           if alm[call.from_user.username] > 0:
               #warns[call.from_user.id][0] = warns[call.from_user.id][0] -1
               #warns[call.from_user.id][1] = call.from_user.first_name
               alm[call.from_user.username] = alm[call.from_user.username] - 1
               bot.edit_message_text(chat_id=call.message.chat.id, message_id=rey.message_id, text="✅️Платеж прошел успешно. Варны отминусованы✅️")
               #warnss=open("warns.txt","w")
               #warnss.write(str(warns))
               re=os.listdir("warns/"+str(call.message.reply_to_message.from_user.id))
               os.remove("warns/"+str(call.message.reply_to_message.from_user.id)+"/"+re[-1])

               almm=open("almaz.txt","w")
               almm.write(str(alm))
               bot.send_message(jbchat, "👀Кто-то купил снятие варна за алмазы")
           else:
               bot.edit_message_text(chat_id=call.message.chat.id, message_id=rey.message_id, text="❌️Произошла ошибка при проведении транзакции. У Вас на балансе 0")


       except:
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=rey.message_id, text="❌️Произошла неизвестная ошибка при проведении транзакции. Возможно у Вас нету варнов. Повторите попытку или напишите нам")
   if call.data=="ntouch":
       def nntouch(call):
           kbb = types.InlineKeyboardMarkup()
           cancel = types.InlineKeyboardButton(text='❌️ Отмена (уже было нажато)', callback_data='cancel')
           #kb_cat = types.InlineKeyboardButton(text='Кошку', callback_data='cat')
           #kb_mouse = types.InlineKeyboardButton(text='Мышь', callback_data='mouse')
           kbb.add(cancel)
           #bot.send_message(message.chat.id, 'Привет', reply_markup=kb)
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⚠️⚠️⚠️Вы получаете предупреждение от администратора группы\n"+str(len(os.listdir(str(call.message.chat.id)+"/warns/"+str(call.message.reply_to_message.from_user.id))))+ "/3", reply_markup=kbb)

           #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⚠️⚠️⚠️Ты получаешь варн от админа\n"+str(warns[call.message.reply_to_message.from_user.id][0])+ "/3", reply_markup=kbb)
           bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Готово:)")


       ew=bot.get_chat_member(call.message.chat.id, call.from_user.id)
       status = ["administrator","creator"]
       if str(ew.status) in status:
           #settingss[str(message.from_user.id)]=message
           nntouch(call)

       #else:
          # bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Это действие не предназначено для тебя😉")

   if call.data=="pluso":
       #if call.from_user.username in admins:
       def ppluso(call):
           #warns[call.message.reply_to_message.from_user.id][0] = warns[call.message.reply_to_message.from_user.id][0] + 1
           #warns[call.message.reply_to_message.from_user.id][1] = call.message.reply_to_message.from_user.first_name
           #f=open("warns.txt","w")
           #f.write(str(warns))
           tt=pytz.timezone("Europe/Moscow")
           dt = datetime.datetime.now(tt)
           dt_string = dt.strftime("Дата(%d-%m-%Y) и время(%H-%M-%S)")
           f=open(str(call.message.chat.id)+"/warns/"+str(call.message.reply_to_message.from_user.id)+"/"+str(dt_string), "w")
           f.write(str(1))

           kb = types.InlineKeyboardMarkup(row_width=2)
           kb_dog = types.InlineKeyboardButton(text='+1', callback_data='pluso')
           kb_cat = types.InlineKeyboardButton(text='-1', callback_data='mio')
           kb_mouse = types.InlineKeyboardButton(text='🛑Оставить как есть', callback_data='ntouch')
           kb.add(kb_dog, kb_cat, kb_mouse)
           #bot.send_message(message.chat.id, 'Привет', reply_markup=kb)
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас варнов у "+call.message.reply_to_message.from_user.first_name+": "+str(len(os.listdir(str(call.message.chat.id)+"/warns/"+str(call.message.reply_to_message.from_user.id)+"/")))+"\nХотите снять?",reply_markup=kb)

           #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас варнов у "+call.message.reply_to_message.from_user.first_name+": "+str(warns[call.message.reply_to_message.from_user.id][0])+"\nХотите снять?",reply_markup=kb)
           bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Готово:)")

       #else:
           #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Это действие не предназначено для тебя😉")
       ew=bot.get_chat_member(call.message.chat.id, call.from_user.id)
       status = ["administrator","creator"]
       if str(ew.status) in status:
           #settingss[str(message.from_user.id)]=message
           ppluso(call)

   if call.data=="mio":
       def mmio(call):
           #warns[call.message.reply_to_message.from_user.id][0] = warns[call.message.reply_to_message.from_user.id][0] - 1
           #warns[call.message.reply_to_message.from_user.id][1] = call.message.reply_to_message.from_user.first_name
           #f=open("warns.txt","w")
           #f.write(str(warns))
           re=os.listdir(str(call.message.chat.id)+"/warns/"+str(call.message.reply_to_message.from_user.id))
           os.remove(str(call.message.chat.id)+"/warns/"+str(call.message.reply_to_message.from_user.id)+"/"+re[-1])
           kb = types.InlineKeyboardMarkup(row_width=2)
           kb_dog = types.InlineKeyboardButton(text='+1', callback_data='pluso')
           kb_cat = types.InlineKeyboardButton(text='-1', callback_data='mio')
           kb_mouse = types.InlineKeyboardButton(text='🛑Оставить как есть', callback_data='ntouch')
           kb.add(kb_dog, kb_cat, kb_mouse)
           #bot.send_message(message.chat.id, 'Привет', reply_markup=kb)
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас варнов у "+call.message.reply_to_message.from_user.first_name+": "+str(len(os.listdir(str(call.message.chat.id)+"/warns/"+str(call.message.reply_to_message.from_user.id))))+"\nХотите снять?",reply_markup=kb)

           #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас варнов у "+call.message.reply_to_message.from_user.first_name+": "+str(warns[call.message.reply_to_message.from_user.id][0])+"\nХотите снять?",reply_markup=kb)
           bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Готово:)")



       ew=bot.get_chat_member(call.message.chat.id, call.from_user.id)
       status = ["administrator","creator"]
       if str(ew.status) in status:
           #settingss[str(message.from_user.id)]=message
           mmio(call)

       #else:
           #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Это действие не предназначено для тебя😉")

   if call.data=="cancel":
       def ccancel(call):

           kb = types.InlineKeyboardMarkup(row_width=2)
           kb_dog = types.InlineKeyboardButton(text='+1', callback_data='pluso')
           kb_cat = types.InlineKeyboardButton(text='-1', callback_data='mio')
           kb_mouse = types.InlineKeyboardButton(text='🛑Оставить как есть', callback_data='ntouch')
           kb.add(kb_dog, kb_cat, kb_mouse)
           #bot.send_message(message.chat.id, 'Привет', reply_markup=kb)
           ree=os.listdir(str(call.message.chat.id)+"/warns/"+str(call.message.reply_to_message.from_user.id))
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас варнов у "+call.message.reply_to_message.from_user.first_name+": "+str(len(ree))+"\nХотите снять?",reply_markup=kb)

           #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сейчас варнов у "+call.message.reply_to_message.from_user.first_name+": "+str(warns[call.message.reply_to_message.from_user.id][0])+"\nХотите снять?",reply_markup=kb)
           bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Готово:)")

       ew=bot.get_chat_member(call.message.chat.id, call.from_user.id)
       status = ["administrator","creator"]
       if str(ew.status) in status:
           #settingss[str(message.from_user.id)]=message
           ccancel(call)
       #else:
           #bot.reply_to(message, "⚠️У Вас нету прав для настроек бота.\n\nЕсли Вы считаете что это ошибка, свяжитесь с админами")

       #else:
           #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Это действие не предназначено для тебя😉")

   try:
        if call.data == "ruletka":
           #bot.delete_message(call.message.chat.id, call.message.message_id)
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Рулетка была запущена")
           bot.send_message(call.message.chat.id, " сейчас будет играть в рулетку 🔫\n\nЕсли удача не на твоей стороне, ты будешь кикнут из чата! 😈\n\nЯ предупредил! 🫣\n\nP.S. Администраторы смогут вас вернуть, просто напишите им в лс!",parse_mode="Markdown")
           bot.send_message(call.message.chat.id, "🎲")
           chi = random.randint(1,8)
           if chi <= 3:
               bot.send_message(call.message.chat.id, "Повезло. Выжил(а)")
           else:
                try:
                    bot.send_message(call.message.chat.id, "Не повезло. Кикаю")
                    #kick(message,message.from_user.id)
                    bot.kick_chat_member(call.message.chat.id, gf)
                    bot.send_message(gf, "Я забанил тебя на 2 минуты. Я тебя сам разбаню, тебя нужно будет самостоятельно зайти в группу. Ссылку на группу дам через пару минут😉")
                    time.sleep(120)
                    bot.unban_chat_member(call.message.chat.id,gf)
                    bot.send_message(gf, "Я разбанил. Заходи\nhttps://t.me/+RRnmQDtW9ZteRx0Un")
                except Exception as e:
                    bot.send_message(call.message.chat.id, str(e))
   except Exception as e:
        bot.send_message(call.message.chat.id, str(e))
@bot.message_handler(commands=["admin"])
def adminch(message):
    f=open(str(message.chat.id)+"/adminstatus.txt","r")
    status=f.read()
    ass=open(str(message.chat.id)+"/adminchat.txt","r")
    admin=ass.read()
    f.close()
    ass.close()
    if str(status) == "true" and admin != "":
        call(message,admin)
    else:
        bot.reply_to(message, "⚠️Жалоба не была доставлена администраторам.\n\n💡Возможные причины:\n•Администраторы отключили эту функцию\n•Администраторы не указали куда отправлять жалобы")
def call(message,admin):
	#global admin
	bot.reply_to(message, "Жалоба отправлена", parse_mode="Markdown")
	menu1 = telebot.types.InlineKeyboardMarkup()
	menu1.add(telebot.types.InlineKeyboardButton(text = 'Проблема решена✅️', callback_data='troubledone'))
	bot.send_message(admin, "🚨Требуют действий администраторов в чате.\nЖалоба: "+message.text, reply_markup=menu1)
#@bot.callback_query_handler(func=lambda call: True)
#def rul(call):
    #except Exception as e:
        #bot.reply_to(call.message, str(e))


@bot.message_handler(commands=["adminset"])
def addmm(message):
    if message.chat.type != "private":
        adminset(message)
def adminset(message):
    global admset
    bot.delete_message(message.chat.id, message.message_id)
    if message.chat.type != "private":
        #if message.from_user.username == "L1ssab3lla" or message.from_user.username == "postolnypavel":
        kb = types.InlineKeyboardMarkup(row_width=1)
        addd = types.InlineKeyboardButton(text='➕️ добавить админа', callback_data='add')
        remove = types.InlineKeyboardButton(text='➖️ убрать админа', callback_data='remove')
        view = types.InlineKeyboardButton(text='👀 посмотреть админов', callback_data='admins')
        kb.add(addd, remove,view)
        bot.send_message(message.from_user.id, "Выбран режим управления админами бота",reply_markup=kb)
        bot.send_message(message.chat.id, "<code>Отправлено в лс бота</code>",parse_mode="HTML")
        admset[message.from_user.id] = message.chat.id
@bot.message_handler(commands=["ruletka"])
def ruletka(message):
    global rf,gf
    #user_id = message.from_user.id
    #user_name = message.from_user.first_name+" "+message.from_user.last_name
    #mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    keyboard = types.InlineKeyboardMarkup()
    urll = types.InlineKeyboardButton(text="Запусти меня тут, прежде чем будешь играть", url="https://t.me/chadmin_jbfamily_bot")
    ur = types.InlineKeyboardButton(text="✅️Готов(а) играть. Запустил(а)", callback_data="ruletka")
    keyboard.add(urll,ur)
    rf=bot.reply_to(message, "Выполни все требования и запускай игру", reply_markup=keyboard)
    bot.delete_message(message.chat.id, message.message_id)
    gf=message.from_user.id
@bot.message_handler(commands=["kick","ban"])
def kickcommand(message):
	global admins
	if message.from_user.username in admins:
		kick(message, message.reply_to_message.from_user.id)
	else:
		bot.reply_to(message, "У вас нет доступа к этой функции")
try:
	@bot.message_handler(commands=["warn"])
	def wirn(message):
	    if message.chat.type != "private":
	        f=open(str(message.chat.id)+"/warnstatus.txt","r")
	        e=f.read()
	        if e=="true":
	            warncommand(message)
	        else:
	            bot.reply_to(message, "❌️Предупреждение не было засчитано, так как оно отключено в настройках группы")
	def warncommand(message):
		global admins,warns,admin
		#d = open(str(message.chat.id)+"/admins.txt", "r")
		#admins=eval(d.read())
		def warrn(message):
			if str(message.reply_to_message.from_user.id) in os.listdir(str(message.chat.id)+"/warns/"):
				#warns[message.reply_to_message.from_user.id][0] = warns[message.reply_to_message.from_user.id][0] + 1
				#warns[message.reply_to_message.from_user.id][1] = message.reply_to_message.from_user.first_name
				#f=open("warns.txt","w")
				#f.write(str(warns))
				tt=pytz.timezone("Europe/Moscow")
				dt = datetime.datetime.now(tt)
				dt_string = dt.strftime("Дата(%d-%m-%Y) и время(%H-%M-%S)")
				f=open(str(message.chat.id)+"/warns/"+str(message.reply_to_message.from_user.id)+"/"+str(dt_string), "w")
				f.write(str(1))

				bot.delete_message(message.chat.id, message.message_id)
				message.message_id=message.reply_to_message.message_id
				kb = types.InlineKeyboardMarkup()
				cancel = types.InlineKeyboardButton(text='❌️ Отмена', callback_data='cancel')
				#kb_cat = types.InlineKeyboardButton(text='Кошку', callback_data='cat')
				#kb_mouse = types.InlineKeyboardButton(text='Мышь', callback_data='mouse')
				kb.add(cancel)
				#bot.send_message(message.chat.id, 'Привет', reply_markup=kb)
				if len(message.text.split("/warn ")) == 2 or len(message.text.split("/warn@TrueChatHelperBot ")) == 2:
				    pr=message.text.split("/warn@TrueChatHelperBot ")
				    pr=pr[-1].split("/warn ")
				    prich="<b>"+pr[-1]+"</b>"
				else:
				    prich="<b>pust</b>"

				bot.reply_to(message,"⚠️⚠️⚠️Вы получаете предупреждение от администратора группы\n"+str(len(os.listdir(str(message.chat.id)+"/warns/"+str(message.reply_to_message.from_user.id))))+ "/3\n\nПричина: "+prich, reply_markup=kb, parse_mode="HTML")


				#bot.reply_to(message,"⚠️⚠️⚠️Ты получаешь варн от админа\n"+str(warns[message.reply_to_message.from_user.id][0])+ "/3\n\nПричина: "+prich, reply_markup=kb, parse_mode="HTML")
				#user_id = message.reply_to_message.from_user.id
				#user_name = message.reply_to_message.from_user.first_name+" "+message.reply_to_message.from_user.last_name
				#mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
				#bot.send_message(admin, "!!!Пользователь "+mention+" получает варн", parse_mode="Markdown")
			else:
			    #warns[message.reply_to_message.from_user.id] = []
			    #warns[message.reply_to_message.from_user.id].append(1)
			    #warns[message.reply_to_message.from_user.id].append(message.reply_to_message.from_user.first_name)
			    try:
			        os.mkdir(str(message.chat.id)+"/warns/"+str(message.reply_to_message.from_user.id))
			    except:
			        pass

			    #f=open("warns.txt","w")
			    #f.write(str(warns))
			    tt=pytz.timezone("Europe/Moscow")
			    dt = datetime.datetime.now(tt)
			    dt_string = dt.strftime("Дата(%d-%m-%Y) и время(%H-%M-%S)")
			    f=open(str(message.chat.id)+"/warns/"+str(message.reply_to_message.from_user.id)+"/"+str(dt_string), "w")
			    f.write(str(1))
			    bot.delete_message(message.chat.id, message.message_id)
			    message.message_id=message.reply_to_message.message_id
			    kb = types.InlineKeyboardMarkup()
			    cancel = types.InlineKeyboardButton(text='❌️ Отмена', callback_data='cancel')
			    kb.add(cancel)
			    prich="<b>pust</b>"
			    if len(message.text.split("/warn ")) == 2 or len(message.text.split("/warn@TrueChatHelperBot ")) == 2:
				    pr=message.text.split("/warn@TrueChatHelperBot ")
				    pr=pr[-1].split("/warn ")
				    prich="<b>"+pr[-1]+"</b>"
				#else:
				#    prich="<b>pust</b>"
			    bot.reply_to(message,"⚠️⚠️⚠️Вы получаете предупреждение от администратора группы\n1/3\n\nПричина: "+prich, reply_markup=kb,parse_mode="HTML")

			    #bot.reply_to(message,"⚠️⚠️⚠️Ты получаешь варн от админа\n"+str(warns[message.reply_to_message.from_user.id][0])+ "/3\n\nПричина: "+prich, reply_markup=kb,parse_mode="HTML")
				#user_id = message.reply_to_message.from_user.id
				#user_name = message.reply_to_message.from_user.first_name+" "+message.reply_to_message.from_user.last_name
				#mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
				#bot.send_message(admin, "!!!Пользователь "+mention+" получает варн", parse_mode="Markdown")
		#else:
			#bot.reply_to(message, "У вас нет доступа к этой функции")

		ew=bot.get_chat_member(message.chat.id, message.from_user.id)
		status = ["administrator","creator"]
		if str(ew.status) in status:
		    #warrn[str(message.from_user.id)]=message
		    warrn(message)
		else:
		    bot.reply_to(message, "⚠️У Вас нету прав для предупреждений участников чата.\n\nЕсли Вы считаете что это ошибка, свяжитесь с админами")

		#if message.from_user.username in admins:
except:
	pass
@bot.message_handler(commands=["info"])
def showwarns(message):
	global warns,alm
	#bot.reply_to(message, str(warns))
	wrn=""
	try:
	    for i in list(os.listdir(str(message.chat.id)+"/warns/"+str(message.reply_to_message.from_user.id)+"/")):
	        wrn=wrn+i+"\n"
	except:
	    wrn="Пользователь не получил варнов"
	try:
	    almaz=alm[message.reply_to_message.from_user.username]
	except:
	    almaz=0
	if almaz == None or almaz == "":
	    almaz=0
	try:
	    ln=message.reply_to_message.from_user.last_name
	except:
	    ln="*Фамилия не указана*"
	bot.send_message(message.chat.id, "ℹ️Информация о пользователе:\n\n<b>Данные о пользователе:</b>\n\nИмя: "+message.reply_to_message.from_user.first_name+"\nФамилия: "+ln+"\n\n<b>Алмазы:</b>\n\n"+str(almaz)+"\n\n<b>Варны:</b>\n\n"+wrn,parse_mode="HTML")

	#mention = "<tg-spoiler><a href='https://t.me/tel46'>test</a></tg-spoiler>"
	#bot.send_message(message.chat.id, mention, parse_mode="HTML")
"""@bot.message_handler(commands=["manual"])
def manualwarn(message):
	global warns,admins
	if message.chat.type == "private":
		bot.delete_message(message.chat.id, message.message_id)
		if message.from_user.username in admins:
			def manwarns(message):
				global warns, jbchat
				warns=eval(message.text)
				bot.send_message(jbchat, "❗️❗️❗️ВАРНЫ ОБНОВИЛИ АДМИНЫ. ВАРНЫ МОЖНО УВИДЕТЬ ТУТ: /showwarn")
				mess=bot.send_message(message.chat.id, "Отправь список варнов")
				bot.register_next_step_handler(mess, manwarns)
	else:
		bot.reply_to(message, "Эта команда может использоваться только в личных сообщениях")
"""

"""@bot.message_handler(commands=["all"])
def unwarn(message):
	global admins,users,unreg
	if message.from_user.username in admins:
	    mfd=bot.reply_to(message, message.from_user.first_name+" запустил(а) призыв\nПризыв удалится через 60 секунд")
	    f=open("users.txt","r")
	    users=eval(f.read())
	    #mff=message.text.split("/call ")
	    mgh=message.text.split("/all ")
	    #usrs=" ".join(users)
	    gft=[]
	    priz=mgh[1]+"\n"
	    for i in users:
	        if i in unreg:
	            pass
	        else:

	            mention = "[.︎︎](tg://user?id="+str(i)+")"
	            priz=priz+mention
	            '''mgs=bot.send_message(message.chat.id, mention, parse_mode="Markdown")
	            gft.append(mgs)
	            time.sleep(3)
	            #bot.delete_message(message.chat.id, mgs.message_id)'''
	            mgs=None

	    #mgs=bot.send_message(message.chat.id, "@L1ssab3lla\n@OksanaKnittedToy", parse_mode="Markdown")
	    #time.sleep(1)
	    #bot.delete_message(message.chat.id, mgs.message_id)
	    #mgs=None
	    #bot.send_message(1373351243,mgh[1])
	    bot.send_message(356906774,mgh[1])
	    prr=bot.reply_to(mfd, priz, parse_mode="Markdown")
	    bot.reply_to(mfd, "Призыв окончен!")
	    priz=""
	    time.sleep(30)
	    bot.delete_message(message.chat.id, prr.message_id)
	    '''time.sleep(30)
	    for i in gft:
	        bot.delete_message(message.chat.id, i.message_id)
	else:
	    bot.reply_to(message, "Эту команду могут использовать только админы!")

	    """
'''
@bot.message_handler(commands=["unwarn"])
def unwarn(message):
	global admins,warns
	if message.from_user.username in admins:
		bot.reply_to(message, "Есть unwarn")
		#warns={}
		#f=open("warns.txt","w")
		#f.write(str(warns))
		shutil.rmtree("warns/")
		os.mkdir("warns/")

	'''

'''@bot.message_handler(commands=["eval"])
	def evall(message):
		try:
			def evalcode(message):
				eval(message.text)
				bot.send_message(message.chat.id, "Код внедрен")
			code=bot.send_message(message.chat.id, "Send code...")
			bot.register_next_step_handler(code, evalcode)
		except Exception as e:
			bot.reply_to(message, str(e))
			"""

			'''
@bot.message_handler(commands=["top"])
def boltt(message):
    a=list(sorted(boltun.items()))
    bot.delete_message(message.chat.id, message.message_id)
    f=0
    stt=""
    for i in a:
        #if f < 10:
        i=str(i)
        bi=i.split("(")
        bo=bi[1].split(",")
        bl=bo[1].split(")")
        ghgh=bo[0].split("'")
        ssa=ghgh[1]+" - "+bl[0]
        stt=stt+"\n"+str(ssa)
        f=f+1
    bot.send_message(message.chat.id, "Наш топчик активных участников :\n"+str(stt))

'''
@bot.message_handler(commands=["give"])
def ggive(message):
    if message.chat.type != "private":
        bot.reply_to(message, "Отправлено в личные сообщения")
        message.chat.type="private"
        give(message)
def give(message):
    global alm,jbchat
    if message.chat.type=="private":
        if len(message.text.split("/give ")) == 2:

            gfr=message.text.split("/give ")
            rey=bot.send_message(message.from_user.id, "⌛️Платеж проводится, ждите...")
            time.sleep(4)
            try:

                if alm[message.from_user.username] > 0:
                        try:
                                if alm[gfr[1]] == 0:
                                    alm[gfr[1]] = 1
                                else:
                                    alm[gfr[1]] = alm[gfr[1]] + 1
                        except:
                            #alm.append(gfr[1])
                            alm[gfr[1]] = 1
                        alm[message.from_user.username] = alm[message.from_user.username] - 1
                        almm=open(str(message.chat.id)+"/almaz.txt","w")
                        almm.write(str(alm))
                        bot.edit_message_text(chat_id=message.chat.id, message_id=rey.message_id, text="✅️Платеж проведен успешно:)")
                        bot.send_message(message.chat.id,"👀Кто то дал @"+gfr[1]+" алмаз")
                else:
                    bot.edit_message_text(chat_id=message.from_user.id, message_id=rey.message_id, text="❌️Произошла ошибка при проведении транзакции. У Вас 0 алмазов")
            except Exception as e:
                bot.edit_message_text(chat_id=message.from_user.id, message_id=rey.message_id, text="❌️Произошла неизвестная ошибка при проведении транзакции("+str(e)+"). Повторите попытку или напишите нам")


        else:
            bot.reply_to(message, "Используйте эту команду так: /give VasyaPupkin")
    else:
        bot.reply_to(message, "Используйте эту команду со мной в личных сообщениях")
@bot.message_handler(commands=["store"])
def sstore(message):
    if message.chat.type != "private":
        bot.reply_to(message, "Отправлено в личные сообщения")
        message.chat.type="private"
        store(message)
def store(message):
    global alm
    if message.chat.type == "private":
        f=open(str(message.chat.id)+"/almaz.txt")
        alm=eval(f.read())
        kbr = types.InlineKeyboardMarkup(row_width=1)
        srk = types.InlineKeyboardButton(text='❌️ Убрать магазин ', callback_data='skr')
        wrn = types.InlineKeyboardButton(text='💎 Снять предупреждение за 1 алмаз', callback_data='minusw')
        #prr= types.InlineKeyboardButton(text="💎
        #kb_mouse = types.InlineKeyboardButton(text='Мышь', callback_data='mouse')
        kbr.add(srk,wrn)
        try:
            bot.reply_to(message, "🧺Вы выбрали магазин.\nУ вас сейчас <b>"+str(alm[message.from_user.username])+"</b> алмазов. Что вы с ними хотите делать??", parse_mode="HTML",reply_markup=kbr)

        except:
            bot.reply_to(message, "🧺Вы выбрали магазин.\nУ вас сейчас <b>0</b> алмазов. Что вы с ними хотите делать??", parse_mode="HTML",reply_markup=kbr)

    else:
        bot.reply_to(message,"Используйте эту команду в личных сообщениях")
        '''
#@bot.message_handler(commands=["weather"])
def weather(message):
    f=open(str(message.chat.id)+"/weather.txt","r")
    re=f.read()
    f.close()
    if re == "true":
        weatherr(message)
    else:
        bot.reply_to(message, "⛔️ Администрация чата отключила эту функцию для группы.\n\nОбратитесь к ним")
def weatherr(message):
    bot.delete_message(message.chat.id,message.message_id)
    #try:
    message.text=message.text.lower()
    ww=message.text.split("погода ")
    observation = mgr.weather_at_place(ww[-1])
    w = observation.weather
    clouds=w.detailed_status         # 'clouds'
    wind=w.wind()                  # {'speed': 4.6, 'deg': 330}
    hum=w.humidity                # 87
    temp=w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    rain=w.rain                    # {}
    heat=w.heat_index              # None
    cloud=w.clouds                  # 75
    bot.send_message(message.chat.id, "Погода в <b>"+str(ww[-1])+"</b>:\n\nСтатус: <b>"+str(clouds)+"</b>\nВетер: <b>"+str(wind)+"</b>\nВлажность: <b>"+str(hum)+"</b>\nТемпература: <b>"+str(temp)+"</b>\nДождь: <b>"+str(rain)+"</b>\nУФ-ИНДЕКС: <b>"+str(heat)+"</b>\nОблачность: <b>"+str(cloud)+"</b>\n\n<b>Данные взяты с канала OpenWeatherMap</b>",parse_mode="HTML")
    #except:
        #bot.send_message(message.chat.id, 'Город не найден :(')
'''@bot.message_handler(content_types=["text"])
def fde(message):
    global ca
    if message.chat.type != "private":
        if message.forward_from:
            e=message.text.split("/adminchatautosetup Это сообщение для настройки админ чата.\nКод: ")
            e=e[-1]
            if message.chat.id != e and e in ca:
                f=open(str(e)+"/adminchat.txt","w")
                f.write(str(message.chat.id))
                f.close()
                bot.send_message(e, "✅️Админ чат успешно был привязан к этой группе")
                bot.send_message(message.chat.id, "📶Связь с чатом установлена")
                w=bot.send_message(message.from_user.id, "📶Связь с чатом установлена успешно")
                bot.edit_message_text(chat_id=message.from_user.id, message_id=w.message_id-1, text="<b>Настройки устарели, запустите их заново из группы</b>",parse_mode="HTML")

                ca.remove(e)
'''
@bot.message_handler(content_types=["text"])
def delad(message):
    global unreg,boltun,admins
    msg=message.text.lower()
    mhg=msg.split(" ")
    if len(msg.split("макс, ")) == 2 and len(msg.split("?")) == 2:
        rr=bot.reply_to(message, "🔮Шар вопросов думает...")
        g=random.randint(1,7)
        time.sleep(g)
        gh=["Да", "Нет", "Возможно", "Маловероятно"]
        ty=random.randint(0,3)
        bot.edit_message_text(chat_id=message.chat.id, message_id=rr.message_id, text="🔮ШАР ГОВОРИТ...."+gh[ty])
    if len(msg.split("погода ")) == 2:
        weather(message)
    '''if len(message.text.split(".птица")) == 2:
        konk="🦜от Ивана Царевича сбежала жар-птица😱😱😱\nОн уже успел так расстроится...😥\n\nПомогите Ивану Царевичу найти птицу за вознаграждение🤑🤑🤑.\n\n Жар-птица иногда мелькает в ночном городе. Поймайте ее за хвост!\n\nВедущий пишет сообщение во время ночи, бот удаляет сообщение. Ваша задача успеть заскринить это сообщение.\n\n===========\nНаграды:\nигроку, который поймает птицу.\n\nЧто за награда, хмм...это секрет🙃.\n\nКто успел заскринить, кидайте в лс ведущему)\nНаше лс всегда открыто"
        if message.from_user.username in admins:
            if len(message.text.split(".птица @")) > 1:
                gjf=message.text.split(".птица ")
                ggf=bot.reply_to(message, konk+"\n\n=====================\n!!!🧛Ведущий: "+gjf[1])
                bot.pin_chat_message(chat_id=message.chat.id, message_id=ggf.message_id)
            else:
                bot.reply_to(message, konk)
        else:
            bot.reply_to(message, konk)

    if message.text == ".коды":
        bot.reply_to(message, "<a href='https://telegra.ph/Kody-varnov-v-chate-JB-FAMILYCHatDom-08-25'>коды варнов тут</a>", parse_mode="HTML")

    if message.from_user.first_name in boltun:
        boltun[message.from_user.first_name]=boltun[message.from_user.first_name]+len(mhg)
        bolt=open("boltun.txt","w")
        bolt.write(str(boltun))
    else:
        boltun[message.from_user.first_name]=len(mhg)
        bolt=open("boltun.txt","w")
        bolt.write(str(boltun))
    f=open("users.txt","r")
    users=eval(f.read())
    if message.from_user.id in users:
        pass
    else:
        users.append(message.from_user.id)
        fg=open("users.txt","w")
        fg.write(str(users))
    if len(msg.split("unreg")) > 1:
        bot.delete_message(message.chat.id, message.message_id)
        if message.from_user.id in unreg:
            bot.send_message(message.chat.id, message.from_user.first_name+", Вы и так уже исключены на время из всеобщего призыва!")
        else:
            unreg.append(message.from_user.id)
            fff=open("unreg.txt", "w")
            fff.write(str(unreg))
            if len(msg.split("unreg ")) > 1:
                bot.send_message(message.chat.id, message.from_user.first_name+", Вы были исключены на время из всеобщего призыва. Вы еще указали потом это. Я не знаю что с этим делать🤷‍♂️\n\n"+message.text)
            else:
                bot.send_message(message.chat.id, message.from_user.first_name+", Вы были исключены на время из всеобщего призыва.")
    if len(msg.split("reg")) > 1:
        bot.delete_message(message.chat.id, message.message_id)
        if message.from_user.id in unreg:
            unreg.remove(message.from_user.id)
            fff=open("unreg.txt", "w")
            fff.write(str(unreg))

            bot.send_message(message.chat.id, message.from_user.first_name+", Вы снова будете получать уведомления о призыве!")
        else:
            bot.send_message(message.chat.id, message.from_user.first_name+", Вы и так получаете уведомления о призыве!")


    if len(msg.split("#реклама")) > 1:
        bot.delete_message(message.chat.id, message.message_id)
    '''
    if msg == "макс" or msg == "бот" or msg=="максим":
        #print(1)
        if message.from_user.first_name == "Channel" or message.from_user.first_name == "Group":
           bot.reply_to(message, "Да, <i>анонимный админ</i>. Чем могу помочь?)", parse_mode="HTML")
        else:
            #user_id = message.from_user.id
            #user_name = message.from_user.first_name+" "+message.from_user.last_name
            #mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
            bot.reply_to(message, "Чем могу помочь?)", parse_mode="Markdown")

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    #bot.send_message(message.chat.id, str(message.new_chat_members[0]))
    rde=message.new_chat_members[0]
    if rde.id == 5457377018:
        bot.reply_to(message, "Привет, "+message.from_user.first_name+"!\nЯ очень простой и удобный бот для модерации в чатах Telegram. Бот еще работает нестабильно, поэтому ссори если будут баги:)\n\nДля начала выдай мне права администратора полные и напиши в чате /register чтобы настроить меня в этом чате если я тут первый раз, иначе используй просто настройки. Приятного пользования)")
    else:
        f=open(str(message.chat.id)+"/welcome.txt","r")
        name=message.from_user.first_name
        surname=message.from_user.last_name
        welcome=f.read()
        bot.reply_to(message, text=welcome.format(name,surname), parse_mode="HTML")

bot.infinity_polling(none_stop=True)

def telegram_polling():
    try:
        bot.polling(none_stop=True, timeout=60) #constantly get messages from Telegram
    except:
        traceback_error_string=traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

if __name__ == '__main__':
    telegram_polling()
