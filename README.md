# 🔬 Label Intelligence Tracker

A zero-cost prototype that tells you whether a substance amount you read off a
food, water, or product label is **Safe / Caution / Harmful**, based on public
health reference limits (WHO, FSSAI, FDA guidelines).

Built for **Challenge Track 1: AI-Powered Decision Intelligence Platform**.

## Why zero cost
This prototype uses a **hardcoded reference database** of known safe limits
(`thresholds.py`) — no AI API calls, no external services. It runs entirely
on Streamlit's own logic, so it costs nothing to run locally and, if deployed,
comfortably fits inside Cloud Run's free tier (2 million requests/month free).

## What it does
1. You read a value off a label (e.g. "Sodium: 850mg" or "Coliform: 2 CFU/100ml").
2. You pick the substance and type the amount.
3. The app compares it against the recommended daily/safety limit and gives:
   - A **Safe / Caution / Harmful** verdict
   - % of the daily recommended limit (for nutrients)
   - A plain-English reason
4. Add multiple substances to get an **overall verdict** for the product.

## Substances covered in the prototype
Sodium, Added Sugar, Saturated Fat, Trans Fat, Caffeine, Sodium Benzoate,
Potassium Sorbate, Coliform Count, Total Plate Count, Lead.
(Easy to extend — just add an entry to `THRESHOLDS` in `thresholds.py`.)

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Cloud Run (free tier)
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

gcloud run deploy label-tracker \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```
No env vars needed — no API key required. The printed Service URL is your
Deployment Link.

## Roadmap (v2 — scan the label)
Replace manual entry with a camera/photo upload:
- Add `pytesseract` + `Pillow` to OCR the label image into text
- Or call the Gemini Vision API (`gemini-2.0-flash`) with the image to extract
  substance names + amounts directly, then feed them into the same
  `evaluate()` function already built here
- The scoring logic (`thresholds.py`) doesn't change at all — only the input
  method does, so this prototype is already scan-ready architecturally.

## Submission checklist
- [ ] Deployment Link → Cloud Run service URL
- [ ] GitHub Repository Link → push this folder
- [ ] Final Project PPT → problem, solution, architecture, demo screenshot, roadmap
- [ ] Demo Video (< 3 min) → add 2-3 substances, show verdicts + overall result
- [ ] Brief description → see below

## Suggested brief description (copy-paste ready)
"Label Intelligence Tracker is a decision-intelligence tool that helps people
understand what's actually in their food and water. Users enter substance
amounts straight off a product label, and the app instantly evaluates them
against WHO/FSSAI/FDA safety guidelines, flagging Safe, Caution, or Harmful
levels with plain-English reasoning. Built as a zero-cost, fully local
prototype, it's architected to scale into a camera-based label scanner in the
next iteration."

## Disclaimer
This is an educational prototype, not medical or regulatory advice. Thresholds
are approximate public reference values; always check official labeling and
consult a professional for health decisions.
