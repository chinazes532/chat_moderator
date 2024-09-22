# chat_moderator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<h1>Описание бота</h1>

Данный чат-бот является модератором в чате.
Бот может блокировать и мутить на определенное время пользователей чата.
Также бот привествтует новых участников чата.

Бот блокирует пользователя, если у него накопилось 3 предупреждения.
Также можно при помощи команды снять ограничения и разблокировать пользователя.

Бот написан на Python Aiogram3 Aiosqlite

<h2>Основные команды бота</h2>
<ol>
    <li><code>/warn</code> - выдает пользователю предупреждение</li>
    <li><code>/unwarn</code> - снимает с пользователя все предупреждения</li>
    <li><code>/mute 1h</code> - заглушает пользователя на определенное время. Первая цифра - количество временных единиц. Буква - временная единица.</li>
</ol>

<h1>Установка и запуск</h1>
<ol>
    <li>Python 3.9 и выше</li>
    <li>Выбрать в главном меню "Get from VCS" и вставить данную ссылку: <code>https://github.com/chinazes532/anonymous-questions-bot.git</code></li>
    <li>Установить нужные зависиомсти, при помощи: <code>pip install -r requirements.txt</code></li>
    <li>Запустите скрипт при помощи <code>python3 main.py</code></li>
</ol>
