import joblib
import numpy as np

# Load the trained model
model = joblib.load("migraine_model.pkl")

# Feature explanations dictionary
questions = {
    "Age": "Enter your age (e.g., 30)",
    "Duration": "How long do your headaches usually last? (1 = <30 mins, 2 = 30 mins–2 hours, 3 = 2–4 hours, 4 = 4–72 hours)",
    "Frequency": "How often do you get headaches in a month? (e.g., 1 = rarely, 5 = frequently)",
    "Location": "Where is the pain mostly located? (0 = No pain, 1 = One side, 2 = Both sides)",
    "Character": "What is the type of pain? (1 = Pulsating/throbbing, 2 = Sharp, 3 = Dull)",
    "Intensity": "How strong is the pain? (1 = Mild, 2 = Moderate, 3 = Severe)",
    "Nausea": "Do you feel like vomiting or have an upset stomach during headache? (0 = No, 1 = Yes)",
    "Vomit": "Do you actually vomit during a headache? (0 = No, 1 = Yes)",
    "Phonophobia": "Are you sensitive to sounds during a headache? (0 = No, 1 = Yes)",
    "Photophobia": "Are you sensitive to light during a headache? (0 = No, 1 = Yes)",
    "Visual": "Do you see flashing lights, zigzag lines, or blind spots? (0 = No, 1 = Yes)",
    "Sensory": "Do you feel tingling or numbness (e.g., in hands or face)? (0 = No, 1 = Yes)",
    "Dysphasia": "Do you have trouble speaking or finding the right words? (0 = No, 1 = Yes)",
    "Dysarthria": "Is your speech slurred during an attack? (0 = No, 1 = Yes)",
    "Vertigo": "Do you feel like the room is spinning? (0 = No, 1 = Yes)",
    "Tinnitus": "Do you hear ringing or buzzing in your ears? (0 = No, 1 = Yes)",
    "Hypoacusis": "Do you feel like your hearing is reduced during attacks? (0 = No, 1 = Yes)",
    "Diplopia": "Do you see double vision during headache? (0 = No, 1 = Yes)",
    "Defect": "Do you temporarily lose vision in part of your visual field? (0 = No, 1 = Yes)",
    "Ataxia": "Do you feel off balance or uncoordinated (like difficulty walking)? (0 = No, 1 = Yes)",
    "Conscience": "Do you lose consciousness or black out? (0 = No, 1 = Yes)",
    "Paresthesia": "Do you experience prickling or 'pins and needles' sensations? (0 = No, 1 = Yes)",
    "DPF": "Do you have Difficulty Performing Daily Functions during a headache? (0 = No, 1 = Yes)"
}

# Display title
print("🧠 Migraine Type Prediction System")
print("Please answer the following questions.\n")
print("Enter numbers as indicated (e.g., 0 = No, 1 = Yes, etc.)\n")

# Collect user input
user_input = []
for feature, question in questions.items():
    while True:
        try:
            value = int(input(f"{question}\n→ {feature}: "))
            user_input.append(value)
            break
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Convert to model input
input_array = np.array(user_input).reshape(1, -1)

# Predict
prediction = model.predict(input_array)

# Output result
print("\n✅ Prediction Result:")
print(f"🩺 You most likely have: {prediction[0]}")
