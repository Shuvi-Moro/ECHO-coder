def sings (txtlist):
	end_list = []
	num = len (txtlist)
	le = str (txtlist.pop (0))
	txt = list (txtlist)
	a = lengs (le)
	q2 = 0
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
			c = str (txtlist.pop (0))
			num = len (txtlist)
			while (i == 1):
				try:
					txtlist.remove (c)
				except ValueError:
					end_list.append (c)
					i -= 1
		num = len (txt)
		q1 = len (end_list)
		if (q1 != q2):
			print (str (len (end_list)) + " знаков готово")
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
			print ("   " + str (sing_list[i]) + " = " + str (txtlist.count (sing_list[i])))
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
		a = list (str (input ("Напишите порядок символов для сортировки:\n")))
	else:
		a = []
	return a

def reg(txtrw, register):
	if (register == "нет" or register == "0"):
		a = txtrw.upper ()
	else:
		a = txtrw
	return a