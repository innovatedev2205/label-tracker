"""
Reference thresholds for common substances found on food / water labels.
Sources (approximate, for prototype/educational use — NOT medical advice):
- WHO daily intake guidelines (sugar, sodium, saturated fat, trans fat)
- FSSAI / BIS drinking water & food safety standards (coliform, preservatives)
- FDA daily values (caffeine)

Each entry defines:
- unit: expected unit of measurement
- daily_limit: the recommended max safe daily intake (for per-day tracking)
- danger_zone: value at/above which it's considered clearly harmful regardless of daily total
- category: "nutrient" (moderation-based) or "contaminant" (zero-tolerance based)
- note: short plain-English explanation
"""

THRESHOLDS = {
    "Sodium": {
        "unit": "mg",
        "daily_limit": 2000,
        "danger_zone": 2300,
        "category": "nutrient",
        "note": "WHO recommends under 2000mg/day. High sodium raises blood pressure risk.",
    },
    "Added Sugar": {
        "unit": "g",
        "daily_limit": 25,
        "danger_zone": 50,
        "category": "nutrient",
        "note": "WHO recommends under 25g/day free sugars for adults; 50g is the upper limit.",
    },
    "Saturated Fat": {
        "unit": "g",
        "daily_limit": 20,
        "danger_zone": 30,
        "category": "nutrient",
        "note": "Keep under ~20g/day to reduce cardiovascular risk.",
    },
    "Trans Fat": {
        "unit": "g",
        "daily_limit": 2,
        "danger_zone": 2,
        "category": "nutrient",
        "note": "WHO recommends eliminating trans fat; even small amounts add cardiovascular risk.",
    },
    "Caffeine": {
        "unit": "mg",
        "daily_limit": 400,
        "danger_zone": 600,
        "category": "nutrient",
        "note": "FDA cites 400mg/day as generally safe for healthy adults.",
    },
    "Sodium Benzoate": {
        "unit": "ppm",
        "daily_limit": 700,
        "danger_zone": 1000,
        "category": "nutrient",
        "note": "Permitted preservative; regulatory limits vary by food category (~700-1000ppm typical cap).",
    },
    "Potassium Sorbate": {
        "unit": "ppm",
        "daily_limit": 1000,
        "danger_zone": 2000,
        "category": "nutrient",
        "note": "Permitted preservative; generally regarded safe within regulatory limits.",
    },
    "Coliform Count": {
        "unit": "CFU/100ml",
        "daily_limit": 0,
        "danger_zone": 1,
        "category": "contaminant",
        "note": "Potable water/food should show ZERO coliform. Any detectable presence signals contamination risk.",
    },
    "Total Plate Count": {
        "unit": "CFU/g",
        "daily_limit": 10000,
        "danger_zone": 100000,
        "category": "contaminant",
        "note": "Indicates general microbial load; high counts suggest poor hygiene/spoilage risk.",
    },
    "Lead": {
        "unit": "ppm",
        "daily_limit": 0.01,
        "danger_zone": 0.02,
        "category": "contaminant",
        "note": "Heavy metal contaminant; WHO limit in drinking water is 0.01 mg/L (ppm). No safe exposure level.",
    },
}

def get_substance_names():
    return list(THRESHOLDS.keys())

def evaluate(name, amount):
    """Return a verdict dict for a given substance name and amount found."""
    data = THRESHOLDS.get(name)
    if not data:
        return None

    limit = data["daily_limit"]
    danger = data["danger_zone"]
    category = data["category"]

    if category == "contaminant":
        # zero-tolerance: any presence above the limit is a problem
        if amount <= limit:
            verdict = "Safe"
        elif amount < danger:
            verdict = "Caution"
        else:
            verdict = "Harmful"
        pct = None
    else:
        pct = round((amount / limit) * 100) if limit > 0 else 0
        if amount < limit * 0.5:
            verdict = "Safe"
        elif amount < limit:
            verdict = "Caution"
        else:
            verdict = "Harmful" if amount >= danger else "Caution"

    return {
        "name": name,
        "amount": amount,
        "unit": data["unit"],
        "verdict": verdict,
        "pct_of_daily_limit": pct,
        "note": data["note"],
        "category": category,
    }
