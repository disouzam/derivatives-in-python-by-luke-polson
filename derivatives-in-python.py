import marimo

__generated_with = "0.19.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Notice of authorship

    Most content in this notebook has been copied / typed based on corresponding code written / made available in YouTube video linked below by Luke Polson (Mr. P Solver)

    **Repository**: [lukepolson/youtube_channel](https://github.com/lukepolson/youtube_channel)

    **Notebook**: https://github.com/lukepolson/youtube_channel/blob/main/Python%20Tutorial%20Series/derivatives1.ipynb

    **Data**: https://github.com/lukepolson/youtube_channel/tree/main/Data

    **YouTube video**: [Derivatives In PYTHON (Symbolic AND Numeric)](https://www.youtube.com/watch?v=DeeoiE22bZ8)
    """)
    return


@app.cell
def _():
    import sympy as smp
    import numpy as np
    import matplotlib.pyplot as plt
    """
    import scipy as sp
    from scipy.misc import derivative
    """
    return np, plt, smp


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Symbolic Case

    You know the formula explicitly but don't really feel like using a pencil to take the derivative

    $$f(x) = ... $$

    **Example:**

    $$f(x) = e^{-a\sin(x^2)}\cdot \sin(b^x) \cdot \ln(c\sin^2(x)/x)$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First Define all your symbols in sympy
    """)
    return


@app.cell
def _(smp):
    x, a, b, c = smp.symbols('x a b c', real=True)
    return a, b, c, x


@app.cell
def _(a, smp, x):
    x**2+smp.exp(a)
    return


@app.cell
def _(a, smp, x):
    expression = x**2+smp.exp(a)
    type(expression)
    return


@app.cell
def _(a, b, c, smp, x):
    f = smp.exp(-a*smp.sin(x**2)) * smp.sin(b**x) * smp.log(c*smp.sin(x)**2 /x)
    f
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Compute derivatives using `smp.diff(f, x)` where $f$ is the function you want to take the derivative of and $x$ is the variable you are taking the derivative with respect to.
    """)
    return


@app.cell
def _(f, smp, x):
    dfdx = smp.diff(f, x)
    dfdx
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Can take the nth derivative $d^n f/dx^n$ by putting the optional argument at the end `smp.diff(f,x,n)`.
    """)
    return


@app.cell
def _(f, smp, x):
    d4fdx4 = smp.diff(f, x, 4)
    d4fdx4
    return (d4fdx4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Can then compute numerical values by plugging in numbers
    """)
    return


@app.cell
def _(a, b, c, d4fdx4, x):
    d4fdx4.subs([(x,4),(a,1),(b,2),(c,3)]).evalf()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Can also convert to a numerical function for plotting
    """)
    return


@app.cell
def _(a, b, c, d4fdx4, smp, x):
    d4fdx4_f = smp.lambdify((x,a,b,c), d4fdx4)
    return (d4fdx4_f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Define $x$ and $y$ arrays using the numerical function above
    """)
    return


@app.cell
def _(d4fdx4_f, np):
    x_values = np.linspace(1,2,100)
    y_values = d4fdx4_f(x_values, a=1, b=2, c=3)
    return x_values, y_values


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Plot
    """)
    return


@app.cell
def _(plt, x_values, y_values):
    plt.plot(x_values,y_values, "o--")
    plt.ylabel('$d^4 f / dx^4$', fontsize=24)
    plt.xlabel('$x$', fontsize=24)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Numerical Case

    Your given data like such
    """)
    return


@app.cell
def _(np):
    x_2, y_2 = np.loadtxt('sample_data1.txt')
    return x_2, y_2


@app.cell
def _(plt, x_2, y_2):
    plt.plot(x_2, y_2, 'o--')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are a few ways to go about this.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **1: The basic way**
    """)
    return


@app.cell
def _(np, x_2, y_2):
    dydx = np.gradient(y_2,x_2)
    return (dydx,)


@app.cell
def _(dydx, np, plt, x_2, y_2):
    plt.plot(x_2,y_2, '^--', label='$y(x)$')
    plt.plot(x_2,dydx, 'o--', label='$y\'(x)$ - 1st Derivative')

    number_of_points = len(dydx)
    dydx_zeros = []
    previous_y_value = dydx[0]
    current_y_value = previous_y_value

    for idx in range(1, number_of_points):
        previous_y_value = current_y_value
        current_y_value = dydx[idx]
        if np.sign(previous_y_value) != np.sign(current_y_value):

            if np.sign(previous_y_value) < 0:
            x_root_boundary = np.array([x_2[idx - 1], x_2[idx]])
            dydx_root_boundary = np.array([dydx[idx - 1], dydx[idx]])
            else:
                x_root_boundary = np.array([x_2[idx], x_2[idx - 1]])
                dydx_root_boundary = np.array([dydx[idx], dydx[idx - 1]])

            y_interpolate = 0
            x_interpolate = np.interp(y_interpolate, dydx_root_boundary, x_root_boundary)
            dydx_zeros.append(x_interpolate)

    for zero in dydx_zeros:
        plt.axvline(x=zero, color='red', linestyle='--', label=f"$y\'(x)=0$ at $x={zero:.2f}$")

    # Adding a horizontal line at y=0
    plt.axhline(y=0, color='black', linestyle='-', label='y=0')
    plt.legend()
    return


if __name__ == "__main__":
    app.run()
