import click
import time
from .exceptions import InvalidPermission
from .common import bot_perms_key, bot_perms

__version__ = "2.0.0"

@click.group()
def cli():
    """The CLI for DisOAuth"""
    pass

@cli.command()
def version():
    """Displays the version"""
    click.echo(f"Version: {__version__}")

@cli.command(help="For anything to do with bot permissions")
@click.option("--help",
              "-h",
              is_flag=True)
@click.option("--translate",
              "-t",
              is_flag=True)
@click.option("--list", 
              "-l",
              is_flag=True)
@click.argument("perms",
                nargs=-1, 
                type=click.INT)
def perms(help, translate, list, perms):
    """Anything to do with bot permissions. For the help page use 'discoauth perms -h'"""
    if help is False:
        if translate is True:
            if list is True:
                raise RuntimeError("You cannot pass these options at the same time")
            for perm in perms:
                if perm == 43 or perm == 44:
                    raise ValueError("43 and 44 are not valid permissions")
                click.echo(f"'{perm}' is translated to '{bot_perms_key[perm].lower()}'")
        if list is True:
            if len(perms) == 0:
                click.echo("The following permissions are available:\n")
                for perm in bot_perms_key:
                    click.echo(f"  {perm}: {bot_perms_key[perm]}")
                    time.sleep(0.01)
            elif len(perms) > 1:
                raise RuntimeError("You can pass either nothing, or a permissions value")
            elif len(perms) == 1:
                click.echo(f"\n\nThe permission value '{perms[0]}' includes the following permissions:\n")
                for p in perms:
                    for perm in bot_perms:
                        if (p & bot_perms[perm]) == bot_perms[perm]:
                            click.echo(f"  {perm.lower()}")
                            time.sleep(0.001)
                click.echo("\n")   
        else:
            value = 0x0
            permValue = 0
            for p in perms:
                if (value & bot_perms[bot_perms_key[p]]) != bot_perms[bot_perms_key[p]]:
                    value |= bot_perms[bot_perms_key[p]]
            click.echo(f"Value: {value}")
    elif help is True:
        if translate is True or list is True:
            raise RuntimeError("You cannot pass these options at the same time")
        click.echo("Usage: main.py perms [OPTIONS] [ARGS]")
        click.echo("\nCalculates the permissions value")
        click.echo("Takes a permission number, and returns the value")
        click.echo("\nArguments:")
        click.echo("  Perms            The permissions you want to pass")
        click.echo("\nOptions:")
        click.echo("  --help, -h       Displays this extended help message")
        click.echo("  --translate, -t  Translates the permission number to it's named alternative")
        click.echo("  --list, -l       Lists the possible permissions, and if a permission value is passed, list all the permissions that make up that value")
        
        

if __name__ == "__main__":
    cli()
