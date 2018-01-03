from transitions.extensions import GraphMachine
from random import randint

class TocMachine(GraphMachine):
    bot = None
    url = None
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def setbot(self,bot):
        self.bot = bot

    def fk(self, update):
       # update.message.reply_text("https://pbs.twimg.com/media/DSh-hTlUQAEiIbs.jpg:large")
        temp_list = []
        temp_list.append("https://pbs.twimg.com/media/DScqVOzVoAAbJo9.jpg:large")
        temp_list.append("https://pbs.twimg.com/media/DSl4iryVAAEpBXI.jpg:large")
        temp_list.append("https://pbs.twimg.com/media/DSh-hTlUQAEiIbs.jpg:large")
        temp_list.append("https://pbs.twimg.com/media/DSkTHHEUQAA6VYB.jpg:large")
        temp_list.append("https://pbs.twimg.com/media/DSmvjxLU8AACyYZ.jpg:large")
        temp_list.append("https://pbs.twimg.com/media/DSih7xRVQAAr7jF.jpg:large")
        url = temp_list[randint(0, 5)]
        self.bot.send_photo(chat_id=update.message.chat_id,photo=url)

    def good_morning(self, update):
        text = update.message.text
        return text.lower() == '早安'

    def good_afternoon(self, update):
        text = update.message.text
        return text.lower() == '午安'

    def good_evening(self, update):
        text = update.message.text
        return text.lower() == '晚安'

    def on_enter_s1(self, update):
        update.message.reply_text("快遲到了 還不去上課")
        self.bot.send_photo(chat_id=update.message.chat_id,photo="http://cdn.clickme.net/Gallery/2013/11/03/107e75c702dfacb323e3c97466630d2f.jpg")
        self.go_back(update)

    def on_exit_s1(self, update):
        print('Leaving s1')

    def on_enter_s2(self, update):
        update.message.reply_text("肚子餓了 快幫我買東西吃")
        self.bot.send_photo(chat_id=update.message.chat_id,photo="https://imgur.com/a/d1Ffj")
        self.go_back(update)

    def on_exit_s2(self, update):
        print('Leaving s2')

    def on_enter_s3(self, update):
        update.message.reply_text("那麼早就睡 你是豬嗎")
        self.go_back(update)
        self.bot.send_photo(chat_id=update.message.chat_id,photo="https://imgur.com/a/pZpRP")
    def on_exit_s3(self, update):
        print('Leaving s3')

