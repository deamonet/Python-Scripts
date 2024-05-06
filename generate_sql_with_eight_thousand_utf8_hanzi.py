with open("eight_thousand_ut8.sql", "w", encoding="utf-8") as f:
    f.write('insert into message_integration.note (content) values (')
    f.write("\"")
    for _ in range(8200):
        f.write("葉")
    f.write("\" );")