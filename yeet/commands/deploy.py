import click


@click.command()
@click.option('--into', help='the alias of the environment', type=str)
@click.option('--service', help='the service name', type=str)
def cli(into: str, service: str = 'all'):
    """Deploys one or all services and layers"""
    click.echo('')
    click.echo('')
    click.echo(f'Y33ting the build into {into}')
    click.echo('')
    click.echo('')
cd ../