from typer import Typer
from rich.console import Console
from subprocess import check_output
from os.path import isfile

console = Console()
builder = Typer()

editor = "vim"

#@builder.command(help="This command sets the editor to use for editing PKGBUILD. Default value vim")
#def editor(editor: editor):

@builder.command()
def main():
    console.print("Welcome to arnix-builder")
    console.print(f"[green]> checking for [/green][cyan]PKGBUILD[/cyan]")
    if isfile("PKGBUILD") != True:
        console.print(f"[red] error:- [/red] [cyan]PKGBUILD[/cyan] not found")
        exit(1)
    else:
        pass

if __name__ == "__main__":
    builder()
