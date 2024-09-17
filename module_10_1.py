from time import sleep
from threading import Thread
from datetime import datetime


def waite_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()

waite_words(10, 'example1.txt')
waite_words(30, 'example2.txt')
waite_words(200, 'example3.txt')
waite_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Работа потоков: {time_end - time_start}')

time_start = datetime.now()

thr_first = Thread(target=waite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=waite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=waite_words, args=(200, 'example7.txt'))
thr_four = Thread(target=waite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()

time_end = datetime.now()
print(f'Работа потоков: {time_end - time_start}')
