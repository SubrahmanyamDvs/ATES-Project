from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Mock ambulance data: Each ambulance has distance (m), direction_from, direction_to
# direction_from/to are N, S, E, W
ambulances = [
    {'id': 1, 'distance': 150, 'from': 'N', 'to': 'E'},
    {'id': 2, 'distance': 145, 'from': 'S', 'to': 'W'},
    {'id': 3, 'distance': 200, 'from': 'E', 'to': 'W'},
    {'id': 4, 'distance': 190, 'from': 'W', 'to': 'N'}
]

# Utility function to check if two paths conflict (simplified)
def paths_conflict(a1, a2):
    # If ambulances come from opposite directions and go straight, conflict
    if (a1['from'] == 'N' and a1['to'] == 'S' and a2['from'] == 'S' and a2['to'] == 'N') or \
       (a1['from'] == 'S' and a1['to'] == 'N' and a2['from'] == 'N' and a2['to'] == 'S') or \
       (a1['from'] == 'E' and a1['to'] == 'W' and a2['from'] == 'W' and a2['to'] == 'E') or \
       (a1['from'] == 'W' and a1['to'] == 'E' and a2['from'] == 'E' and a2['to'] == 'W'):
        return True
    # Also conflict if ambulances paths intersect (one going N->E, another S->W)
    # Simplify to these cases:
    crossing_pairs = [
        (('N', 'E'), ('S', 'W')),
        (('S', 'W'), ('N', 'E')),
        (('N', 'S'), ('E', 'W')),
        (('E', 'W'), ('N', 'S'))
    ]
    if ((a1['from'], a1['to']), (a2['from'], a2['to'])) in crossing_pairs or \
       ((a2['from'], a2['to']), (a1['from'], a1['to'])) in crossing_pairs:
        return True
    return False

# Decide green signals for case 4
def case4_priority(ambs):
    # Find ambulances whose paths don't conflict with others
    safe_ambs = []
    for amb in ambs:
        conflict_found = False
        for other in ambs:
            if other['id'] == amb['id']:
                continue
            if paths_conflict(amb, other):
                conflict_found = True
                break
        if not conflict_found:
            safe_ambs.append(amb)
    if safe_ambs:
        # Give green to safe ambulances
        green_ids = [a['id'] for a in safe_ambs]
    else:
        # No safe paths, pick ambulance closest first
        sorted_ambs = sorted(ambs, key=lambda x: x['distance'])
        green_ids = [sorted_ambs[0]['id']]
    return green_ids

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_signal_data')
def get_signal_data():
    # For demo, we cycle through cases every 10 sec (simulate)
    current_time = int(time.time())
    cycle = current_time // 10 % 4 + 1

    if cycle == 1:
        # Case 1 - 1 ambulance from N
        ambs = [ambulances[0]]
        green = [1]
        explanation = "Case 1: Ambulance from North at 150m - Green signal to North, others red."
    elif cycle == 2:
        # Case 2 - 1 ambulance from S
        ambs = [ambulances[1]]
        green = [2]
        explanation = "Case 2: Ambulance from South at 145m - Green signal to South, others red."
    elif cycle == 3:
        # Case 3 - 2 ambulances, 1 after other based on distance
        ambs = [ambulances[0], ambulances[1]]
        # Sort by distance, green to closest only
        sorted_ambs = sorted(ambs, key=lambda x: x['distance'])
        green = [sorted_ambs[0]['id']]
        explanation = f"Case 3: Two ambulances from North and South at {sorted_ambs[0]['distance']}m and {sorted_ambs[1]['distance']}m. Green to closest ambulance."
    else:
        # Case 4 - all 4 ambulances, use safe path logic
        ambs = ambulances
        green = case4_priority(ambs)
        explanation = "Case 4: Four ambulances from all directions. Priority given to ambulances with non-conflicting paths to avoid accidents."

    # Signals for directions
    signals = {'N': 'red', 'S': 'red', 'E': 'red', 'W': 'red'}

    # Assign green signal to ambulances' from directions who got green signal
    for gid in green:
        for a in ambs:
            if a['id'] == gid:
                signals[a['from']] = 'green'

    # Return all ambulance info + signals + explanation
    return jsonify({
        'ambulances': ambs,
        'signals': signals,
        'green_ids': green,
        'explanation': explanation,
        'case': cycle
    })

if __name__ == '__main__':
    app.run(debug=True)
