# class Car:
# 	color = 'red'
# 	top_speed = 250

# # создаем объект
# zaz = Car()	
# toyota = Car()

# zaz.top_speed = 140

# a = Car
# bmw = a()
# print(bmw.color)

# print(zaz.top_speed)
# print(toyota.top_speed)
# # print(dir([]))

# class SmartPhone:
# 	brand = ''
# 	price = 0

# 	def call(self, name):
# 		return '{} Ring ring to {}'.format(self.brand, name)

# 	# def print_self(self):
# 	# 	return self



# samsung = SmartPhone()
# samsung.brand = 'samsung'
# samsung.price = 500
# print(samsung.call('Lera'))

# xiaomi = SmartPhone()
# xiaomi.brand = 'xiaomi'
# xiaomi.price = 100
# # print(xiaomi.call())



class SmartPhone(object):
	brand = ''
	price = 0

	phone_book = {}

	def call(self, name):
		# self.shutdown()


		return 'Call to {}'.format(self.phone_book[name])

# 	def shutdown(self):
# 		print("Shutdown !!!!!!22211111!!!!")


# siemens = SmartPhone()
# siemens.brand = 'siemens'
# siemens.price = 50
# siemens.phone_book = {'Yana':'80043221', 'Maks': '938829923'}
# print(siemens.call('Maks'))

# iphone = SmartPhone()
# iphone.brand = 'iphone'
# iphone.price = 1300
# iphone.phone_book = {'steve': '12334', 'tim': "09876"}
# print(iphone.call('tim'))


class Phone(SmartPhone):
	def call(self, number):
		return 'Ring Ring to {}'.format(number)

iphone = SmartPhone()
iphone.brand = 'apple'

nokia = Phone()
nokia.brand = '1100'

# print(iphone.call('vasya'))
print(nokia.call('99339393'))