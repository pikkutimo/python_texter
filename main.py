import curses
# Show text
# Allow user to input text
# Check if input_char is equal to string[X] 
# Count mistakes
# Add possibility to amend your input?
# name = ""

def check_for_diffences(input_string: str, message: str) -> int:
    errors = 0
    
    for index in range(len(input_string)):
        if input_string[index] != message[index]:
            errors += 1

    return errors

def show_text(stdscr, middle_row: int, message: str, num_cols: int) -> int:
# show text and return the starting position for the text
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    stdscr.addstr(middle_row, x_position, message, curses.color_pair(1))

    return x_position

def get_input(stdscr, middle_row: int, cursor_pos: int, message: str):

    input_string = ""
    count = 0
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.keypad(True)

    while True:
        input_char = stdscr.get_wch()
        if input_char == curses.KEY_LEFT:
            # HOWTO - allow user to edit his input
            stdscr.addstr(middle_row - 5, cursor_pos, "Cursor key")
            continue
        input_string += input_char
        stdscr.addstr(middle_row, cursor_pos, input_string)

        count = check_for_diffences(input_string, message)
        if count > 0:
            error_message = f"Out of {len(input_string)} characters, you have {count} errors"
            stdscr.addstr(middle_row + 5, cursor_pos, error_message)

        if len(input_string) == len(message):
            break

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)
    
    num_rows, num_cols = stdscr.getmaxyx()
    middle_row = int(num_rows / 2)
    message = "Hello, Matti! This is a sample."
    cursor_pos = show_text(stdscr, middle_row, message, num_cols)
    
    get_input(stdscr, middle_row, cursor_pos, message)

    stdscr.refresh()
    stdscr.getkey()

# The wrapper takes callable object and does the initializations for you and after the callable returns, the wrapper restores the terminal's original state.
# The wrapper contains try...catch for this purpose.
print("Initializing texter...")
curses.wrapper(main)
