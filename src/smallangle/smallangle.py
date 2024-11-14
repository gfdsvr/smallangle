import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 1,
)

def sin(number):
    """Divides 2 pi in the given number of steps and calculates the sin of
    each of these values.

    Args:
        number (int): how many steps there are
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 1,
)

def tan(number):
    """ Divides 2 pi in the given number of steps and calculates the tan of 
    each of these values.

    Args:
        number (int): how many steps there are
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    cmd_group()

