import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])



print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_carts = pd.merge(visits, cart, how='left')

print(visits_carts)

print(len(visits_carts))

print(visits_carts[visits_carts.cart_time.isnull()])

len_visits = float(len(visits_carts))
len_cart_null = float(len(visits_carts[visits_carts.cart_time.isnull()]))
percent_cart_cull = float(((100 * len_cart_null)/len_visits))
print(percent_cart_cull)

cart_checkout = pd.merge(cart, checkout, how='left')
no_purchase_cart = float(len(cart_checkout[cart_checkout.cart_time.notnull()]))
checkout_null = float(len(cart_checkout[cart_checkout.checkout_time.notnull()]))

percentage_no_purchase = float(((100*checkout_null)/no_purchase_cart))
print(percentage_no_purchase)