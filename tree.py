import random
import time
import os
import argparse
import signal
import sys

# ANSI escape-коды для цветов
GREEN = '\033[32m'
BLUE = '\033[34m'
WHITE = '\033[37m'
RESET = '\033[0m'

# Список цветов для игрушек (исключая зеленый и синий)
DECORATION_COLORS = ['\033[31m', '\033[33m', '\033[35m', '\033[36m']  # Красный, желтый, пурпурный, бирюзовый

def draw_tree(rows, freq, snow_animation=False, use_colors=True):
    if rows < 3:
        print("Высота елки должна быть не менее трех строк.")
        return

    branches = '*'
    decorations = ['o', 'O', '@', '0']
    snow = '.'

    width = 3
    steps = (rows - 3) // 2 + 1

    # Создаем массив для елки и снега
    tree_height = 3 * steps + 3  # Высота елки плюс ствол
    tree_width = rows * 2
    tree = [[' ' for _ in range(tree_width)] for _ in range(tree_height)]

    for step in range(steps):
        for i in range(3 + step):
            line_index = step * 3 + i
            if line_index >= tree_height:
                break
            start = (tree_width // 2) - (width // 2)
            end = start + width
            if start < 0 or end > tree_width:
                continue
            tree[line_index][start] = '/'
            tree[line_index][end - 1] = '\\'
            for j in range(start + 1, end - 1):
                if random.randint(1, freq) == 1:
                    tree[line_index][j] = random.choice(decorations)
                else:
                    tree[line_index][j] = branches
        width += 2

    # Добавляем ствол елки
    trunk_width = 3
    trunk_start = (tree_width // 2) - (trunk_width // 2)
    for i in range(3):
        for j in range(trunk_start, trunk_start + trunk_width):
            tree[tree_height - 3 + i][j] = '|'

    floor = '_' * tree_width
    tree.append(list(floor))

    def print_tree():
        for line in tree:
            colored_line = ''.join(
                (random.choice(DECORATION_COLORS) + char + RESET if char in decorations and use_colors else
                 GREEN + char + RESET if char == branches and use_colors else
                 WHITE + char + RESET if char == snow and use_colors else
                 BLUE + char + RESET if use_colors else char)
                for char in line
            )
            print(colored_line)

    if snow_animation:
        snowflakes = []

        while True:
            # Очищаем предыдущие позиции снежинок
            for row, col, _ in snowflakes:
                if tree[row][col] == snow:
                    tree[row][col] = ' '

            # Добавляем новые снежинки
            if random.random() < 0.3:  # Вероятность появления новой снежинки
                col = random.randint(0, tree_width - 1)
                snowflakes.append((0, col, random.randint(0, 2)))  # (row, col, кадры зависания)

            # Обновляем позиции снежинок
            new_snowflakes = []
            for row, col, freeze_frames in snowflakes:
                if freeze_frames > 0:
                    new_snowflakes.append((row, col, freeze_frames - 1))
                else:
                    # Случайное смещение для имитации ветра
                    wind = random.choice([-1, 0, 1])
                    new_col = col + wind
                    if 0 <= new_col < tree_width and row < tree_height - 1 and tree[row + 1][new_col] == ' ':
                        new_snowflakes.append((row + 1, new_col, random.randint(0, 2)))
                    else:
                        tree[row][col] = snow

            snowflakes = new_snowflakes

            # Рисуем снежинки
            for row, col, _ in snowflakes:
                tree[row][col] = snow

            print_tree()
            time.sleep(1 / 20)  # Частота кадров
            os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана

    else:
        print_tree()

def signal_handler(sig, frame):
    print("\nС новым Годом, хабровчане!")
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Рисуем новогоднюю елочку с анимацией.")
    parser.add_argument('-r', '--rows', type=int, default=15, help='Высота елочки (стандартно 15)')
    parser.add_argument('-f', '--frequency', type=int, default=3, help='Заполение украшениями Мин 100 Макс 1 (стандартно 3)')
    parser.add_argument('-c', '--colors', action='store_true', help='Включить цвета')
    parser.add_argument('-s', '--snow', action='store_true', help='Включить анимацию снега')

    args = parser.parse_args()

    signal.signal(signal.SIGINT, signal_handler)

    draw_tree(args.rows, args.frequency, snow_animation=args.snow, use_colors=args.colors)

if __name__ == "__main__":
    main()