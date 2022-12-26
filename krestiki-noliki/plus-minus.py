# Крестики - нолики

# создаем матрицу - игровое поле (без номеров строк и столбцов)
game_zone = [["-" for j in range(3)] for i in range(3)]

# вывод игровой таблицы на экран
def out_game_tab(game_zone):
    n = 0
    print(" ", "1", "2", "3")
    for i in game_zone:
        n += 1
        print(n, i[0], i[1], i[2])

# ставим значок (крестик или нолик) на игровое поле
def in_game_zone(x, y, game_zone, player):
    if game_zone[y-1][x-1] == "-":
        game_zone[y-1][x-1] = player
        return True
    return False

def check_step(x, y, game_zone, player):
    # если выигрышный вариант - Игрок выиграл!!! - переписываем выигрышную комбинацию в верхнем регистре и возвращаем True
    x = x-1
    y = y-1
    if game_zone[y][0] == game_zone[y][1] == game_zone[y][2] == player:
        # по вертикали
        game_zone[y][0] = player.upper()
        game_zone[y][1] = player.upper()
        game_zone[y][2] = player.upper()
        return True
    if game_zone[0][x] == game_zone[1][x] == game_zone[2][x] == player:
        # по горизонтали
        game_zone[0][x] = player.upper()
        game_zone[1][x] = player.upper()
        game_zone[2][x] = player.upper()
        return True
    if x == y and game_zone[0][0] == game_zone[1][1] == game_zone[2][2] == player:
        # диагональ сверху(слева)-вниз(вправо)
        game_zone[0][0] = player.upper()
        game_zone[1][1] = player.upper()
        game_zone[2][2] = player.upper()
        return True
    if (y == 0 and x == 2 or y == 1 and x == 1 or y == 2 and x == 0) and game_zone[0][2] == game_zone[1][1] == game_zone[2][0] == player:
        # диагональ снизу(слева)-вверх(вправо)
        game_zone[0][2] = player.upper()
        game_zone[1][1] = player.upper()
        game_zone[2][0] = player.upper()
        return True
   # иначе - не выиграл
    return False

# проверяем, свободна ли хотя-бы одна клетка
def check_free_exist(game_zone):
    for i in game_zone:
        for j in i:
            if j == "-":
                return True
    return False

### Игра

# триггер - конец игры
game_end = False

# знак текущего игрока ("o" или "x" (en))
player = "x"

# Выводим начальную раскладку (пустое игровое поле)
out_game_tab(game_zone)

while not game_end:
    step_is_done = False
    while not step_is_done:
        input_ok = False
        if player == "x":
            print("Ходит игрок, ставящий крестики. Укажите куда поставить крестик.")
        else:
            print("Ходит игрок, ставящий нолики. Укажите куда поставить нолик.")
        while not input_ok:
            x = input("Номер столбца (цифра: 1, 2 или 3): ")
            if len(x) > 1:
                print("Ошибка ввода. Вы ввели много знаков.")
            elif not x[0].isdigit():
                print("Ошибка ввода. Вы ввели не цифру.")
            else:
                x = int(x)
                if 0 < x < 4:
                    input_ok = True
                else:
                    print("Вы ввели неверное значение.")

        input_ok = False
        while not input_ok:
            y = input("Номер строки (цифра: 1, 2 или 3): ")
            if len(y) > 1:
                print("Ошибка ввода. Вы ввели много знаков.")
            elif not y[0].isdigit():
                print("Ошибка ввода. Вы ввели не цифру.")
            else:
                y = int(y)
                if 0 < y < 4:
                    input_ok = True
                else:
                    print("Вы ввели неверное значение.")

        step_is_done = in_game_zone(x, y, game_zone, player)
        if not step_is_done:
            print("Игровое поле занято. Выберите другие координаты.")

    # выводим игровое поле после хода
    out_game_tab(game_zone)
    # Проверка хода (можно совместить с ходом, или вызывать из него, но так независимо и не нагромождено)
    if check_step(x, y, game_zone, player):
        print("Игрок ", player.upper(), " выиграл. Поздравляем!")
        game_end = True
    if not check_free_exist(game_zone):
        print("Все игровые поля заполнены. Победитель не выявлен. Ничья!")
        game_end = True

    # Меняем игрока (первый ход - меням на крестики)
    if player == "o":
        player = "x"
    else:
        player = "o"
        
# Вывод на экран финальной раскладки
out_game_tab(game_zone)
print("Спасибо!")





