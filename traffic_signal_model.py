import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample data: [traffic_density, emergency_vehicle, time_of_day]
X = np.array([
    [80, 0, 0], [30, 0, 1], [10, 1, 2], [90, 0, 1], [50, 1, 0],
    [20, 0, 2], [70, 1, 1], [40, 0, 0]
])
y = np.array([1, 0, 1, 1, 1, 0, 1, 0])  # 1 = Green, 0 = Red

model = RandomForestClassifier()
model.fit(X, y)

# Save model
import pickle

# after training your model
with open("signal_model.pkl", "wb") as f:
    pickle.dump(model, f)
