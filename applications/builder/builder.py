from typer import Typer
from typer import Argument
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from subprocess import check_output
from os.path import isfile , isdir
from os import system , chdir

console = Console()
builder = Typer()

editor = "vim"

@builder.command(help="This has 2 args.. one projdir for the project directory and editor for the editor selection during PKGBUILD")
def main(projdir: str , editor: Optional[str] = Argument(None)):
    if isdir(projdir) == True:
        chdir(projdir)
        pass
    else:
        console.print(Panel(f"[red] error:- [/red] [cyan]{projdir}[/cyan] not found"))
        exit(1)

    console.print("Welcome to arnix-builder")
    console.print(f"[green]> checking for [/green][magenta]PKGBUILD[magenta]")
    if isfile("PKGBUILD") != True:
        console.print(f"[red] error:- [/red] [magenta]PKGBUILD[magenta] not found")
        exit(1)
    else:
        console.print("[cyan]info:- [/cyan] do you want to edit PKGBUILD(y/n)")
        yn = str(input())
        if yn == "y" or yn == "Y" or yn == "yes":
            prcs = system(f"{editor} PKGBUILD")
            if prcs != 0 :
                exit(prcs)
            else:
                pass
        else:
            pass

        console.print("Starting building package..")
        try:
            prcs = check_output(["makepkg" , "-s"]).decode('utf-8')
        except Exception:
            console.print(Panel("[red]error:-[/red] process completed unsucessfully"))
            exit(1)

        console.print("Complete output:-")
        console.print(Panel(f"{prcs}" , expand=1))

        log = open("arnix-builder.log" , "w")
        log.write(str(prcs))
        log.close()

if __name__ == "__main__":
    builder()
