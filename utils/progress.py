"""This module provides a simple progress bar for Jupyter
"""

from IPython.display import clear_output

def update_progress(progress: float) -> None:
    """This function prints a simple command line progress bar for your Jupyter
    Notebook.

    Args:
        progress (float): The current progress

    Example:
        number_of_elements = 1000

        for i in range(number_of_elements):
            time.sleep(0.1) # Replace this with a real computation
            update_progress(i / number_of_elements)
        update_progress(1)

    """
    bar_length = 20
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1

    block = int(round(bar_length * progress))
    clear_output(wait=True)
    text = "Progress: [{0}] {1:.1f}%".format(
        "#" * block + "-" * (bar_length - block), progress * 100
    )
    print(text)
