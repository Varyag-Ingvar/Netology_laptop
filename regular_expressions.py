import re

text = '''
После революции 1917 года «Мистерия-буфф» Владимира Маяковского стала одной из первых пьес новой страны. 
В ней Маяковский переосмыслял библейский сюжет и традиционные концепции рая и ада, утверждал труд, движение 
и развитие как истинное новое добро. Впервые «Мистерию-буфф» поставил Всеволод Мейерхольд в 1918 году. 
Несмотря на то что пьесу высоко оценил сам Анатолий Луначарский, спектакль пришлось быстро снять.
'''

text_1 = 'После революции 1917 года «Мистерия-буфф» Владимира Маяковского стала одной из первых пьес новой страны.'

text_2 = "После революции 1917 года «Мистерия-буфф» Владимира маяковского стала одной из первых пьес новой страны. В " \
         "ней Маяковский переосмыслял библейский сюжет и традиционные концепции рая и ада, утверждал труд, " \
         "движение и развитие как истинное новое добро. Впервые «Мистерию-буфф» поставил Всеволод Мейерхольд в 1918 " \
         "году. Несмотря на то что пьесу высоко оценил сам Анатолий Луначарский, спектакль пришлось быстро снять. "

text_3 = '+7 (8512)77-45-45, 8 (495) 101-12-39, 8(8843)522-43-21'


pattern = r'\w+'

words_list = re.match(pattern, text_1)
print(words_list)
print(words_list[0])

words_list_1 = re.findall(pattern, text)
print(len(words_list_1), words_list_1)

pattern_2 = '[.?!]'
sentences_list_1 = re.split(pattern_2, text_2)
print(len(sentences_list_1), sentences_list_1)

res = re.sub(r"[М-м]аяковск\w+", "Сотона", text)
print(res)

pattern_3 = re.compile(r'(\+7|8)?\s*\((\d+)\)\s*(\d+)[-\s](\d+)[-\s](\d+)')

res_3 = pattern_3.sub(r'+7(\2)\3-\4-\5', text_3)
print(res_3)
