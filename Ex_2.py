# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = True
y = True
z = True
result = not(x or y or z) == (not x) and (not y) and (not z)
print(result)