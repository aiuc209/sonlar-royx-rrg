def clamp(son):
    if son < 0:
        return 0
    elif son > 100:
        return 100
    else:
        return son

sonlar = [150, -20, 50, 120, -10]
yangi_sonlar = [clamp(son) for son in sonlar]
print(yangi_sonlar)
