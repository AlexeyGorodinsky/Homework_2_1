
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
            print(dishes_dic)
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()