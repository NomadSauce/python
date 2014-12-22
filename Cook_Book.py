class mealPlan(object):
    def __init__(self, meal, price):
        self.meal = meal
        self.price = price
        
class meat(object):
    def __init__(self, meatName, weight):
        self.meatName = meatName
        self.weight = weight
        
    def __str__(self):
        return self.meatName
        
class recipe(object):
    def __init__(self, spiceList):
    	self.spiceList = []
	
    def spice(self, spiceID, amount):
        spice = {}
	spice['Spice Name'] = raw_input('Spice Name: ')
	spice['Amount'] = raw_input('Amount: ')
	
p = meat("chicken", "1")
str(p)
