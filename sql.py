import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)

request = ("CREATE TABLE IF NOT EXISTS products"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255),"
           "price INTEGER,"
           "depth INTEGER)")
cursor.execute(request)

insert_request = ("INSERT INTO products"
                "(name, description, price, depth) VALUES (?, ?, ?, ?)")
cursor.execute(insert_request, ("бассейн 1", "Цей чудовий басейн ідеально підійде для вашого подвір'я, створюючи комфортне місце для відпочинку в спекотні дні.", "$200", "2m"))
cursor.execute(insert_request, ("бассейн 2", "цим басейном ви отримаєте можливість насолоджуватися водними розвагами разом з родиною та друзями!", "$400", "2m"))
cursor.execute(insert_request, ("бассейн 3", "Цей стильний басейн стане яскравим акцентом у вашому саду та додасть елегантності вашому простору.", "$600", "2m"))
cursor.execute(insert_request, ("бассейн 4", "Ідеальний вибір для великих сімей, цей басейн дозволяє проводити час на воді весело і безпечно.", "1200", "2m"))
cursor.execute(insert_request, ("бассейн 5", "Насолоджуйтеся розкішшю та комфортом з цим басейном, що ідеально підходить для розваг в літній сезон.", "$1600", "2m"))
cursor.execute(insert_request, ("бассейн 6", "Відмінний вибір для тих, хто хоче створити ідеальне місце для відпочинку на свіжому повітрі.", "$3200", "2m"))

text = cursor.execute("SELECT * FROM products")
for line in text.fetchall():
    print(line)


