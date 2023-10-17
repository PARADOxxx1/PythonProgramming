# TODO Найдите количество книг, которое можно разместить на дискете

disk_memory_kilobites = 1.44
bites_in_kilobites = 2 ** 20
disk_memory_bites = disk_memory_kilobites * bites_in_kilobites
pages_book = 100
str_page = 50
symb_str = 25
symb_memory = 4
print("Количество книг, помещающихся на дискету:", disk_memory_bites // (symb_str * str_page * pages_book * symb_memory))
