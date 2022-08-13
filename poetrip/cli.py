import typer
from poetrip import PyProject

app = typer.Typer(add_completion=False)


@app.command()
def pipfile(
        pyproject_file: str = typer.Option('pyproject.toml', "--from", "-f"),
        pipfile_file: str = typer.Option("Pipfile", "--to", "-t")
):
    pyproject = PyProject.from_file(pyproject_file)
    pipfile = pyproject.to_pipfile()

    pipfile.to_file(pipfile_file)
