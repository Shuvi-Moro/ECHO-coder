import function as func
txtrw = input ("Напишите текст:\n")
register =  str (input ("""\nДелать разделение по регистру?
Пример ==> \"да\" да или 1, \"нет\" нет или 0\n	"""))
txtrw2 = func.reg (txtrw, register)
leng = str (input ("""\nНапишите язык на котором это делать сортировку:
Пример ==> \"русский\" ru или 1, \"ангельский XD\" eng или 2 либо \"кастомную сортировку\" custom или 0\n	"""))
txtrwlist = list (txtrw2)
rwtxtpls = func.leng_sort (leng, txtrwlist)
func.print_info (rwtxtpls, txtrw2)