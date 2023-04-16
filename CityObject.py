class CityObject:
    def __init__(self, name, obj_type, position):
        self.name = name
        self.type = obj_type
        self.position = position

class Magasin(CityObject):
    def __init__(self, name, position):
        super().__init__(name, "magasin", position)
        
class Entrepot(CityObject):
    def __init__(self, name, position):
        super().__init__(name, "entrepot", position)
        self.stock = {}  # dictionnaire pour stocker les produits

    def add_product(self, product, quantity):
        if product in self.stock:
            self.stock[product] += quantity
        else:
            self.stock[product] = quantity

    def remove_product(self, product, quantity):
        if product in self.stock:
            if self.stock[product] >= quantity:
                self.stock[product] -= quantity
                return True
        return False

        
class StationRecharge(CityObject):
    def __init__(self, name, position):
        super().__init__(name, "station de recharge", position)