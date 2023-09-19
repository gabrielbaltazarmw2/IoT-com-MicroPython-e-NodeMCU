from machine import Pin
import time

# Define os pinos para os segmentos do display de 7 segmentos
a = Pin(0, Pin.OUT)  # a
b = Pin(1, Pin.OUT)  # b
c = Pin(2, Pin.OUT)  # c
d = Pin(3, Pin.OUT)  # d
e = Pin(4, Pin.OUT)  # e
f = Pin(5, Pin.OUT)  # f
g = Pin(14, Pin.OUT)  # g

# Mapeamento para exibir os dígitos de 0 a 9
digit_map = {
    0: [1, 1, 1, 1, 1, 1, 0],  # 0
    1: [0, 1, 1, 0, 0, 0, 0],  # 1
    2: [1, 1, 0, 1, 1, 0, 1],  # 2
    3: [1, 1, 1, 1, 0, 0, 1],  # 3
    4: [0, 1, 1, 0, 0, 1, 1],  # 4
    5: [1, 0, 1, 1, 0, 1, 1],  # 5
    6: [1, 0, 1, 1, 1, 1, 1],  # 6
    7: [1, 1, 1, 0, 0, 0, 0],  # 7
    8: [1, 1, 1, 1, 1, 1, 1],  # 8
    9: [1, 1, 1, 1, 0, 1, 1],  # 9
}

# Função para exibir um dígito no display
def display_digit(digit):
    for i, pin in enumerate([a, b, c, d, e, f, g]):
        pin.value(digit_map[digit][i])

# Loop principal
counter = 0

while True:
    # Exibe o dígito atual no display
    display_digit(counter % 10)

    # Incrementa o contador
    counter += 1

    # Aguarda 1 segundo antes de continuar
    time.sleep(1)
