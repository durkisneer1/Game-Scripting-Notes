import marimo

__generated_with = "0.19.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 2.1
    > Strings exist in every programming language, as it's **the** way to represent text in computers. The term "string" comes from it being a "string of characters". They're essentially chained characters in memory.

    ## Formatted Strings
    The most common approach when placing extra information next to variable values is with a formatted string. You can use concatenation, percent formatting, the format method, or f-strings for this purpose.

    _Concatenation:_<br>
    `"Hello, " + str(name) + ", how are you?"`

    _Percent formatting:_<br>
    `"Hello, %s, how are you?" % name`

    _Format method:_<br>
    `"Hello, {}, how are you?".format(name)`

    _F-String:_<br>
    `f"Hello, {name}, how are you?"`
    """)
    return


@app.cell
def _():
    # code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Substring Replacement
    Sometimes in a live chat room, you need to censor certain words. You can use the `replace` method to swap out substrings with another. This is a case-sensitive operation.

    _Syntax:_<br>
    `str.replace(old, new, count)`
    * `old`: The substring you want to replace
    * `new`: The new substring to insert in its place
    * `count` (optional): The max number of occurances to replace. If omitted, all occurrances are replaced.
    """)
    return


@app.cell
def _():
    # code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Splitting and Joining Strings
    One of the most used string methods for game dev. The split method allows for parsing words in a user input, and the join method does the opposite. Think of these as a string-to-list bridge.

    *Syntax*:<br>
    `str.split(separator, maxsplit)`
    * `separator` (optional): The delimiter to use for splitting the string. If not specified, whitespace is used.
    * `maxsplit` (optional): The max number of splits to perform.

    `separator.join(iterable)`
    * `separator`: The string that will be inserted between each element of the iterable.
    * `iterable`: An array-like data structure containing only string elements to be joined.
    """)
    return


@app.cell
def _():
    # code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Searching for Substrings in Strings
    You can use the `in` keyword to check if a substring exists in another string. It could be used for detecting keyword usage in a user input.
    """)
    return


@app.cell
def _():
    # code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practice 1
    ```py
    player_name = input("Enter a username: ")
    print("Welcome to Townsville, {player_name}!")

    new_message = input()
    filtered_message = new_message.replace("nerd", "****")
    print(f"{} says {}")
    ```

    1. Will line 2 output the string we intend to? If not, how can you fix it?

    2. What goes in both formatted sections of the f-string in line 6?

    3. What is the output of line 6 if the input of "You're a nerd!" was assigned to `new_message`?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 2.2
    > Like comparative operators, you can use logical operators to get a boolean output from a boolean expression. You can check if two values are true, at least one is, or even invert a value.

    ## Logical Operations
    To perform boolean arithmetic, you'll need these keywords (ordered by priority):
    1. `not` - Invert a boolean
    2. `and` - Check if booleans on both sides are `True`
    3. `or` - Check if at least one boolean on either side is `True`

    With `and`, if the left-hand side boolean is `False`, it will _short-circuit_, which can be used to your advantage to _reduce nesting_. Similary, `or` will short-curcuit if the left-hand side boolean is `True`.
    """)
    return


@app.cell
def _():
    # code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practice 2
    ```py
    a = "hello"
    b = "hi"
    x = False

    print(len(a) > len(b) and b == "hi")
    print(not x or a != "hello")
    ```

    1. What is the output of line 5?

    2. What is the output of line 6?

    3. Which boolean would I get if I compared the variables `a` and `b` with the `==` operator?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 2.3
    > Everything that has to do with computers is based on boolean algebra, from adding two numbers to calculating billions of matrices within a second. To achieve these feats, hundreds of thousands of scientists and engineers over decades needed to optimize how boolean expressions are processed in a computer.

    ## Boolean Algebra Laws

    | Law | Math | Code |
    | - | - | - |
    | De Morgan's | $\neg a \wedge \neg b \equiv \neg(a \vee b)$ | `not a and not b == not (a or b)` |
    | Double Negation | $\neg(\neg a) \equiv a$ | `not (not a) == a` |
    | Identity | $a \wedge 1 \equiv a$ <br> $a \vee 0 \equiv a$ | `a and True == a` <br> `a or False == a` |
    | Domination | $a \vee 1 \equiv 1$ <br> $a \wedge 0 \equiv 0$ | `a or True == True` <br> `a and False == False` |
    | Idempotent | $a \vee a \equiv a$ <br> $a \wedge a \equiv a$ | `a or a == a` <br> `a and a == a` |
    | Complement | $a \vee \neg a \equiv 1$ <br> $a \wedge \neg a \equiv 0$ | `a or not a == True` <br> `a and not a == False` |
    | Absorption | $a \vee (a \wedge b) \equiv a$ <br> $a \wedge (a \vee b) \equiv a$| `a or (a and b) == a` <br> `a and (a or b) == a` |
    """)
    return


@app.cell
def _():
    # code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practice 3
    Translate the following English sentence into Boolean expressions in Python:

    1. The light is on.

    2. You can ride the rollercoaster if you are taller than 48 inches and not afraid of heights.

    3. Send a reminder if the task is overdue or if it's due today and the user hasn't checked it off yet.

    4. Show the discount if the customer is a premium member, or if it's Black Friday and they're added at least one sale item to their cart, all unless the coupon has already been applied.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Section 2.4
    > In order for programs to have different outcomes based on different inputs, it must have **branches**. The different outcomes of these branches are chosen by conditionals, a combination of comparative and/or logical operations.

    ## Branching
    To branch in Python, or almost every modern programming language, you need `if`, `elif` (else if), and `else` statements.
    """)
    return


@app.cell
def _():
    # code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practice 4
    ```py
    age = int(input("Enter age: "))

    if age >= 65:
        print("You can retire")
    elif age >= 35:
        print("You can become president")
    elif age >= 18:
        print("You can vote")
    elif age >= 16:
        print("You can drive")
    else:
        print("Not old enough for anything yet")
    ```

    1. After reading the code, what can you conclude the purpose of the program is?

    2. What would be the output if a user were to input the number 20?

    3. If the `elif`s were all `if`s instead, what would then be the output for the input of 20?
    """)
    return


if __name__ == "__main__":
    app.run()
