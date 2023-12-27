import random
import os
import time

# A small script that makes your terminal 'snow'
# Merry Christmas
# author: lightblue
# date: 2023-12-25
# inspired by Engineer Man from https://www.youtube.com/watch?v=_chP0a4PMTM

INTERVAL = 0.4
CHANCE_TO_ADD_SNOWFLAKE = 0.04

column_count, line_count = os.get_terminal_size()
snowflakes = ['❆', '❅', '❄', '.', '•']
rid_prompt = '\033[?25l'
running = True

def make_line(column_count, blank=False):
    if blank:
        return [' '] * column_count
    line = []
    for _ in range(column_count):
        if random.random() < CHANCE_TO_ADD_SNOWFLAKE:
            line.append(random.choice(snowflakes))
        else:
            line.append(' ')
    return line

def init_grid(column_count, line_count):
    grid = []
    grid.append([ n for n in 'Merry Christmas!'.center(column_count) ])
    for _ in range(line_count-1):
        grid.append(make_line(column_count, blank=True))
    return grid

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def draw_grid(grid):
    output = ''
    for line in grid:
        output += ''.join(line) + '\n'
    output.rstrip('\n')
    clear_screen()
    print(rid_prompt)
    print(output, end='')

def snow():
    grid = init_grid(column_count, line_count)
    while running:
        grid.pop()
        grid.insert(1, make_line(column_count))
        draw_grid(grid)
        time.sleep(INTERVAL)
    clear_screen()    

if __name__ == "__main__":
    snow()