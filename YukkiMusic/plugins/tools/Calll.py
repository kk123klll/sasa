
import telebot

bot_token = '5769323463:AAFMHSF4rQ3sfMJarIQa_eOkBntQGIo5hJI'
bot = telebot.TeleBot(bot_token)

# تعريف دالة للتعامل مع الطلبات الإذاعية
@bot.message_handler(commands=['invite'])
def invite_friend(message):
    chat_id = message.chat.id
    # التعامل مع رسالة الطرف الثاني
    friend = message.text[8:] 
    bot.send_message(chat_id, 'تم ارسال دعوة الى' + friend + 'للانضمام للمجموعة!')
    bot.invite_chat_member(chat_id, friend)

bot.polling()
