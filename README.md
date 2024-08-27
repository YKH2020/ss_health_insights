# SS Health Insights

The SS Health Insights command-line tool allows users (particularly therapists) to view concise and organized information regarding university students' mental health. This tool provides heatmaps based on an MIT-licensed dataset.

## Setup Instructions

Follow these steps to set up and use the SS Health Insights tool:

### 1. Navigate to the Project Directory

Open your terminal or command prompt and navigate to the directory where the `ss_health_insights` project is located:

```bash
cd path/to/your/project/ss_health_insights
```

### 2. Set Up a Virtual Environment

On Windows: 
```bash
python -m venv venv
venv\Scripts\activate
```

On MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Project in Development Mode
```bash
python setup.py develop
```

### 4. Use any of the 5 CLI Commands from here!
```bash
analyze-gender
analyze-ages
analyze-anxiety
analyze-stress
analyze-depression
```