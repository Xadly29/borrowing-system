import connectdatabase

with connectdatabase.connection.cursor() as cursor:
    cursor.execute("SELECT itemID, availability FROM itemtbl")
    result = cursor.fetchall()
    for row in result:
        print(row)
