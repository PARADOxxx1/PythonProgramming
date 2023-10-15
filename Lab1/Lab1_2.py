# TODO Найдите количество книг, которое можно разместить на дискете

disk_memory_bites = 1.44 * (2 ** 20)
pages_book = 100
str_page = 50
symb_str = 25
symb_memory = 4
print("Количество книг, помещающихся на дискету:", disk_memory_bites // (symb_str * str_page * pages_book * symb_memory))
