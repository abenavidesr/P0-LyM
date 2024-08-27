import main

# PRUEBAS

code = "R;M;R;B"
pasos = main.lexer(code)
for elem in pasos:
    print(elem)