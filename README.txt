
# ATES - Ambulance Traffic Emergency Signal System

## Project Overview
This project dynamically manages traffic signals based on ambulance proximity, handling worst-case scenarios intelligently using simulated path prediction.

## Signal Control Logic
- Four signals at an intersection.
- Ambulances from N/E/S/W directions.
- Signal turns green if ambulance is within 250–300m.
- In multi-ambulance cases, the nearest gets priority.
- **Worst Case Handling**: If distances are equal, trajectory prediction is simulated using direction heuristics to allow two ambulances to pass without collision.

## Files
- `main.py` - Core simulation logic
- `README.txt` - Project explanation

## How to Run
1. Open terminal or command prompt.
2. Navigate to extracted folder: `cd ATES_Emergency_Traffic_Control`
3. Run the project: `python main.py`

## Technologies Used
- Python 3.10+
- Simulated trajectory using random heuristics
- Can be enhanced with real GPS + ML models

## Resume Description
**Project Title**: Ambulance Traffic Emergency System (ATES)  
**Tech**: Python, Real-time Signal Logic, Path Prediction Simulation  
**Summary**: Developed a system that simulates smart traffic signal control prioritizing ambulances. Implemented logic for handling multiple ambulances and resolving worst-case conflicts using path prediction.  

## Interview Talking Points
- Explained use of sorting and prediction logic for priority.
- Discussed handling real-time signal switching logic.
- Mention how the system reduces ambulance delay in traffic.
