NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

# Added dict ver example
print("DICT EXAMPLE VER 1")
dict = {"John": 20, "Paul": 21, "George": 22, "Ringo": 23}
for name in dict:
    print(name, dict[name])
    
print("DICT EXAMPLE VER 2")
for name, age in dict.items():
    print(name, age)


for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate
