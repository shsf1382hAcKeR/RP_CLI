from setuptools import setup, find_packages

setup(
    name='RP_CLI',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'typer',
        'inquirer',
        'click',
        'rich'
    ],
    entry_points='''
        [console_scripts]
        rp-cli=rp_cli.cli:cli
    ''',
)
