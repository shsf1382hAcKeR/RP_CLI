from setuptools import setup, find_packages

setup(
    name='RP_CLI',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'typer',
        'inquirer'
    ],
    entry_points='''
        [console_scripts]
        rp-cli=rp_cli.cli:cli
    ''',
)
