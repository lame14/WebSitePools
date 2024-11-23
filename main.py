from flask import *
import sqlite3

app = Flask(__name__)
connection = sqlite3.Cursor(connection)



def make_product_card(info):
    name = str(info[1])
    description = str (info[2])
    price = str(info[3]) + "UAH"
    return f'<div class="product-card"><img src="pool 6.jpg" alt="Товар 6" class="product-image"><h3>Товар 6</h3><p class="price">$3200</p><p>Опис: Відмінний вибір для тих, хто хоче створити ідеальне місце для відпочинку на свіжому повітрі.</p><button class="order-button" onclick="navigateTo('order')">Замовити</button></div>'

def make_product_card():