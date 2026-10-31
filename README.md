# cowspam
A small, silly, screen-cluttering Python library derived from [Cowsay](https://pypi.org/project/cowsay/). By Ian Rodriguez.

Cowsay was originally created by Tony Monroe, and its Python port by multiple contributors is available as a [GitHub repo](https://github.com/VaasuDevanS/cowsay-python). The purpose of **cowspam** is a personal challenge to see how far I can go with making a derivative of such a small, niche library.

Requires pip and Python 3.12 or later. From the project directory, build with these commands:

    python -m pip install .
    cowspam --help

Or build a distributable package:

    python -m pip install build
    python -m build

## Library

```python
from cowspam import Cow, make_cow_text, run_kilobytes

cow = Cow("Bessie")
cow.moo()

text, is_normal = make_cow_text()
counts, bytes_generated = run_kilobytes(1, write_output=False) # Generates 1 KB of cowsay spam
```

- `COWSAY_CHARS` - List of alternate characters for anomalous cows (the regular cow isn't in this list).
- `Cow` - Fundamental dataclass of this silly little library. Set its `name` and optionally its `age`; `.moo()` prints a moo (and the age for normal cows), while `.speak(str)` prints your message.
- `clear_screen()` - Clear the screen to make room for another Cow.
- `main()` - Carries the CLI; by default, prints out 100 Cows to terminal.
- `make_cow_text()` - Build a Cow with a random name, then return its moo text and whether it's normal. By default, normality is random; set `normal_only=True` to guarantee a normal cow.
- `print_tally()` - Print a tally from a `Counter` object.
- `rand_cow_name()` - Pick a random cow name from the bundled name list.
- `run_kilobytes()` - Generate cows until at least the requested number of kilobytes is produced; optionally, write them to standard output.

## CLI Commands
- `-h / --help` - View commands
- `(loops)` - Positional argument; enter a number of cows to generate, either to terminal or piped to a file. Default: 100.
- `-a / --auto` - Run without a 1-second delay between cowsay prints; automatic for piped
- `-f / --flash` - (Epilepsy warning) Clear the screen for each cow print, creating a flashing effect
- `-k / --kb / --kilobytes X` - Alternative to loops: generate cowsay prints until X amount is generated in kilobytes.
- `-n / --normal` - Only generate normal cows
