with open('cook.txt', encoding = 'utf-8') as f:
    cook_book = {}

    dish_name_list = []
#    def dish_name_list():
#        while True:
#            dish_name = f.readline().strip()
#            if not dish_name:
#                break
#            ingridient_number = f.readline().strip()
#            ingridient_number_int = int(ingridient_number)
#
#            for i in range(ingridient_number_int):
#                f.readline()  # пустая строка
#            f.readline()
#            dish_name_list.append(dish_name)
#        print(dish_name_list)
#        return dish_name_list
#    def ingridient_list():
    dishes_dic = {}
    ingridient_list = {}
    while True:
        f.readline()
        ingridient_number = f.readline().strip()

        if not ingridient_number:
            break

        for i in range(int(ingridient_number)):
            str_strip = f.readline().strip()
            str = str_strip.split(' | ')
            dishes_dic['ingridient_name'] = str[0]
            dishes_dic['quantity'] = int(str[1])
            dishes_dic['measure'] = str[2]
 #           return dishes_dic
        f.readline()










