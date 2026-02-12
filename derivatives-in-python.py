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


if __name__ == "__main__":
    app.run()
