# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slice the `items` string into individual items
candy1 = items[:9]        # "Bubblegum"
candy2 = items[11:20]     # "Chocolate"
dry_goods = items[22:]     # "Pasta"

# Slice the `categories` string into individual categories
category1 = categories[:11]  # "Candy Aisle"
category2 = categories[13:]  # "Pasta Aisle"

# Preise als Strings
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# Ausgabe per f-String
print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")