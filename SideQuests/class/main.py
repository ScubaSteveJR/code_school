from item import Item
from phone import Phone

# phone1 = Phone("jscPhonev10", 500, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20", 700, 5, 1)

Item.from_csv()

print(Item.all)
