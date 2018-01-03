from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

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
        self.go_back(update)

    def on_exit_s1(self, update):
        print('Leaving s1')

    def on_enter_s2(self, update):
        update.message.reply_text("肚子餓了 快幫我買東西吃")
        self.go_back(update)

    def on_exit_s2(self, update):
        print('Leaving s2')

    def on_enter_s3(self, update):
        update.message.reply_text("那麼早就睡 你是豬嗎")
        self.go_back(update)

    def on_exit_s3(self, update):
        print('Leaving s3')
