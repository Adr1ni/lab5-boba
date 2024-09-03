import re

pattern = r"Hola"
text = "Hola Mundo desde regex!"
match = re.search(pattern, text)

if match:
    print("Coincidencia encontrada:", match.group())
