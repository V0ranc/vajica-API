from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/coinflip")
def coinflip():
    return render_template("coinflip.html")

@app.route("/coinData")
def coinData():
    print(request.args["vrednost"])
    rnd = random.randint(0, 1)
    status = ["HEADS", "TAILS"][rnd]
    if rnd == 0:
        return {"img": "https://i.postimg.cc/CBNJNfDJ/head.png", "status": status}
    else:
        return {"img": "https://i.postimg.cc/zysdXN8w/tail.png", "status": status}
    
@app.route("/randomQuote")
def randomQuote():
    quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. – Martin Luther King Jr.",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "It is never too late to be what you might have been. – George Eliot",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. – Ralph Waldo Emerson"
    ]
    quote = random.choice(quotes)
    return {"img": "url", "status": quote}

app.run(debug=True)