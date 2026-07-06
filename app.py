import streamlit as st
from thresholds import THRESHOLDS, get_substance_names, evaluate

st.set_page_config(page_title="Label Intelligence Tracker", page_icon="🔬", layout="centered")

st.title("🔬 Label Intelligence Tracker")
st.caption("Type in what you read off a food, water, or product label — find out instantly if it's safe.")

st.info(
    "📷 **Coming soon:** scan a label photo instead of typing values. "
    "For this prototype, enter values manually.",
    icon="📷",
)

if "entries" not in st.session_state:
    st.session_state.entries = []

st.subheader("Add a substance from the label")

col1, col2, col3 = st.columns([2, 1.2, 1])
with col1:
    substance = st.selectbox("Substance", get_substance_names())
with col2:
    amount = st.number_input(
        f"Amount ({THRESHOLDS[substance]['unit']})",
        min_value=0.0,
        step=0.1,
        format="%.3f",
    )
with col3:
    st.write("")
    st.write("")
    add_clicked = st.button("➕ Add", use_container_width=True)

if add_clicked:
    st.session_state.entries.append((substance, amount))

if st.session_state.entries:
    st.divider()
    st.subheader("📋 Results")

    verdict_colors = {"Safe": "🟢", "Caution": "🟡", "Harmful": "🔴"}
    overall_harmful = False
    overall_caution = False

    for i, (name, amt) in enumerate(st.session_state.entries):
        result = evaluate(name, amt)
        if result is None:
            continue

        icon = verdict_colors[result["verdict"]]
        with st.container(border=True):
            c1, c2 = st.columns([4, 1])
            c1.markdown(f"**{icon} {result['name']}** — {result['amount']} {result['unit']}")
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.entries.pop(i)
                st.rerun()

            st.markdown(f"**Verdict: {result['verdict']}**")
            if result["pct_of_daily_limit"] is not None:
                st.progress(min(result["pct_of_daily_limit"], 100) / 100)
                st.caption(f"{result['pct_of_daily_limit']}% of recommended daily limit")
            st.caption(result["note"])

        if result["verdict"] == "Harmful":
            overall_harmful = True
        elif result["verdict"] == "Caution":
            overall_caution = True

    st.divider()
    st.subheader("🏁 Overall Verdict")
    if overall_harmful:
        st.error("⚠️ This product contains at least one substance at a HARMFUL level. Consume with caution or avoid.")
    elif overall_caution:
        st.warning("🟡 This product is within limits but has substances worth watching if consumed regularly.")
    else:
        st.success("✅ All checked substances are within safe limits.")

    if st.button("Clear all"):
        st.session_state.entries = []
        st.rerun()
else:
    st.caption("No substances added yet. Pick one above and click Add.")

st.divider()
st.caption(
    "⚠️ Educational prototype only — not medical or regulatory advice. "
    "Thresholds are approximate reference values (WHO / FSSAI / FDA guidelines). "
    "Consult official product labeling and a health professional for decisions."
)
