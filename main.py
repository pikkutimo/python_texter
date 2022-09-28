import curses
from time import perf_counter
# Show text
# Allow user to input text
# Check if input_char is equal to string[X] 
# Count mistakes
# Add possibility to amend your input
# Calculate the words per minute

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

def words_per_minute():
    # The value is calculated with the following formula:
    # Every character of the string divided by 5 per minutes minus uncorrected errors per minutes
    #  
    pass

def get_input(stdscr, middle_row: int, cursor_pos: int, message: str):

    user_input = ""
    index = -1
    count = 0
    user_editing = False
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.keypad(True)
    # start = None
    # Main loop
    
    while True:
        input_char = stdscr.get_wch()
        if len(user_input) == 0:
            # Start time
            time_start = perf_counter()
        if input_char == curses.KEY_LEFT:
            # If the user presses the left arrow key and there are char in the list:
            # Back the index down by one and make the cursor visible to the user.
            if user_editing:
                index -= 1
            curses.curs_set(1)
            user_input = user_input[:index]
            stdscr.addstr(middle_row, cursor_pos, user_input)
            continue
        if input_char == curses.KEY_RIGHT:
            pass
        # if the user has edited the content of the user_input
        if user_editing:
            user_editing = False
        user_input += input_char
        stdscr.addstr(middle_row, cursor_pos, user_input)

        if len(user_input) == len(message):
            break
    
    time_end = perf_counter()

    count = check_for_diffences(user_input, message)
    if count > 0:
        error_message = f"Out of {len(user_input)} characters, you have {count} errors."
        stdscr.addstr(middle_row + 3, cursor_pos, error_message)

    stdscr.addstr(middle_row + 6, cursor_pos, f"Done - It took you {time_end - time_start} seconds")
    stdscr.getkey()

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)
    
    num_rows, num_cols = stdscr.getmaxyx()
    middle_row = int(num_rows / 2)
    message = "Hello, Matti! This is a sample."
    cursor_pos = show_text(stdscr, middle_row, message, num_cols)
    
    get_input(stdscr, middle_row, cursor_pos, message)


# The wrapper takes callable object and does the initializations for you and after the callable returns, the wrapper restores the terminal's original state.
# The wrapper contains try...catch for this purpose.
print("Initializing texter...")
curses.wrapper(main)
