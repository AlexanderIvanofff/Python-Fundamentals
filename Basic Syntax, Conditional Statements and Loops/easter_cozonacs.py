budget = float(input())
price_for_one_flour = float(input())

price_for_one_pack_eggs = price_for_one_flour * 0.75
price_for_one_liter_milk = price_for_one_flour * 1.25
milk_price = price_for_one_liter_milk / 4

cozonac_price = price_for_one_pack_eggs + price_for_one_liter_milk + milk_price

colored_eggs = 0
cozonac_made = 0
while budget > cozonac_price:
    cozonac_made += 1
    colored_eggs += 3

    if cozonac_made % 3 == 0:
        colored_eggs -= cozonac_made - 2

    budget -= cozonac_price

print(f'You made {cozonac_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

budget = float(input())
price_for_1_kg = float(input())

price_pack_of_eggs = price_for_1_kg * 0.75
price_for_1L_milk = price_for_1_kg * 1.25
milk_price = price_for_1L_milk / 4

cozonac_price = price_pack_of_eggs + milk_price + price_for_1_kg

colored_eggs = 0
cozonac_made = 0

while budget > cozonac_price:
    cozonac_made += 1
    colored_eggs += 3

    if cozonac_made % 3 == 0:
        colored_eggs -= cozonac_made - 2
    budget -= cozonac_price

print(f'You made {cozonac_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

