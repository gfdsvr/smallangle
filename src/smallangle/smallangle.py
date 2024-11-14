import click
import numpy as np
from numpy import pi
import pandas as pd

@click.command()
@click.argument("number")
@click.option(
    "-n",
    "--number",
    default = 1,
)

def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    sin()