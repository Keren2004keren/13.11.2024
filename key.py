# START
import random

cities: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
# a
print(sorted(cities, key=lambda city: len(city)))
# b
print(sorted(cities, key=lambda city: len(city.split())))
# c
print(sorted(cities, key=lambda city: city[-1]))
# d
print(sorted(cities, key=lambda city: city[::-1]))
# e
print(sorted(cities, key=lambda city: city.lower().count("a")))
# f
mil_cont: list[object] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050, "Europe"],
                          ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"],
                          ["Shanghai", 4920, "Asia"]]
# 1
print(sorted(mil_cont, key=lambda city: city[1]))
# 2
print(sorted(mil_cont, key=lambda city: city[1], reverse=True))
# 3
print(sorted(mil_cont, key=lambda city: city[2]))
# 4
print(sorted(mil_cont, key=lambda city: (city[2], city[1])))

rand_num: list[int] = [random.randint(1, 100) for _ in range(50)]
print(rand_num)
print(sorted(rand_num))
print(sorted(rand_num, key=lambda num: abs(num - (sum(rand_num) / 50))))

# STOP
