import re
from scipy.spatial import distance
f = open("sentences.txt", 'r')
text = f.readlines()
words_dict = {}
index = 0
# приводим весь текст к нижнему регистру, удаляем символы и пустые строки
for i in range(len(text)):
    text[i] = text[i].lower()
    text[i] = re.split('[^a-z]', text[i])
    for k in range(text[i].count('')):
        text[i].remove('')

# создаем словарь пронумерованных слов в тексте
text_set = set(sum(text, []))  # возможно, делать нужно не так, но эта функция делает из двумерного массива одномерный
index = 0
for i in text_set:
    words_dict[i] = index
    index += 1

matrix = [[0] * 254 for i in range(22)]

for i in range(len(text)):
    for k in range(len(text[i])):
        for j in words_dict.keys():
            if j == text[i][k]:
                matrix[i][words_dict[j]] += 1
output = open('output.txt', 'w')
for i in range(1, len(matrix)):
    output.write(distance.cosine(matrix[i], matrix[0]) + ' ')

f.close()
output.close()


        
    
















