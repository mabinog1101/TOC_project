import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '491063275:AAHSe1vuL_FcCTEbf8FiTBc1fMt6YVvRGzc'
WEBHOOK_URL = 'https://e2e6fb41.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        's1',
        's2',
        's3'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 's1',
            'conditions': 'good_morning'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 's2',
            'conditions': 'good_afternoon'
        },
         {
            'trigger': 'advance',
            'source': 'user',
            'dest': 's3',
            'conditions': 'good_evening'
        },
        {
            'trigger': 'go_back',
            'source': [
                's1',
                's2',
                's3'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
