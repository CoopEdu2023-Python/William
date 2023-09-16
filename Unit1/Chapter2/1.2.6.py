pay = 13999
pay *= 0.095
pay = 13999 - 200 - pay
m = 67890 // int(pay)    # m为购买的数量
m = int(m)
sheng = 67890 - (m * int(pay))
sheng = sheng * 13
print(sheng)