from app import db, Products, Orders, Customers

db.drop_all()
db.create_all()

# Create products
bread = Products(
    name = "bread",
    price = 0.99
)

beans = Products(
    name = "beans",
    price = 0.39
)

pack_of_oranges = Products(
    name = "pack of oranges",
    price = 1.90
)

db.session.add(bread)
db.session.add(beans)
db.session.add(pack_of_oranges)
db.session.commit()

# Create customers
harry = Customers(
    name = "Harry" 
)

tiffany = Customers(
    name = "Tiffany" 
)

db.session.add(harry)
db.session.add(tiffany)
db.session.commit()

# Create orders
harrys_shopping_list = [
    (pack_of_oranges, 2),
    (beans, 4)
]

tiffanys_shopping_list = [
    (beans, 1),
    (bread, 10)
]

for item in harrys_shopping_list:
    order = Orders(
        customer_id = harry.id,
        product_id = item[0].id,
        quantity = item[1]
    )
    db.session.add(order)
    db.session.commit()

for item in tiffanys_shopping_list:
    order = Orders(
        customer_id = tiffany.id,
        product_id = item[0].id,
        quantity = item[1]
    )
    db.session.add(order)
    db.session.commit()

# Display orders
print(f"Tiffany ordered:")
for order in tiffany.orders:
    print(f"- {order.quantity} {order.product.name} for £{order.quantity * order.product.price}")

print(f"Harry ordered:")
for order in harry.orders:
    print(f"- {order.quantity} {order.product.name} for £{order.quantity * order.product.price}")