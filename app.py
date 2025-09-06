from fastapi import FastAPI, Request
from transformers import pipeline
import json

app = FastAPI()
model_name = "microsoft/Phi-3-mini-4k-instruct"  # Lightweight model for deployment
classifier = pipeline("zero-shot-classification", model=model_name)

def analyze_tx(tx_data, chain):
    prompt = f"Transaction on {chain}: {json.dumps(tx_data)}. Detect anomalies: flash loan (large borrow/repay), fake USDT (invalid contract). Risk score 0-100. Explanation:"
    result = classifier(prompt, candidate_labels=["normal", "flash loan attack", "fake token simulation"])
    score = result['scores'][result['labels'].index(result['labels'][0])] * 100
    explanation = f"Detected: {result['labels'][0]}. Risk: {score:.2f}. Reason: {prompt.split('.')[1].strip()}"
    return score, explanation

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    score, expl = analyze_tx(data['tx_data'], data['chain'])
    return {"score": score, "explanation": expl}

@app.get("/health")
async def health():
    return {"status": "healthy"}