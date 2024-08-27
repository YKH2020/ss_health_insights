from setuptools import setup, find_packages

setup(
    name='ss_insights_tool',
    description='''allows users (particularly therapists) to view concise and organized heatmap information 
    regarding university students' mental health (from an MIT licensed dataset) through prompts.''',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==2.1.0',
        'pandas==2.2.2',
        'matplotlib==3.9.0',
        'scikit-learn',
        'click',
        'seaborn',
    ],
    entry_points={
        'console_scripts': [
            'analyze-gender=cli:analyze_gender',
            'analyze-ages=cli:analyze_ages',
            'analyze-anxiety=cli:analyze_anxiety',
            'analyze-stress=cli:analyze_stress',
            'analyze-depression=cli:analyze_depression',
        ],
    },
    author='Yash Hegde',
    author_email='ykh2@duke.edu',
)
