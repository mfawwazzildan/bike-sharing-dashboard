# Bike Sharing Dashboard

Ekstrak file ZIP submission, lalu buka terminal pada folder utama `Submission_DS_Muhammad Fawwaz ZIldan`.

## Setup Environment - Anaconda

```bash
conda create --name main-ds python=3.12
conda activate main-ds
python -m pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```bash
python -m pip install pipenv
pipenv --python 3.12
pipenv install -r requirements.txt
```

## Run Streamlit App

Jika menggunakan Anaconda:

```bash
python -m streamlit run Dashboard/Dashboard.py
```

Jika menggunakan Shell/Terminal (Pipenv):

```bash
pipenv run python -m streamlit run Dashboard/Dashboard.py
```

Dashboard dapat diakses melalui http://localhost:8501.

## Dashboard Online

https://bike-sharing-dashboard-kyfjynzcqgvknbnzfngexi.streamlit.app/
