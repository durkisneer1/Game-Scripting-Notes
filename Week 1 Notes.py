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
        src="public/image.png",
        width=600,
        caption="Fig 1.2: Variable representation in memory",
        style={"margin": "0 auto"}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Practice 1
    1. Complete the code based on the image above.
    """)
    return


@app.cell
def _():
    # x = 23
    # food =
    # = False
    #
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2. What is the data type of the variable `is_hit`?

    3. What is the difference between the data presented by the variable `x` and by the varible `y`?

    4. What might be a potential memory problem with strings if you're not careful, now seeing how they're represented in memory?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 1.3
    > If you can tank of a mathematical formula, you can write it in code. Python natively supports basic arithmetic, but more advanced mathematical operations require external modules.

    ## Mathematical Operations
    Addition, subtraction, multiplication, and division operators are what you'd expect them to be, but there are a few others that can be very useful. All programming languages follow the order of operations (e.g., PEMDAS).
    """)
    return


@app.cell
def _():
    # Write code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 1.4
    > Computers user comparative operators to evaluate relationships between data -- an essential feature for decision-making in video games.

    ## Comparative Operations
    Every program you've ever used boils down to a compilation of decisions, and with every decision comes a comparison between two or more values.
    """)
    return


@app.cell
def _():
    # Write code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Practice 2

    ```py
    PI = 3.14

    radius = float(input("Enter sphere radius: "))
    volume = (4 / 3) * PI * radius**3

    print(volume)
    ```
    1. What is the output of the program above if the user input was 6? (Round to the nearest tenth)

    ```py
    water_amount = 2000

    print(water_amount <= volume)
    ```

    2. If the program has an output of `True`, what does this mean in the context of the program?

    3. Give an example where a user input value _greater than_ `0` would result in the output being `False`.
    """)
    return


@app.cell
def _():
    # Write code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Homework
    Building upon sphere code above, print the percentage of the sphere's volume that the water amount takes up for any user input.

    Then, reverse engineer the program to find and print the exact radius a sphere has to be to **perfectly contain** 2000 units of water.

    > Hint: You know the target volume. Use algebra to flip the volume formula to find the unknown radius instead.

    I will be grading on correctness, syntax, and typing standards.
    """)
    return


@app.cell
def _():
    # Write code here
    return


if __name__ == "__main__":
    app.run()
