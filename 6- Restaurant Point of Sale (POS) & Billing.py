menu = {101:("Gourmet Burger",12.50),
        102:("Garlic Fries",5.00),
        103:("Soda",2.50)
        }
order = []
subTotal = 0
while True:
    itemId = int(input("Enter Your Item I'd what you wanna Order : "))

    if itemId == 0:
        break

    if itemId in menu:
        quantity = int(input("Enter Quantity : "))
        if quantity > 0:
            itemName = menu[itemId][0]
            unitPrice = menu[itemId][1]
            total = unitPrice * quantity
            subTotal += total

            orderList = (itemName,quantity,total)
            order.append(orderList)

            if subTotal > 50:
                discount = 5
            else:
                discount = 0
    else:
        print("Please input valid Item I'd.")

tax = subTotal * 0.08
finalAmount = (subTotal + tax) - discount
print(50 * "=")
print("GOURMET BISTRO RECEIPT".center(50))
print(50 * "=")
print(f"{"Item":<15} | {"Qty":<4} | {"Unit Price":<10} | {"Total ($)":<4}")
print(50 * "-")

for itemId,quantity,total in order:
    unitPrice = total / quantity
    print(f"{itemId:<15} | {quantity:<4} | ${unitPrice:<9.2f} | ${total:<3.2f}")

print(50 * "-")
print(f"Subtotal        : ${subTotal:.2f}")
print(f"Tax             : ${tax:.2f}")
print(f"Final Amount    : ${finalAmount:.2f}")







# menu_items = {"Gourmet Burger":12.50,
#               "Garlic Fries":5.00,
#               "Soda":2.50}
# subtotal = 0
# unit_price = 0
# print(50 * "=")
# print("GOURMET BISTRO RECEIPT".center(50))
# print(50 * "=")
# print(f"{"Item":<15} | {"Qty":<4} | {"Unit Price":<10} | {"Total":<5}")
# print(50 * "-")
# for order,unit_price in menu_items.items():
#     if order in menu_items:
#         if order == 'Gourmet Burger':
#             quantity = 2
#             total = unit_price * quantity
#             subtotal += total
#         elif order == "Garlic Fries":
#             quantity = 1
#             total = unit_price * quantity
#             subtotal += total
#         elif order == "Soda":
#             quantity = 2
#             total = unit_price * quantity
#             subtotal += total
#         else:
#             unit_price = 0
#             total = unit_price * quantity
#     else:
#         print("item out of stock")
#     print(f"{order:<15} | {quantity:<4} | ${unit_price:<9.2f} | ${total:<5.2f}")
# tax = (subtotal * 8) / 100
# final_amount = subtotal + tax
# print(50 * "-")
# print(f"Subtotal        : ${subtotal:.2f}")
# print(f"Tax (8%)        : ${tax:.2f}")
# print(f"Final Amount    : ${final_amount:.2f}")
# print(50 * "=")