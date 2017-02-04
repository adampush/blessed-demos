"""Some functions I wrote while exploring the blessed Python module
by J Quast (fork of blessings module)."""

import random

import blessed


def hello_bold_world():
    """Print some bold text to stdout."""
    term = blessed.Terminal()
    print(term.bold("Hello, Bold World!"))

def hello_boldest_world():
    """Print some colorful text to stdout."""
    term = blessed.Terminal()
    print(term.bold_red_on_bright_green("Hello, Bold Red On Bright Green World!"))

def get_inkey_type():
    """Wait until user types a keystroke, then capture and print
    keystroke information to stdout."""
    term = blessed.Terminal()
    with term.cbreak():
        inp = term.inkey()
        print('term.inkey() datatype is {}'.format(type(inp)))
        print('')
        print('Using repr() to get string representation of inkey:')
        print('You pressed ' + repr(inp))
        print('repr(term.inkey()) datatype is {}'.format(type(repr(inp))))
        print('')
        print('Using str() to get string rep. of inkey:')
        print('You pressed ' + str(inp))
        print('str(term.inkey()) datatype is {}'.format(type(str(inp))))

def get_inkey_q():
    """Wait until user presses 'q' (case-sensitive) then exit."""
    term = blessed.Terminal()
    with term.cbreak():
        inp = term.inkey()
        while repr(inp) != "'q'":
            inp = term.inkey()
        print("You pressed 'q'!")

def get_cursor_location():
    """Get the cursor's location and print it to stdout."""
    term = blessed.Terminal()
    row, col = term.get_location(timeout=5)
    print('Row, Col is {:d}, {:d}.'.format(row, col))

def print_to_fixed_location(col=20, row=0, text='Hello, (20, 5)!'):
    """Print some text to a specific location on terminal."""
    term = blessed.Terminal()
    with term.location(x=col, y=row):
        print(text)
    print('Goodbye, ({},{})!'.format(col, row))

def print_simulated_typing_text(rainbow=False):
    """Keep printing some dummy text to the screen until the user
    presses 'q'."""
    term = blessed.Terminal()
    print(term.clear)
    print(term.move(0, 0))

    # Create a gibberish sentence.
    # Set of letters from which to build words.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # Pick a random number of words to create.
    num_words = random.randint(20, 30)
    # Pick a random length for each of the words.
    word_lengths = [random.randint(3, 7) for x in range(num_words)]
    # Build the words and then join them into a sentence.
    words = []
    for word_len in word_lengths:
        word = ''
        for i in range(word_len):
            word = ''.join([word, letters[random.randint(0, len(letters) - 1)]])
        words.append(word)
    sentence = ' '.join(words)

    # Set of text colors to use if argument rainbow == True
    colors = [term.red, term.green, term.blue, term.yellow, term.cyan, term.magenta]

    # Main loop where look for 'q' or 'Q' keypress -- if no keypress, then
    # print out a character from the sentence. We keep printing the sentence
    # over and over until we get a 'q' or 'Q'
    with term.cbreak():
        inp = term.inkey(timeout=0.001)
        char_count = 0
        while inp not in (u'q', 'Q'):
            timeout = random.randint(0, 150) / 1000
            if char_count < len(sentence):
                # Print each character using a random color if rainbow == True
                if rainbow:
                    color = colors[random.randint(0, len(colors) - 1)]
                # Otherwise just use black
                else:
                    color = term.black
                char = sentence[char_count]
                print(color(char), end='', flush=True)
                char_count += 1
                if char_count == len(sentence):
                    print(term.bold_red('. '), end='', flush=True)
                    char_count = 0
            # Kind of hacky I guess but we use the timeout arg to do the
            # random delay that simulates a human typing out the sentence.
            inp = term.inkey(timeout=timeout)

def clear_blue_bg_end_flush():
    """Clear the screen and leave a blue background."""
    term = blessed.Terminal()
    print(term.move(1, 1))
    print(term.on_blue(term.clear), end='', flush=True)
    print(term.move(term.height - 1, 0))

def clear_blue_bg():
    """Clear the screen and leave a blue background."""
    term = blessed.Terminal()
    print(term.move(1, 1))
    print(term.on_blue(term.clear))
    print(term.move(term.height - 1, 0))

def clear():
    """Clear the screen (not like a bash clear command)."""
    term = blessed.Terminal()
    print(term.clear)

def print_line_numbers():
    """Prints a number on each line of the terminal."""
    term = blessed.Terminal()
    print(term.move(0, 0))
    with term.cbreak():
        lst = [str(x) for x in range(term.height)]
        print('   \n'.join(lst) + '. Press q to quit.')
        inp = term.inkey()
        while repr(inp) not in ("'q'", "'Q'"):
            inp = term.inkey()
        print('Done!')

