import click

@click.command()
@click.argument('git_url', nargs=-1)
def cli(git_url):
    """Script used to submit PyTorch models to the blockchain for training.

    \b
    Submit project from GitHub:
        tcsubmit https://github.com/nick11roberts/PGCnet/
    """

    ### Sends request containing url to someone in the mining pool
    click.echo(git_url)
