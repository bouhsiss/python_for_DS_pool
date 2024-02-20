import time
from tqdm import tqdm
import os


def ft_tqdm(iterable, total=None):
    """
    A custom implementation of tqdm, a progress bar library for Python.

    Parameters:
    iterable (iterable): The iterable object to iterate over.
    total (int, optional): The total number of iterations. If not provided, it will be set to the length of the iterable.

    Yields:
    item: The next item from the iterable.

    """
    total = total or len(iterable)
    for i, item in enumerate(iterable, 1):
        progress = i / total * 100
        terminal_width = os.get_terminal_size().columns
        bar_width = terminal_width - 30
        bar = f"[{'█' * int(progress / 100 * bar_width):{bar_width}}]"
        formatted_progress = f"{progress:.1f}%"
        print(f"\r{formatted_progress} {bar} | {i}/{total}", end='')
        yield item
    print()