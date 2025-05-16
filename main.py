
import time
import random

# Sample ambulance data (ID, direction, distance in meters)
ambulances = [
    {"id": 1, "direction": "North", "distance": 280},
    {"id": 2, "direction": "East", "distance": 270},
    {"id": 3, "direction": "South", "distance": 300},
    {"id": 4, "direction": "West", "distance": 300}
]

def predict_direction(ambulance_id):
    # Simulate trajectory prediction logic (normally done with GPS + ML)
    directions = ["Left", "Straight", "Right"]
    return random.choice(directions)

def control_signals(ambulance_list):
    print("Initial Signal Control Check")
    ambulance_list.sort(key=lambda x: x['distance'])

    if len(ambulance_list) == 1:
        print(f"Only one ambulance ({ambulance_list[0]['id']}) approaching from {ambulance_list[0]['direction']}")
        print(f"Signal turned GREEN for {ambulance_list[0]['direction']}, RED for others")
    else:
        distances = [amb['distance'] for amb in ambulance_list]
        if all(dist == distances[0] for dist in distances):
            print("Worst case: All ambulances at same distance")
            print("Predicting direction using map trajectory...")
            predicted = {amb['id']: predict_direction(amb['id']) for amb in ambulance_list}
            print("Predicted Paths:", predicted)

            released = []
            if len(predicted) >= 2:
                dirs_used = set()
                for amb_id, path in predicted.items():
                    if path not in dirs_used:
                        dirs_used.add(path)
                        released.append(amb_id)
                        if len(released) == 2:
                            break
                print(f"Signals GREEN for ambulances: {released}, others RED")
            else:
                print("Signal GREEN for one ambulance only due to conflict")
        else:
            for amb in ambulance_list:
                print(f"Signal GREEN for ambulance {amb['id']} from {amb['direction']} (distance: {amb['distance']}m)")
                print("Waiting for ambulance to pass...")
                time.sleep(1)
                print(f"Signal RED for {amb['direction']} after ambulance {amb['id']} passes")

if __name__ == "__main__":
    print("🚨 Ambulance Traffic Emergency System Activated 🚨")
    control_signals(ambulances)
