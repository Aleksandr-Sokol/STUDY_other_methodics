Flask. Send mail every day by Flask

Сервер на Python/ Flask - автоматическая отправка писем при запуске.
К письмо может быть приложено изображение, которое автоматически загружается из выбранной директории.
Для отправки писем используется flask-mail.
Библиотека APScheduler используется для ежедневной, автоматической отправки писем.

Настройка ведется в файле conf.py
configuration_data = {
    'mail_login': 'aleksandr.sokol.mail@gmail.com',
    'mail_password': '7K185PXz',
    'mail_recipients': 'aleksandr__sokol@mail.ru',
    'directory': r'E:\WORK\Python\Flask\image',
    'file_name': 'im.bmp',
    'sent_time': '17:00:00',
}
в нем: 'mail_login' и 'mail_password' — логин и пароль от почты gmail (этот почтовый клиент хорошо взаимодействует с библиотекой flask-mail)
'mail_recipients' — адрес на который отправляется почта
'directory' и 'file_name' — соответственно имя директории и прилагаемого к письму файла с изображением
'sent_time' — время ежедневной отправки файла (настраиваются только часы)