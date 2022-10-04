import curses
from time import perf_counter
# Show text
# Allow user to input text
# Check if input_char is equal to string[X]
# Count mistakes
# Add possibility to amend your input
# Calculate the words per minute

def check_for_diffences(input_string: str, message: str) -> int:
    """Compares the input_string against the message"""
    errors = 0
    for index, char in enumerate(input_string):
        if char != message[index]:
            errors += 1

    return errors

def calculate_x_position(num_cols: int, message: str) -> int:
    """Calculate the column where message"""
    middle_column = int(num_cols / 2)
    half_length_of_message = int(len(message) / 2)
    x_position = middle_column - half_length_of_message

    return x_position


def calculate_wpm(time_start: float, time_end: float, user_input: str, error_count: int) -> int:
    """Calculate words per minute"""
    # The value is calculated with the following formula:
    # Every character of the string divided by 5 per minutes minus uncorrected errors per minutes

    minutes = (time_end - time_start) / 60
    words = len(user_input) / 5

    return int((words - error_count) / minutes)

def print_logo_and_menu(stdscr, num_cols: int):
    """Print the logo and menu"""

    logo = ["::::::::::::::::::::::::    :::::::::::::::::::::::::::::::::",  
        "       :+:    :+:       :+:    :+:    :+:    :+:       :+:    :+:", 
        "       +:+    +:+        +:+  +:+     +:+    +:+       +:+    +:+", 
        "       +#+    +#++:++#    +#++:+      +#+    +#++:++#  +#++:++#:  ",
        "       +#+    +#+        +#+  +#+     +#+    +#+       +#+    +#+ ",
        "       #+#    #+#       #+#    #+#    #+#    #+#       #+#    #+# ",
        "       ###    #############    ###    ###    #############    ### ",
        "",
        "__________________________________________________________________",
        "",
        "1. Test your speed",
        "2. To quit the program",
        "__________________________________________________________________"]     

    logo_position = int(num_cols / 2 - len(logo[0]) / 2)
    for index in enumerate(logo):
        stdscr.addstr(5 + index, logo_position, logo[index], curses.color_pair(1))

def get_input(window, cursor_pos: int, message: str):

    user_input = ""
    index = -1
    count = 0
    user_editing = False
    window.keypad(True)
    
    while True:
        input_char = window.get_wch()
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
            window.addstr(1, cursor_pos, user_input)
            continue
        # if the user has edited the content of the user_input
        if user_editing:
            user_editing = False
        user_input += input_char
        window.addstr(1, cursor_pos, user_input)

        if len(user_input) == len(message):
            break
    
    time_end = perf_counter()
    error_count = check_for_diffences(user_input, message)
    if count > 0:
        error_message = f"Out of {len(user_input)} characters, you have {error_count} errors."
        window.addstr(3, cursor_pos, error_message)

    wpm = calculate_wpm(time_start, time_end, user_input, error_count)

    window.addstr(5, cursor_pos, f"Done - Your WPM score is {wpm} words per minute.")
    
    input_key = window.getch()

def test():
    pass

def main(stdscr):
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
        


# The wrapper takes callable object and does the initializations for you and after the callable returns, the wrapper restores the terminal's original state.
# The wrapper contains try...catch for this purpose.
print("Initializing texter...")
curses.wrapper(main)
