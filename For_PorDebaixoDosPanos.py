"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entragar um valor por vez
next -> me entrega o próximo valor
iter -> me entrega seu iterador
"""

text = "Python"
iterator = iter(text)

while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break

#It's the same as:
for letter in text:
    print(letter)