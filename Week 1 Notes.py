import marimo

__generated_with = "0.19.0"
app = marimo.App(width="medium", app_title="Week 1 Notes")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 1.1
    > **Python** is the most popular and widely supported programming languages in modern day. It is an interpreted language with uses ranging from small, single-purpose applications to machine learning and data science.

    ## I/O Operations
    Inputting and outputting character data in Python uses the two built-in functions, `input()` and `print()`, respectively.
    """)
    return


@app.cell
def _():
    # Write code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 1.2
    > Computers can represent data in the form of numbers, characters, true/false, and even in user-defined ways.

    ## Variables
    Variables represent data stored in memory with an alias. They point to binary expressions, which can be in the form of different data types.
    """)
    return


@app.cell
def _():
    # Write code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=r"public\image.png",
        alt="Marimo logo",
        width=800,
        rounded=True,
        style={"margin": "0 auto"}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Practice 1
    Complete the code based on the image above.
    """)
    return


@app.cell
def _():
    # x = 23
    # food =
    # = False
    #
    return


if __name__ == "__main__":
    app.run()
