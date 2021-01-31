# Домашка
# 1. Создать классы Oxygen, Chlorine, Iron. (Один на выбор)
# 2. В качестве свойств описать температуру замерзания, плавления, испарения
# 3. Написать метод agg_state(self, t), который принимает температуру в 
# градусах цельсия и возвращает строчное представление текущего агрегатного состояния." 
# 4. Добавить параметр шкалы измерения (цельсий, фаренгейт, кельвин).
# 5. Создать родительский класс Element, в котором будут содержаться
# все методы.
# 6. Добавить метод для конвертации из одной шкалы в другую.



class Element(object):
	temp_freezing = 0
	temp_melting = -218
	temp_evaporation = -182
	scale = ''

	def agg_state(self, t):
		if t < self.temp_melting:
			return 'solid'
		elif t >= self.temp_melting and t < self.temp_evaporation:
			return "liquid"
		else:
			return "Gas"
	# def convert_temp(self, t, scale):
	# 	final_temp = 0.0
	# 	if scale == 'k':
	# 		final_temp = t + 273.15
	# 	elif scale == 'f':
	# 		final_temp = (t * 1.8) + 32
	# 	else:
	# 		raise Exception('Bad Temperature Scale')
	# 	return final_temp



class Oxygen(Element):
	def convert_temp(self, t, scale):
		final_temp = 0.0
		if scale == 'k':
			final_temp = t + 273.15
		elif scale == 'f':
			final_temp = (t * 1.8) + 32
		else:
			raise Exception('Bad Temperature Scale')
		return final_temp

oxygen = Element();

temp_oxygen = int(input("Please input temperature for oxygen in C: " ))
print(oxygen.agg_state(temp_oxygen))


convertTemp = Oxygen();
input_temp = float(input("Please input temperature for convert in C: " ))
scale_input = input('(k) or (f)?: ')

print(convertTemp.convert_temp(input_temp, scale_input))


