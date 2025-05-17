# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_gmail():
    # Конфигурация учетных данных
    gmail_user = "gsp672021@gmail.com"
    app_password = "gbiylefkztnirvyh"  # Пароль без пробелов

    # Создание письма
    msg = MIMEText("Это тестовое письмо, отправленное через Python скрипт")
    msg["Subject"] = "Тестовое письмо с Python"
    msg["From"] = formataddr(("Отправитель Gmail", gmail_user))
    msg["To"] = formataddr(("Получатель Gmail", gmail_user))

    try:
        # Установка соединения с SMTP-сервером Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, app_password)
            server.sendmail(gmail_user, gmail_user, msg.as_string())
            print("Письмо успешно отправлено!")

    except Exception as e:
        print(f"Ошибка при отправке: {str(e)}")


if __name__ == "__main__":
    send_gmail()