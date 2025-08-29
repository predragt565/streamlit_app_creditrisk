import streamlit as st
import os
import joblib
import pandas as pd
import plotly.express as px
import numpy as np
import hashlib
import json

# Setting up the global colour palette template:
# Setting up the global colour palette template:
import plotly.io as pio

# Example themes: "plotly_dark", "plotly_white", "ggplot2", "simple_white"
pio.templates.default = "ggplot2"

# Define a global blue-green colorway for all charts
pio.templates["ggplot2"].layout.colorway = [
    "#066e69",  # Soft teal / ocean
    "#17becf",  # Cyan / turquoise
    "#2ca02c",  # Vibrant green
    "#66c2a5",  # Soft teal
    "#005f73",  # Deep teal / ocean
    "#8dd3c7"   # Light aqua
]
pio.templates["ggplot2"].layout.coloraxis.colorscale = [
    [0.0,  "#dbe9f6"],  # very light blue
    [0.2,  "#a6c8e4"],  # soft sky blue
    [0.4,  "#5fa8d3"],  # medium blue
    [0.6,  "#2b7bba"],  # deep blue
    [0.8,  "#084d91"],  # darker navy
    [1.0,  "#031f4b"]   # almost black navy
]


# ------------------------------ #
# Help functions
# ------------------------------ #

@st.cache_resource
def load_artifacts():
    # Modell laden:
    model_files = ["xgb_credit_model.pkl", "extra_trees_credit_model.pkl"]
    model = None
    used_model_path = None
    for mf in model_files:
        if os.path.exists(mf):
            model = joblib.load(mf)
            used_model_path = mf
        break
    if model is None:
        st.error("Kein Modell gefunden, lege z.B. eine 'xgb_credit_model.pkl' Datei an.")
        st.stop()
    
    # Feature Reihenfolge bestimmen:
    feature_names_path = "feature_names.pkl"
    if os.path.exists(feature_names_path):
        feature_order = joblib.load(feature_names_path)
    else:
        st.warning("")
        st.stop()
    
    # Encoder laden:
    cat_cols = ["Sex", "Housing", "Saving accounts", "Checking account", "Purpose"]
    encoders = {}
    missing = []
    for col in cat_cols:
        pkl = f"ml_models/{col}_credit_encoder.pkl"
        # print(pkl)
        if os.path.exists(pkl):
            encoders[col] = joblib.load(pkl)
        else:
            missing.append(col)
    if missing:
        st.warning(f"Fehlende Encoder: {missing} - App funktioniert nicht!")
        st.stop()
    
    return model, used_model_path, encoders, feature_order

def options(col):
    enc = ENCODERS.get(col)
    # print(getattr(enc, "classes_"))
    return list(getattr(enc, "classes_")) if enc is not None else[]

def encode_value(col, value):
    enc = ENCODERS.get(col)
    if enc is None:
        return value
    return enc.transform([value])[0]    # <- transforms-replaces input value from the apps's field with the corresponding value from the .pkl encoder

# Hilfsfunktion zum Hashen der Eingaben
def get_input_hash(inputs: dict) -> str:
    # Convert all numpy types to native Python types
    cleaned_inputs = {
        k: (v.item() if hasattr(v, "item") else v)
        for k, v in inputs.items()
    }
    return hashlib.md5(json.dumps(cleaned_inputs, sort_keys=True).encode()).hexdigest()


# ------------------------------ #
# MAIN
# ------------------------------ #
# Grundlägende Konfiguration:
st.set_page_config(page_title="Credit Risk Prediction", page_icon="💳" ,layout="wide")
st.title("Credit Risk Prediction")
st.caption("Demo für den German Credit Data Datensatz")

# Modell & Encoders laden:
with st.spinner("Lade ML-Model..."):
    model, user_model_path, ENCODERS, FEATURE_ORDER =  load_artifacts() # (w, x, y, z), Tupel entpacken
if "model_toast_done" not in st.session_state:
    st.toast("Modell erfolgreich geladen!")
    st.session_state["model_toast_done"] = True

# Sidebar Menü:
with st.sidebar:
    st.header("Eingaben")
    
    # Einfache Defaults:
    age = st.number_input("Age", min_value=18, max_value=80, value=30, step=1)
    sex = st.selectbox("Sex", options=options("Sex") or ["male", "female"])
    job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1, step=1)
    housing = st.selectbox("Housing", options=options("Housing"))
    saving_accounts = st.selectbox("Saving accounts", options=options("Saving accounts"))
    checking_account = st.selectbox("Checking account", options=options("Checking account"))
    purpose = st.selectbox("Purpose", options=options("Purpose"))
    credit_amount = st.number_input("Credit amount", min_value=1000, max_value=100000, step=100, value=5000)
    duration = st.number_input("Duration (months)", min_value=1, max_value=60, step=1, value=12)
    
    # Entscheidungsschwelle: (decide when is good or bad)
    st.divider()
    st.subheader("Einstellungen")
    threshold = st.slider("Entscheidungsschwelle ('Bad' ab):", 0.05, 0.95, 0.50, 0.01)
    

# Eine modellkonforme Eingabe erzeugen:
row = {
    "Age": age,
    "Job": job,
    "Sex": encode_value("Sex", sex),
    "Housing": encode_value("Housing", housing),
    "Saving accounts": encode_value("Saving accounts", saving_accounts),
    "Checking account": encode_value("Checking account", checking_account),
    "Credit amount": credit_amount,
    "Duration": duration,
    "Purpose": encode_value("Purpose", purpose)
}
input_df = pd.DataFrame([row])
input_df = input_df[FEATURE_ORDER]
# print(input_df)
# print(FEATURE_ORDER)

# Navigationsmenü erstellen
tab_pred, tab_whatif, tab_explain, tab_about = st.tabs(["📑 Predictions", "❔ What-If", "✅ Erklärung", "ℹ️ About"])

# ------------------------------- #
# Vorhersagen (Predictions-Menü):
# ------------------------------- #

# Aktueller Eingabe-Hash
current_input_hash = get_input_hash(row)

with tab_pred:
    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("Modell-konformes Input")
        st.dataframe(input_df)  #, use_container_width=True)
        st.info(f"Aktives Modell: {user_model_path}")
    with c2:
        st.subheader("Vorhersage")
        
        risiko_button_clicked = st.button("Risiken vorhersagen")
        if risiko_button_clicked:
            st.session_state["just_predicted"] = True  # <- Flag SOFORT setzen (vor der Warnung)

        # Warnung bei veralteter Vorhersage (nur wenn nicht gerade neu vorhergesagt)
        if (
            "last_input_hash" in st.session_state
            and st.session_state.get("prediction_made")
            and current_input_hash != st.session_state["last_input_hash"]
            and not st.session_state.get("just_predicted", False)
        ):
            st.warning("⚠️ Achtung: Vorhersage basiert auf alten Eingaben.")

        # Wenn Button geklickt wurde → Session-State aktualisieren
        if risiko_button_clicked:
            X = input_df
            proba = model.predict_proba(X)[0]
            print(f"Vorhersage: {proba}")
            p_bad = float(proba[1])
            is_bad = p_bad >= threshold
            st.metric("Bad-Risiko", f"{p_bad:.1%}")
            # print(min(max(p_bad, 0.0), 1.0)) #[0, 1]
            st.progress(min(max(p_bad, 0.0), 1.0))
            if is_bad:
                st.error(f"Einstuffung: **BAD** $\geq$ {threshold:.0%}")
            else:
                st.success(f"Einstuffung: **GOOD** $<$ {threshold:.0%}")

            with st.expander("Was bedeutet das?"):
                st.write(
                    """
                    * Das Modell gibt eine Wahrscheinlichkeit für 'bad' aus (Zahlungsauswall-Risiko).
                    * Über den Schwellenwert bestimmst du, ab wann aus der Wahrscheinlichkeit
                    eine binäre Entscheidung (GOOD/BAD) wird
                    """
                )

            st.session_state["prediction_made"] = True
            st.session_state["prediction_result"] = {
                "p_bad": p_bad,
                "is_bad": is_bad,
                "threshold": threshold
            }
            st.session_state["last_input_hash"] = current_input_hash
        
        # Falls bereits Vorhersage gemacht wurde, erneut anzeigen
        elif st.session_state.get("prediction_made") and st.session_state.get("prediction_result"):
            result = st.session_state["prediction_result"]
            st.metric("Bad-Risiko", f"{result['p_bad']:.1%}")
            st.progress(min(max(result["p_bad"], 0.0), 1.0))
            if result["is_bad"]:
                st.error(f"Einstuffung: **BAD** $\geq$ {result['threshold']:.0%}")
            else:
                st.success(f"Einstuffung: **GOOD** $<$ {result['threshold']:.0%}")

            with st.expander("Was bedeutet das?"):
                st.write(
                    """
                    * Das Modell gibt eine Wahrscheinlichkeit für 'bad' aus (Zahlungsauswall-Risiko).
                    * Über den Schwellenwert bestimmst du, ab wann aus der Wahrscheinlichkeit
                    eine binäre Entscheidung (GOOD/BAD) wird
                    """
                )
    # RESET just_predicted FLAG (nach dem Run zurücksetzen)
    if st.session_state.get("just_predicted"):
        st.session_state["just_predicted"] = False
    
# Einfluss einzelner Features:
with tab_whatif:
    st.subheader("What-if-Analyse: Wie ändert sich das Risiko, wenn ich ein Feature variiere?")
    feature_to_vary = st.selectbox("Feature wählen", FEATURE_ORDER)
    is_categorical = feature_to_vary in ENCODERS
    # print(ENCODERS)
    # print(feature_to_vary)
    # print(is_categorical)
        
    base = input_df.iloc[0].copy()
    
    if is_categorical:
        cats = list(ENCODERS[feature_to_vary].classes_)
        # print(cats)
        picked_cat = st.selectbox("Wert setzen", cats)
        vary_values_enc = ENCODERS[feature_to_vary].transform(cats)
        min_val = max_val = None
    else:
        current_val = float(base[feature_to_vary])
        c1, c2 = st.columns(2)
        with c1:
            min_default = max(0.0, current_val * 0.5)
            max_default = max(current_val * 1.5, current_val * 1.0)
            min_val, max_val = st.slider(
                "Bereich",
                min_value=0.0,
                max_value=float(max_default *2),
                value=(float(min_default), float(max_default)),
                step=1.0
            )
            
        #     min_val = st.number_input("Min", value=current_val * 0.5, min_value=0.0, step=1.0)
        # with c2:
        #     max_val = st.number_input("Max", value=current_val, min_value=min_val + 1, step=1.0)
        with c2:
            steps = st.slider("Schritte", 3, 50, 11)
        vary_values_raw = np.linspace(min_val, max_val,int(steps))
        cats = [float(v) for v in vary_values_raw]
        vary_values_enc = vary_values_raw
    
    b1, b2 = st.columns([1, 1])
    with b1:
        if st.button("What-if berechnen"):
            st.session_state["whatif_active"] = True
    with b2:
        if st.button("Auto-Update stoppen"):
            st.session_state["whatif_active"] = False
        
    if st.session_state.get("whatif_active", False):
        if (min_val is not None) and (max_val is not None) and (max_val <= min_val):
            st.warning("Max muss größer als Min sein.")
        else:
            probs = []
            labels = []
            for val_raw, val_enc in zip(cats, vary_values_enc):
                row_mut = base.copy()
                row_mut[feature_to_vary] = val_enc
                X_mut = pd.DataFrame([row_mut])[FEATURE_ORDER]
                p_bad = model.predict_proba(X_mut)[0][1]
                probs.append(p_bad)
                labels.append(val_raw)
                
            chart_df = pd.DataFrame({
                "Wert": labels,
                "Bad-Risiko": probs
            })
            chart_df.set_index("Wert")

            fig = px.bar(
                chart_df,
                x="Wert",
                y="Bad-Risiko",
                text="Bad-Risiko",
                color="Bad-Risiko",
                color_continuous_scale=pio.templates["ggplot2"].layout.coloraxis.colorscale
            )
            fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
            fig.update_layout(
                yaxis=dict(title="Risiko"),
                xaxis=dict(title=feature_to_vary),
                title=f"What-if Analyse für {feature_to_vary}"
            )
            st.plotly_chart(fig)
    
    