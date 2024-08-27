import click
import pandas as pd
import ss_insights_tool.analyze_df as adf

CSV_FILE_PATH = "ss_data.csv"  # This file is in the ss_health_insights dir!

'''Groups all of the commands under the 'cli' command'''
@click.group()
def cli():
    pass

@click.command()
def analyze_gender():
    df = pd.read_csv(CSV_FILE_PATH)
    adf.show_and_clear_gender(df)

@click.command()
def analyze_ages():
    df = pd.read_csv(CSV_FILE_PATH)
    adf.show_and_clear_ages(df)

@click.command()
def analyze_anxiety():
    df = pd.read_csv(CSV_FILE_PATH)
    adf.show_anxiety_levels(df)

@click.command()
def analyze_stress():
    df = pd.read_csv(CSV_FILE_PATH)
    adf.show_stress_levels(df)

@click.command()
def analyze_depression():
    df = pd.read_csv(CSV_FILE_PATH)
    adf.show_depression_levels(df)

cli.add_command(analyze_gender)
cli.add_command(analyze_ages)
cli.add_command(analyze_anxiety)
cli.add_command(analyze_stress)
cli.add_command(analyze_depression)

if __name__ == "__main__":
    cli()