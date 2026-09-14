import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of observations
n = 2500

# Dates from Jan 1, 2025 to Dec 31, 2025
start_date = datetime(2025, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 364)) for _ in range(n)]
times = [f"{random.randint(5, 23):02d}:{random.choice(['00', '15', '30', '45'])}" for _ in range(n)]

modes = ['Bus', 'Metro', 'Tram', 'Rail', 'Shared Cycling']
mode_probs = [0.4, 0.3, 0.15, 0.1, 0.05]
transport_modes = np.random.choice(modes, size=n, p=mode_probs)

routes = []
locations = ['North District', 'South District', 'East District', 'West District', 'City Center']
start_locs = []
end_locs = []

passenger_counts = []
delays = []
distances = []
emissions = []
satisfaction = []

for i in range(n):
    mode = transport_modes[i]
    start = random.choice(locations)
    end = random.choice([loc for loc in locations if loc != start])
    start_locs.append(start)
    end_locs.append(end)
    
    if mode == 'Bus':
        routes.append(f"B-{random.randint(10, 99)}")
        passenger_counts.append(int(np.random.normal(40, 15)))
        delays.append(max(0, int(np.random.normal(5, 10))))
        dist = round(random.uniform(2.0, 15.0), 1)
        distances.append(dist)
        emissions.append(round(dist * 0.10, 2))  # ~100g CO2 per km per vehicle
        satisfaction.append(max(1, min(5, int(np.random.normal(3.5, 1)))))
    elif mode == 'Metro':
        routes.append(f"M-{random.choice(['Red', 'Blue', 'Green', 'Yellow'])}")
        passenger_counts.append(int(np.random.normal(300, 100)))
        delays.append(max(0, int(np.random.normal(2, 5))))
        dist = round(random.uniform(5.0, 30.0), 1)
        distances.append(dist)
        emissions.append(round(dist * 0.03, 2)) # Lower emissions
        satisfaction.append(max(1, min(5, int(np.random.normal(4.0, 0.8)))))
    elif mode == 'Tram':
        routes.append(f"T-{random.randint(1, 15)}")
        passenger_counts.append(int(np.random.normal(80, 25)))
        delays.append(max(0, int(np.random.normal(3, 6))))
        dist = round(random.uniform(2.0, 10.0), 1)
        distances.append(dist)
        emissions.append(round(dist * 0.04, 2))
        satisfaction.append(max(1, min(5, int(np.random.normal(3.8, 0.9)))))
    elif mode == 'Rail':
        routes.append(f"R-{random.choice(['Express', 'Local'])}")
        passenger_counts.append(int(np.random.normal(400, 150)))
        delays.append(max(0, int(np.random.normal(8, 15))))
        dist = round(random.uniform(20.0, 80.0), 1)
        distances.append(dist)
        emissions.append(round(dist * 0.05, 2))
        satisfaction.append(max(1, min(5, int(np.random.normal(3.2, 1.2)))))
    else: # Shared Cycling
        routes.append("Cycle-Share")
        passenger_counts.append(1)
        delays.append(0)
        dist = round(random.uniform(0.5, 5.0), 1)
        distances.append(dist)
        emissions.append(0.0) # 0 emissions
        satisfaction.append(max(1, min(5, int(np.random.normal(4.5, 0.5)))))

# Clean up passenger counts (must be > 0)
passenger_counts = [max(1, p) for p in passenger_counts]

# Introduce some missing values to show cleaning in the report (approx 2%)
for i in range(int(n * 0.02)):
    idx = random.randint(0, n-1)
    satisfaction[idx] = np.nan

df = pd.DataFrame({
    'Date': [d.strftime('%Y-%m-%d') for d in dates],
    'Time': times,
    'Transport_Mode': transport_modes,
    'Route': routes,
    'Start_Location': start_locs,
    'End_Location': end_locs,
    'Distance_km': distances,
    'Passenger_Count': passenger_counts,
    'Delay_Duration_min': delays,
    'CO2_Emissions_kg': emissions,
    'Satisfaction_Score': satisfaction
})

# Sort by date and time
df = df.sort_values(by=['Date', 'Time']).reset_index(drop=True)

import os

output_dir = os.path.join(os.path.dirname(__file__), 'tableau_and_data')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'urban_mobility_dataset.csv')

df.to_csv(output_path, index=False)
print(f"Dataset generated successfully at {output_path}")
