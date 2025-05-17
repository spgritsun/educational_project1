import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

username = 'gsp672021@gmail.com'
password = "gbiylefkztnirvyh"

receiver = 'gritsun.sp@gmail.com'
subject = 'Тестовое письмо'
body = 'Привет! Как дела?'

# Формируем сообщение с заголовками
message = f"From: {username}\r\nTo: {receiver}\r\nSubject: {subject}\r\n\r\n{body}"

context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))
    print("Письмо успешно отправлено!")
except smtplib.SMTPAuthenticationError:
    print("Ошибка аутентификации. Проверьте имя пользователя и пароль (пароль приложения).")
except Exception as e:
    print(f"Другая ошибка: {e}")