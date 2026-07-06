# 🔬 Label Intelligence Tracker

A zero-cost prototype that tells you whether a substance amount you read off a
food, water, or product label is **Safe / Caution / Harmful**, based on public
health reference limits (WHO, FSSAI, FDA guidelines).


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


This is an educational prototype, not medical or regulatory advice. Thresholds
are approximate public reference values; always check official labeling and
consult a professional for health decisions.
