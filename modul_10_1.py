from datetime import datetime
from time import sleep
from threading import Thread

def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_finish = datetime.now()
time_rez = time_finish - time_start
print(time_rez)

time_start = datetime.now()
the_first = Thread(target=wite_words, args=(10, 'example5.txt'))
the_second = Thread(target=wite_words, args=(30, 'example6.txt'))
the_third = Thread(target=wite_words, args=(200, 'example7.txt'))
the_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))

the_first.start()
the_second.start()
the_third.start()
the_fourth.start()

the_first.join()
the_second.join()
the_third.join()
the_fourth.join()

time_finish = datetime.now()
time_rez = time_finish - time_start
print(time_rez)