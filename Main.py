from goods.Bulb import *
from goods.Switch import *
from LightHouseManager import *
from goods.Lamp import *

if __name__ == '__main__':
    lightHouseManager = LightHouseManager()

    bulb1 = Bulb("Cool", 15.0, "LED", 5, "Red", "Econom", "Triangular")
    bulb2 = Bulb("Excellent", 25.0, "LED", 25, "Yellow", "Super", "Round")
    bulb3 = Bulb("+++", 35.0, "LED", 50, "X-Ray", "Rich", "Angular")
    lamp1 = Lamp("Lalala", 56.5, "Bosch", "Plastic", 36, "Good")
    lamp2 = Lamp("LADA", 50.5, "Bosch", "Glass", 26, "Good+")
    lamp3 = Lamp("Happy", 16.5, "Bosch", "Wood", 6, "Good++")
    switch1 = Switch("Better", 2.0, "Tarantino", "Plastic", 5, "Blue")
    switch2 = Switch("Worst", 1.0, "USSR", "Wooden", 15, "Red")

    lightHouseManager.goods = [bulb1, bulb2, bulb3, lamp1, lamp2, lamp3, switch1, switch2]
    print("Initial list:")
    lightHouseManager.print_list()

    lightHouseManager.sort_by_price()
    print("Sorted list")
    lightHouseManager.print_list()

    lightHouseManager.goods = lightHouseManager.find_by_type(GoodsType.LAMP, 51.0)
    print("Found list:")
    lightHouseManager.print_list()

    pass
