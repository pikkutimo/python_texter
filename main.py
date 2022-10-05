import curses
from texter import print_logo_and_menu, calculate_x_position, get_input

def main(stdscr):
    """The main function of the program"""
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    num_rows, num_cols = stdscr.getmaxyx()
    middle_row = int(num_rows / 2)

    while True:
        # Name and menu
        print_logo_and_menu(stdscr, num_cols)
        # The choose option from menu
        menu_selection = stdscr.getkey()

        if menu_selection == "1":
            window = curses.newwin((num_rows - middle_row), num_cols, middle_row, 0)
            # Main loop
            message = "Hello, Matti! This is a sample."
            x_position = calculate_x_position(num_cols, message)
            window.addstr(1, x_position, message, curses.color_pair(1))
            get_input(window, x_position, message)
            stdscr.clear()
        if menu_selection == "2":
            break



# The wrapper takes callable object and does the initializations for you and after the callable
# returns, the wrapper restores the terminal's original state.
# The wrapper contains try...catch for this purpose.
print("Initializing texter...")
curses.wrapper(main)