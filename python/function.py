def sings (txtlist):
	end_list = []
	num = len (txtlist)
	le = str (txtlist.pop (0))
	txt = list (txtlist)
	a = lengs (le)
	q2 = 0
	iii = 1
	while (num >= 1):
		i = 1
		ii = 1
		txt2 = list (txt)
		try:
			b = str (a.pop (0))
		except:
			b = "nope"		
		if (le != "ns"):
			while (ii == 1):
				try:
					c = str (txt2.pop (0))
				except:
					с = "XD"
					i -= 1
					ii -= 1
				if (c == b or b == "nope"):
					while (i == 1):
						try:
							txt.remove (c)
						except ValueError:
							end_list.append (c)
							i -= 1
							ii -= 1
		else:
			while (ii == 1):
				try:
					c = str (txt2.pop (0))
				except:
					с = "XD"
					i -= 1
					ii -= 1
				if (c == b or b == "nope"):
					while (i == 1):
						try:
							txt.remove (c)
						except ValueError:
							end_list.append (c)
							i -= 1
							ii -= 1
		num = len (txt)
		q1 = len (end_list)
		if (q1 != q2):
			if (iii == 1):
				print ("\n")
				iii -= 1
			print (" >>> " + str (len (end_list)) + " знаков готово")
		q2 = q1
	return end_list

def get_sings (txtrw):
	txtlist = list (txtrw)
	sing_list = sings (txtlist)
	return sing_list

def print_info (rwtxtpls, txtrw):
	sing_list = get_sings (rwtxtpls)
	txtlist = list (str (txtrw))
	print ("\n	Информация о знаках в тексте:\n\n   " + str (txtrw))
	print ("\n	Колличество знаков = " + str (len (txtrw)) + "\n")
	leng_info (sing_list, txtlist)

def leng_info (sing_list, txtlist):
	manh = 0
	i = 0
	while (manh == 0):
		try:
			print ("   \" " + str (sing_list[i]) + " \" = " + str (txtlist.count (sing_list[i])))
			i += 1 
		except:
			print ("\n" + "	Разных знаков в тексте = " + str (i))
			manh = 1

def leng_sort (leng, txtrw):
	try:
		if (leng == "ru" or leng == "1" or leng == "eng" or leng == "2" or leng == "custom" or leng == "0"):
			if (leng == "ru" or leng == "1"):
				txtrw.reverse ()
				txtrw.append ("rus")
				txtrw.reverse ()
				return txtrw
			elif (leng == "eng" or leng == "2"):
				txtrw.reverse ()
				txtrw.append ("eng")
				txtrw.reverse ()
				return txtrw
			elif (leng == "custom" or leng == "0"):
				txtrw.reverse ()
				txtrw.append ("cst")
				txtrw.reverse ()
				return txtrw
		else:
			txtrw.reverse ()
			txtrw.append ("ns")
			txtrw.reverse ()
			return txtrw
	except:
		txtrw.reverse ()
		txtrw.append ("ns")
		txtrw.reverse ()
		return txtrw

def lengs (le):
	if (le == "rus"):
		a = list (" АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯяAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890")
	elif (le == "eng"):
		a = list (" AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzАаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя1234567890")
	elif (le == "cst"):
		a = list (str (input ("Напишите порядок символов для сортировки:\n >>> ")))
	else:
		a = []
	return a

def reg (txtrw, register):
	if (register == "нет" or register == "0"):
		a = txtrw.upper ()
	else:
		a = txtrw
	return a

def wdoing (wd):
	if (wd == "0"):
		txtrw = input ("\nНапишите текст:\n >>> ")
		register =  str (input ("""\nДелать разделение по регистру?
Пример ==> \"да\" или \"нет\", если пропустить то да\n >>> """))
		txtrw2 = reg (txtrw, register)
		leng = str (input ("""\nНапишите язык на котором это делать сортировку:
Пример ==> \"русский\" ru или 1, \"ангельский XD\" eng или 2 либо \"кастомную сортировку\" custom или 0\n >>> """))
		txtrwlist = list (txtrw2)
		rwtxtpls = leng_sort (leng, txtrwlist)
		print_info (rwtxtpls, txtrw2)
	elif (wd == "1"):
		met = input ("\nМетод шифрования:\nAT-BUSH - 0\nЦезарь  - 1\nЗамена  - 2\n >>> ")
		txtrw = input ("\nНапишите текст:\n >>> ")
		leng = input ("""\nНа каком языке проводить шифрование:
Пример ==> \"русский\" rus или 1, \"ангельский XD\" eng или 2 либо \"кастомную сортировку\" custom или 0\n >>> """)
		if (met == "0"):
			at_bash_endecoder (txtrw, leng)
		elif (met == "1"):
			cezar_encoder (txtrw, leng)
	elif (wd == "2"):
		met = input ("\nМетод дешифрования:\nAT-BUSH - 0\nЦезарь  - 1\nЗамена  - 2\n >>> ")
		txtrw = input ("\nНапишите текст:\n >>> ")
		leng = input ("""\nНа каком языке проводить шифрование:
Пример ==> \"русский\" rus или 1, \"ангельский XD\" eng или 2 либо \"кастомную сортировку\" custom или 0\n >>> """)
		if (met == "0"):
			at_bash_endecoder (txtrw, leng)
		elif (met == "1"):
			knon = input ("\nИзвестно ли смещение?\nЕсли \"да\" то 1 или \"нет\" то 0 или ничего\n >>> ")
			if (knon == "да" or knon == "1"):
				cezar_encoder (txtrw, leng)
			elif (knon == "нет" or knon == "0"):
				cezar_decoder (txtrw, leng)
			else:
				cezar_decoder (txtrw, leng)
	else:
		pass

def coder_lengs (le):
	if (le == "rus" or "1"):
		a = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
		b = input ("\nНапишите дополнительные знаки для шифратора/дешифратора (в нужном порядке)\nЕсли не требуется ни чего, кроме алфавита, просто нажмите enter\n >>> ")
		c = b + a
		return c
	elif (le == "eng" or "2"):
		a = list ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		b = list (input ("\nНапишите дополнительные знаки для шифратора/дешифратора (в нужном порядке)\nЕсли не требуется ни чего, кроме алфавита, просто нажмите enter\n >>> "))
		c = a.extend (b)
		return c
	elif (le == "cst" or "0"):
		a = list (input ("\nНапишите дополнительные знаки для шифратора/дешифратора (в нужном порядке)\nЕсли надо зашифровать среди символов из текста нажмите enter\n >>> "))
		return a
	else:
		print ( " >>> ERROR " )

def at_bash_endecoder (txtrw, leng):
	txt = list (txtrw.upper ())
	text = txt
	alf = list (coder_lengs (leng))
	end_list = []
	try:
		alf.reverse ()
		revalf = list (alf)
		alf.reverse ()
	except:
		print ( " >>> ERROR " )
	i = 1
	ii = 0
	space = str (input ("\nУбираем ли пробелы:\nЕсли \"да\" то 1 или \"нет\" то 0 или ничего\n >>> "))
	print ("")
	if (space == "да" or space == "1"):
		while (text.count (" ") >= 1):
			text.remove (" ")
	else:
		pass
	while (i == 1):
		text = txt
		try:
			poptext = text.pop (ii)
			try:
				ind = int (alf.index (poptext))
				a = revalf.pop (ind)
				end_list.append (a)
				revalf.insert (ind, a)
			except:
				end_list.append (poptext)
		except:
			i -= 1
	end = ''.join (end_list)
	print ("\nОтвет:\n >>> " + end)

def cezar_encoder (txtrw, leng):
	txt = list (txtrw.upper ())
	text = txt
	alf = list (coder_lengs (leng))
	end_list = []
	i = 1
	ii = 0
	space = str (input ("\nУбираем ли пробелы:\nЕсли \"да\" то 1 или \"нет\" то 0 или ничего\n >>> "))
	delta = int (input ("\nНа какое значение смещать:\nВведите число смещения (1, 2... или -1, -2...)\n >>> "))
	print ("")
	if (space == "да" or space == "1"):
		while (text.count (" ") >= 1):
			text.remove (" ")
	else:
		pass
	while (i == 1):
		text = txt
		alf2 = list (alf)
		try:
			poptext = text.pop (ii)
			try:
				ind = int (alf2.index (poptext)) + delta
				if (ind > len (alf2) or ind < 0):
					if (ind > len (alf2)):
					 	ind -= len (alf2)
					elif (ind < 0):
						ind += len (alf2)
				a = alf2.pop (ind)
				end_list.append (a)
			except:
				end_list.append (poptext)
		except:
			i -= 1
	end = ''.join (end_list)
	print ("\nОтвет:\n >>> " + end)

def cezar_decoder (txtrw, leng):
	txt = list (txtrw.upper ())
	text = list (txt)
	alf = list (coder_lengs (leng))
	end_list = list ("")
	end_list.clear ()
	i = 1
	iii = 0
	while (iii <= len (alf)):
		text = list (txt)
		while (i == 1):
			alf2 = list (alf)
			try:
				poptext = text.pop (0)
				try:
					ind = int (alf2.index (poptext)) + iii
					if (ind > len (alf2) or ind < 0):
						if (ind > len (alf2)):
						 	ind -= len (alf2)
						elif (ind < 0):
							ind += len (alf2)
					a = alf2.pop (ind)
					end_list.append (a)
				except:
					end_list.append (poptext)
			except:
				i -= 1
		end = ''.join (end_list)			
		print ("\nСмещение " + str(iii) + ":\n >>> " + end)
		iii += 1
		end_list.clear ()
		i += 1
	print ("")