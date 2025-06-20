import curses
from random import randint

last_score = 0  # Variable global para guardar el último puntaje

def draw_menu(stdscr):
    stdscr.clear()
    sh, sw = stdscr.getmaxyx()

    if sh < 12 or sw < 30:
        stdscr.addstr(0, 0, "La ventana es demasiado pequeña.")
        stdscr.addstr(1, 0, "Aumenta el tamaño y vuelve a intentarlo.")
        stdscr.refresh()
        stdscr.getch()
        return False

    stdscr.addstr(5, 10, "=== SNAKE GAME ===")
    stdscr.addstr(7, 10, "1. Jugar")
    stdscr.addstr(8, 10, "2. Salir")
    stdscr.addstr(10, 10, f"Último puntaje: {last_score}")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            return True
        elif key == ord('2'):
            return False


def main(stdscr):
    global last_score

    while True:
        play = draw_menu(stdscr)
        if not play:
            break

        # Juego
        curses.curs_set(0)
        sh, sw = stdscr.getmaxyx()
        w = curses.newwin(sh, sw, 0, 0)
        w.keypad(True)
        w.timeout(100)




        # Dibujar bordes del tablero
        for x in range(sw):
            w.addch(0, x, '#')
            w.addch(sh - 2, x, '#')
        for y in range(sh):
            w.addch(y, 0, '#')
            w.addch(y, sw - 2, '#')

        snk_x = sw // 4
        snk_y = sh // 2
        snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
        food = [randint(1, sh - 2 - 1), randint(1, sw - 2 - 1)]

        w.addch(food[0], food[1], curses.ACS_PI)

        key = curses.KEY_RIGHT
        score = 0

        while True:
            next_key = w.getch()
            key = key if next_key == -1 else next_key

            head = snake[0]
            if key == curses.KEY_DOWN:
                new_head = [head[0] + 1, head[1]]
            elif key == curses.KEY_UP:
                new_head = [head[0] - 1, head[1]]
            elif key == curses.KEY_LEFT:
                new_head = [head[0], head[1] - 1]
            elif key == curses.KEY_RIGHT:
                new_head = [head[0], head[1] + 1]
            else:
                continue

            if new_head in snake or new_head[0] in [0, sh] or new_head[1] in [0, sw]:
                msg = "GAME OVER"
                w.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
                w.refresh()
                curses.napms(2000)
                last_score = score
                break

            snake.insert(0, new_head)

            if new_head == food:
                score += 1
                while True:
                    food = [randint(1, sh - 2), randint(1, sw - 2)]
                    if food not in snake:
                        break
                w.addch(food[0], food[1], curses.ACS_PI)
            else:
                tail = snake.pop()
                w.addch(tail[0], tail[1], ' ')

            w.addch(new_head[0], new_head[1], '#')

if __name__ == "__main__":
    curses.wrapper(main)
