import time

from flask import Flask
#comment 
class Messenger:
    db = []
    requested_count = 0

    def send_message(self, name, text):
        timestamp = time.asctime()
        self.db.append({
            'name': name,
            'text': text,
            'timestamp': timestamp
        })

    def get_messages(self):
        return self.db

    def get_new_messages(self):
        new_messages = self.db[self.requested_count:]
        self.requested_count += len(new_messages)
        return new_messages


messenger = Messenger()
messenger.send_message('Jack', 'abc')
messenger.send_message('Jack', 'abcd')
print('All:', messenger.get_messages())
print('New:', messenger.get_new_messages())
print()

messenger.send_message('Black', 'Hello!')
print('All:', messenger.get_messages())
print('New:', messenger.get_new_messages())
print()

messenger.send_message('Black', 'Hello2')
print('All:', messenger.get_messages())
print('New:', messenger.get_new_messages())
print()

messenger.send_message('Black', 'Hello3')
print('All:', messenger.get_messages())
print('New:', messenger.get_new_messages())


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world - Maks hui sosi"

@app.route("/status")
def status():
    return {'status': 'OK'}

app.run()