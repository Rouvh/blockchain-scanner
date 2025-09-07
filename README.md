# Blockchain Scanner
A FastAPI app to detect blockchain anomalies using machine learning.

## Description
This project uses FastAPI to provide an API endpoint (/analyze) for detecting anomalies in blockchain transactions, powered by the Transformers library.

## Deployment
Deployed on Render at https://blockchain-scanner-app.onrender.com/analyze.

## Setup
- Install dependencies: `pip install -r requirements.txt`
- Run with: `uvicorn app:app --host 0.0.0.0 --port 7860`