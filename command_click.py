import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--pro', '-n', default="longitude", help='build pro name')
def run(pro):
    pass


@cli.command()
@click.option("--modules_path", "-p", default='utils', help='module path')
def find_path(modules_path):
    pass


if __name__ == '__main__':
    cli()
