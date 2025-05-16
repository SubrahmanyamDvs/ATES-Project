import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Directions: N=0, E=1, S=2, W=3

# Training data: distances from ambulances (use 9999 if no ambulance)
X = [
    [150, 9999, 9999, 9999],  # Case 1: Ambulance from North
    [9999, 140, 9999, 9999],  # Case 2: Ambulance from East
    [9999, 9999, 145, 200],   # Case 3: Ambulances South & West (nearest S)
    [150, 150, 145, 160],     # Case 4: All ambulances present
]

# Labels: priority direction (0=N,1=E,2=S,3=W)
y = [0, 1, 2, 2]  # For case 4, let's give South highest priority for demo

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

with open("signal_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Dummy model trained and saved as signal_model.pkl")
