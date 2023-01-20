import telebot

# تعين البوت
bot = telebot.TeleBot("5769323463:AAFKnPLkoEUTeKh4zN_D4nUySLP0oL32I-0")

# معرف المجموعة الرسومية
chat_id = 

# ارسال التاك لاعضاء المجموعة الرسومية
def tag_all(message):
    members = bot.get_chat_members_count(chat_id)
    for i in range(members):
        try:
            username = bot.get_chat_member(chat_id, i).user.username
            if(username):
                message_with_tag="@" + username + " " + message
                bot.send_message(chat_id, message_with_tag)
        except Exception as e:
            print(e.args)
            continue
# مثال 
message = "تعالوا نتسلى ونكسر هل روتين 🫂🤍."
tag_all(message)
