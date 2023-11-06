import copy


class Shop:
       def __init__(self,*items):
            self.stock = list(items)
       def list_items(self):
             a = 'In stock:\n'
             for item in self.stock:
              if item.amount > 0:
                      a += f"{item.name},{item.amount}\n"
             return a 
       def buy(self,item_name,item_amount = 1):
              for item in self.stock:
                     if item_name == item.name:
                            item.decrease_amount(item_amount)
                            break
              else: 
                     raise ValueError('Товара нет в наличии')
              item_copy = copy.deepcopy(item)
              item_copy.set_amount(item_amount)
              return item_copy
       def sell(self,item,amount=1):
           item.decrease_amount(amount)
           for stock_items in self.stock:
               if stock_items.name == item.name:
                  stock_items.increase_amount(amount)
                  break
           else:
               item_copy = copy.deepcopy(item)
               item_copy.set_amount(amount)
               self.stock.append
class Item:
       def __init__(self,name,amount=1,rarrity='common'):
             self.name = name
             self.amount = amount
             self.rarrity = rarrity
       def set_amount(self,value):
             if value < 0:
                   raise ValueError('Количество товара меньше нуля')
             self.amount  = value
       def decrease_amount(self,value=1):
             if self.amount - value >= 0:
                self.amount -= value
             else:
                  raise ValueError('Сумма товаров не может быть меньше нуля')
       def increase_amount(self,value=1):
              if value < 0:
                  raise ValueError('Количество товара меньше нуля')
              self.amount += value
shop = Shop(Item('shirt',1),Item('shorts',14))
print(shop.list_items())
purchased_items = shop.buy('shirt',2)
print(purchased_items.name, purchased_items.amount)
shop.sell(Item('shoes',1),1)
print(shop.list_items())