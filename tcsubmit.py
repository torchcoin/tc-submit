import click
import emoji
import numpy as np

@click.command()
@click.argument('git_url')
@click.argument('dataset_url')
def cli(git_url, dataset_url):
    """Script used to submit PyTorch models to the blockchain for training.

    \b
    Submit project from GitHub:
        tcsubmit https://github.com/nick11roberts/PGCnet/
    """

    click.echo("Validating repository against submission guidelines...")
    ### TODO Download repo, check repo structure, run tests, etc...

    # For now, randomly select pass/fail
    #if np.random.choice(2):
    if False:
        click.echo(
            """
            Repository does not meet specifications, see
            https://github.com/nick11roberts/torch-coin
            for more information and formatting instructions.
            """)
        exit()

    click.echo(
        emoji.emojize(
            "Passed! :smile: :100: :thumbs_up:", use_aliases=True))

    ### TODO Send model to someone in the mining pool

    click.echo(
        emoji.emojize(
            ":zap: Submitting model...",
            use_aliases=True))

    click.echo(
        emoji.emojize(
            ":mushroom: Model submitted.",
            use_aliases=True))

    click.echo(
        emoji.emojize(
            ":mailbox_with_mail: Download instructions for your trained model will be sent via email, hang tight.",
            use_aliases=True))
