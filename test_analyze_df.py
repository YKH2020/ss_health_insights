import pytest
import ss_insights_tool.analyze_df as adf

'''Uses pytest fixture decorator to pass in an example dataframe into the test functions'''
@pytest.fixture
def setup_df():
    import pandas as pd
    df = pd.read_csv("ss_data.csv")
    df = df.head(10)  # Example to limit rows
    return df

'''All of the following test functions test whether the functions in analyze_df.py properly execute.'''
def test_show_and_clear_gender(setup_df):
    try:
        adf.show_and_clear_gender(setup_df)
    except Exception as e:
        pytest.fail(f"show_and_clear_gender failed with exception: {e}")

def test_show_and_clear_ages(setup_df):
    try:
        adf.show_and_clear_ages(setup_df)
    except Exception as e:
        pytest.fail(f"show_and_clear_ages failed with exception: {e}")

def test_show_anxiety_levels(setup_df):
    try:
        adf.show_anxiety_levels(setup_df)
    except Exception as e:
        pytest.fail(f"show_anxiety_levels failed with exception: {e}")

def test_show_stress_levels(setup_df):
    try:
        adf.show_stress_levels(setup_df)
    except Exception as e:
        pytest.fail(f"show_stress_levels failed with exception: {e}")

def test_show_depression_levels(setup_df):
    try:
        adf.show_depression_levels(setup_df)
    except Exception as e:
        pytest.fail(f"show_depression_levels failed with exception: {e}")