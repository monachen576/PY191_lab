import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # ==========================================================
    # INITIALIZE THE DISPLAY
    #
    # Display the document with the cursor at the current
    # cursor position.
    #
    # Example
    #
    # text    = "Hello"
    # cursor  = 0
    #
    # display = "|Hello"
    #
    # ---------------- TODO ----------------

    display = text[:cursor] + "|" + text[cursor:]

    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)
    
    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

    # left arrow
        elif key == curses.KEY_LEFT:
            if (cursor>0): 
                cursor -= 1
    # right arrow
        elif key == curses.KEY_RIGHT:
            if (cursor < len(text)): 
                cursor += 1
    # backspace
        elif key in (8, 127, curses.KEY_BACKSPACE):
            text = text[0:cursor] + text[cursor+1:]
            cursor -= 1

    # enter
        elif key == 10:
            text = text[0:cursor] + "\n" + text[cursor:]
            cursor += 1

    # insert
        elif 32 <= key <= 126:
            text = text[0:cursor] + chr(key) + text[cursor:]
            cursor += 1

        # ----------------------------------------

        #BONUS: Can you figure out how to select one line up/down by yourself?
"""
        elif key == curses.KEY_UP:

            ...

            display = ...

        elif key == curses.KEY_DOWN:

            ...

            display = ...
"""
curses.wrapper(main)
