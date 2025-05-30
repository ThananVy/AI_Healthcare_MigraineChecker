from customtkinter import *
from tkinter import messagebox
from PIL import Image
import numpy as np
import joblib

# Load your trained model
model = joblib.load("migraine_model.pkl")

# Define feature explanations and values
features = [
    ("Age", "How old are you?"),
    ("Duration", "How long does your headache last? (1=short, 5=all day)", ["1", "2", "3", "4", "5"]),
    ("Frequency", "How often do you get headaches in a month?", ["1", "2", "3", "4", "5"]),
    ("Location", "Where does it hurt?", ["0 (none)", "1 (one side)", "2 (both sides)"]),
    ("Character", "Type of pain?", ["1 (throbbing)", "2 (sharp)", "3 (dull)"]),
    ("Intensity", "Pain strength?", ["1 (mild)", "2 (medium)", "3 (severe)"]),
    ("Nausea", "Feel like vomiting?", ["0 (No)", "1 (Yes)"]),
    ("Vomit", "Do you vomit?", ["0 (No)", "1 (Yes)"]),
    ("Phonophobia", "Loud sounds hurt?", ["0 (No)", "1 (Yes)"]),
    ("Photophobia", "Light hurts?", ["0 (No)", "1 (Yes)"]),
    ("Visual", "See flashes or zigzags?", ["0 (No)", "1 (Yes)"]),
    ("Sensory", "Feel numb/tingling?", ["0 (No)", "1 (Yes)"]),
    ("Dysphasia", "Hard to speak?", ["0 (No)", "1 (Yes)"]),
    ("Dysarthria", "Slurred speech?", ["0 (No)", "1 (Yes)"]),
    ("Vertigo", "Room spinning?", ["0 (No)", "1 (Yes)"]),
    ("Tinnitus", "Ringing in ears?", ["0 (No)", "1 (Yes)"]),
    ("Hypoacusis", "Hear less?", ["0 (No)", "1 (Yes)"]),
    ("Diplopia", "See double?", ["0 (No)", "1 (Yes)"]),
    ("Defect", "Lose vision?", ["0 (No)", "1 (Yes)"]),
    ("Ataxia", "Wobbly or clumsy?", ["0 (No)", "1 (Yes)"]),
    ("Conscience", "Fainting or blackout?", ["0 (No)", "1 (Yes)"]),
    ("Paresthesia", "Pins and needles?", ["0 (No)", "1 (Yes)"]),
    ("DPF", "Does it affect your daily life?", ["0 (No)", "1 (Yes)"]),
]

# Explanations for predictions
explanations = {
    "Migraine without aura": "Regular migraine with pain, maybe nausea, but no warning signs like flashing lights.",
    "Migraine with aura": "Migraine with signs like flashing lights or blurry vision before pain starts.",
    "Typical aura with migraine": "You see signs before the headache, like zigzag or bright lights.",
    "Typical aura without migraine": "You see the signs but don't get the headache.",
    "Familial hemiplegic migraine": "A rare inherited migraine that causes one side of your body to feel weak.",
    "Sporadic hemiplegic migraine": "Like familial, but it doesn't run in families.",
    "Basilar-type migraine": "Rare migraine that causes dizziness, double vision, or fainting."
}

# GUI setup
set_appearance_mode("dark")
app = CTk()
app.geometry("700x900")
app.title("🧠 Migraine Type Predictor")

main_frame = CTkScrollableFrame(app, width=680, height=1000)
main_frame.pack(padx=10, pady=10)

entry_widgets = {}

CTkLabel(main_frame, text="Migraine Checker", font=("Arial", 24)).pack(pady=10)

def create_fields():
    for i, feature in enumerate(features):
        # Sub-frame to hold label and input in a row
        row_frame = CTkFrame(main_frame)
        row_frame.pack(fill="x", padx=10, pady=5)

        # Label on the left
        label = CTkLabel(row_frame, text=f"{feature[0]}:", font=("Arial", 14), width=180, anchor="w")
        label.grid(row=0, column=0, sticky="w", padx=(0, 10))

        # Explanation under the label (optional)
        help_text = CTkLabel(row_frame, text=feature[1], font=("Arial", 10), text_color="gray", anchor="w")
        help_text.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))

        # Combobox or Entry on the right
        if len(feature) == 3:  # Dropdown
            combo = CTkComboBox(row_frame, values=feature[2], fg_color="#0093E9",
                                border_color="#FBAB7E", dropdown_fg_color="#0093E9", width=200)
            combo.grid(row=0, column=1, sticky="w")
            entry_widgets[feature[0]] = combo
        else:  # Text Entry
            entry = CTkEntry(row_frame, width=200)
            entry.grid(row=0, column=1, sticky="w")
            entry_widgets[feature[0]] = entry


create_fields()

# Predict function
def predict():
    try:
        data = []
        for f in features:
            name = f[0]
            widget = entry_widgets[name]
            val = widget.get().strip()
            if val == "":
                raise ValueError(f"Missing value for {name}.")
            # Only take the number from value (e.g., "1 (Yes)" => 1)
            num = int(val.split(" ")[0]) if "(" in val else int(val)
            data.append(num)

        if len(data) != 23:
            raise ValueError("All fields must be filled!")

        prediction = model.predict(np.array(data).reshape(1, -1))[0]
        explain = explanations.get(prediction, "Unknown type. Please consult a doctor.")

        messagebox.showinfo("Result", f"🧠 Migraine Type: {prediction}\n\nℹ️ Meaning: {explain}")
    except Exception as e:
        messagebox.showerror("Input Error", f"⚠️ {e}")

# Predict button
CTkButton(main_frame, text="🔍 Predict Now", command=predict,
          fg_color="#4158D0", hover_color="#C850C0",
          border_color="#FFCC70", border_width=2, corner_radius=20).pack(pady=20)

app.mainloop()