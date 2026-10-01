inventory = {101:{'name':"Laptop",'price':800.00,'stock':10},
             102:{'name':"Mouse",'price':25.00,'stock':45},
             103:{'name':"Keyboard",'price':50.00,'stock':12}
}
def purchase_item(item_id,quantity):
    if item_id in inventory and inventory[item_id]['stock'] > quantity:
        inventory[item_id]['stock'] -= quantity
    else:
        print("purchase item is not available in stock.")
purchase_item(101,2)
threshold = 10
total_valuation = 0
low_stock = 0
print(50 * "=")
print("E-Commerce Stock Report".center(50))
print(50 * "=")
print(f"{"ID":<3} | {"Name":<10} | {"Price(₹)":<9} | {"Stock":<5} | {"Status":<5}")
for item_id,details in inventory.items():
    name = details['name']
    price = details['price']
    stock = details['stock']
    total_valuation += (price * stock)
    if stock < threshold:
        status = "LOW STOCK"
        low_stock += 1
    else:
        status = "IN STOCK"
    print(f"{item_id:<2} | {name:<10} | {price:<9} | {stock:<5} | {status:<5}")
print(50 * "-")
print(f"Total Inventory Valuation : ₹ {total_valuation}")
print(f"Low Stock items Count : {low_stock}")
print(50 * "=")
