#desafio

work_tue = False
work_wed = False

tv50_sorv = work_tue and work_wed
tv32_sorv = work_tue != work_wed
sorvete = work_tue or work_wed
mais_saudavel = not sorvete

print('tv50 = {} \n Tv32= {} \n Sorvete={} \n saudavel+{}'.format(tv50_sorv,tv32_sorv,sorvete,mais_saudavel))