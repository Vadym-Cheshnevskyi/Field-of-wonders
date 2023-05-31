"""
Створити програму - гру "Поле чудес".

Зареєструватись на github, та створити окремий репозиторій для цього завдання

1. Програма буде брати зі списку слів одне рандомне слово.
2. Програма буде отримувати від користувача число - кількість спроб вгадати
3. Далі програма буде чекати від користувача або букву, або ціле слово.
4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме число,
якщо так то говорити що користувач вгадав слово, або писати що слово не правильне.
5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові,
та якщо є, виводити наше слово, де зірочками будуть закриті всі літери,
які користувач ще не вгадав, або "Такої літери немає"
6. Якщо кількість спроб закінчиться, потрібно сказати користувачю,
що він програв та закінчити роботу програми.

Приклад:
Програмою обрано слово "apple"
Вхід: 10 (10 спроб вгадати слово)
Вхід: "a"
Вихід: "a****"
Вхід: "d"
Вихід: "Такої літери немає"
Вхід: "l"
Вихід: "a**l*"
Вхід: "e"
Вихід: "a**le"
Вхід: "apple"
Вихід: "Вітаю, ви вгадали слово"

Код програми залейте до вашого репозиторію та надішліть посилання у відповідь.
"""
import random
import re

text = "Person Time Year Way Day Man Government Company Hand Part Place Case Group Problem Fact Child System Fact Point Government Company Hand Part Place Case Group Problem Fact Child System Thing Eye Woman Life Child World School State Family Student Group Country Problem Hand Part Place Case Week Company System Program Question Work Government Number Night Point Home Water Room Mother Area Money Story Fact Month Lot Right Study Book Eye Job Word Business Issue Side Kind Head House Service Friend Father Power Hour Game Line End Member Law Car City Community Name President Team Minute Idea Kid Body Information"
text = text.lower()
text_list = text.split()
word = random.choice(text_list)
word2 = word.upper()

#print(word)
#print(word2)
question = list('*' * len(word))
print("".join(question))
victory = False
attempts = int(input('За скільки спроб ви вгадаєте слово? '))
stars_letters = list(range(0, len(word)))
while attempts >= 1:
    answer = input('Буква або слово? ')
    answer = answer.upper()
    if len(answer) > 1:
        if answer.lower() == word:
            victory = True
            attempts = 0
        else:
            victory = False
            attempts = 0
    elif len(answer) == 1:
        word2 = re.sub(answer, answer.lower(), word2)
        win = False
        for i in stars_letters:
            if word2[i] == word2[i].lower():
                question[i] = word[i]
                stars_letters.remove(i)
                win = True
        attempts -= 1
        if not win:
            print('Такої літери немає')
        else:
            print("".join(question))

    if word == "".join(question):
        victory = True
        attempts = 0
if victory:
    print('Вітаю, ви вгадали слово.')
else:
    print('Нажаль ви програли.')
