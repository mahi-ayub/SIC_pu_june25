total_land = 80
segment = total_land / 5

tomato_30 = segment * 0.3 * 10
tomato_70 = segment * 0.7 * 12
tomato_total = tomato_30 + tomato_70
tomato_sales = tomato_total * 1000 * 7

potato_yield = segment * 10
potato_sales = potato_yield * 1000 * 20

cabbage_yield = segment * 14
cabbage_sales = cabbage_yield * 1000 * 24

sunflower_yield = segment * 0.7
sunflower_sales = sunflower_yield * 1000 * 200

sugarcane_yield = segment * 45
sugarcane_sales = sugarcane_yield * 4000

total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
print("Total sales:", int(total_sales))

chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales
print("Chemical-free sales after 11 months:", int(chemical_free_sales))
