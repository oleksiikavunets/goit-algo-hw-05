import timeit
from pathlib import Path

from searches.boyer_moore_search import boyer_moore_search
from searches.kmp_search import kmp_search
from searches.rabin_karp_search import rabin_karp_search

existing_substr_1 = 'Двійковий або логарифмічний пошук часто використовується через швидкий час пошуку'
existing_substr_2 = 'Метою даної роботи є дослідження та програмна реалізація методів і структур даних'
non_existing_substr = 'два крокодила'

with open(Path('resources/text1.txt'), 'r') as text1:
    content1 = text1.read()

with open(Path('resources/text2.txt'), 'r') as text2:
    content2 = text2.read()

bm_exist1 = timeit.timeit(lambda: boyer_moore_search(content1, existing_substr_1), number=1)
bm_non_exist1 = timeit.timeit(lambda: boyer_moore_search(content1, non_existing_substr), number=1)

kmp_exist1 = timeit.timeit(lambda: kmp_search(content1, existing_substr_1), number=1)
kmp_non_exist1 = timeit.timeit(lambda: kmp_search(content1, non_existing_substr), number=1)

rk_exist1 = timeit.timeit(lambda: rabin_karp_search(content1, existing_substr_1), number=1)
rk_non_exist1 = timeit.timeit(lambda: rabin_karp_search(content1, non_existing_substr), number=1)

bm_exist2 = timeit.timeit(lambda: boyer_moore_search(content2, existing_substr_1), number=1)
bm_non_exist2 = timeit.timeit(lambda: boyer_moore_search(content2, non_existing_substr), number=1)

kmp_exist2 = timeit.timeit(lambda: kmp_search(content2, existing_substr_1), number=1)
kmp_non_exist2 = timeit.timeit(lambda: kmp_search(content2, non_existing_substr), number=1)

rk_exist2 = timeit.timeit(lambda: rabin_karp_search(content2, existing_substr_1), number=1)
rk_non_exist2 = timeit.timeit(lambda: rabin_karp_search(content2, non_existing_substr), number=1)

print('Текст 1:')
print('Існуючий підрядок:')
print(f'Боєр-Мур:          {bm_exist1}')
print(f'Кнут-Морріс-Пратт: {kmp_exist1}')
print(f'Рабін-Карп:        {rk_exist1}')
print('\nНеіснуючий підрядок:')
print(f'Боєр-Мур:          {bm_non_exist1}')
print(f'Кнут-Морріс-Пратт: {kmp_non_exist1}')
print(f'Рабін-Карп:        {rk_non_exist1}')
print('=' * 40)
print()
print('Текст 2:')
print(f'Боєр-Мур:          {bm_exist2}')
print(f'Кнут-Морріс-Пратт: {kmp_exist2}')
print(f'Рабін-Карп:        {rk_exist2}')
print('\nНеіснуючий підрядок:')
print(f'Боєр-Мур:          {bm_non_exist2}')
print(f'Кнут-Морріс-Пратт: {kmp_non_exist2}')
print(f'Рабін-Карп:        {rk_non_exist2}')
