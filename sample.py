from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__) 
portuguese_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(portuguese_bot)
trainer.train("chatterbot.corpus.portuguese")
trainer.train("data/data.yml")
trainer.train("data/conversations.yml")
trainer.train("data/compliment.yml")


@app.route("/")
def index():
     return render_template("index.html")

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg")
     return str(portuguese_bot.get_response(userText))


if __name__ == "__main__":
     app.run(debug = True)


