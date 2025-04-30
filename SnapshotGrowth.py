import pandas as pd

# Load the data
snapshot_df = pd.read_csv('C:/Users/tiffy\Downloads/ABC District/ABCDistrictsnapshotdata.csv')
snapshot_overall = snapshot_df[snapshot_df['Strand'] == 'Overall'].copy()

# Convert 'Level' to numeric format
snapshot_overall['Level'] = pd.to_numeric(snapshot_overall['Level'], errors='coerce')

# Pivot the table
snapshot_pivot = snapshot_overall.pivot_table(
    index=['Student ID', 'Grade', 'School', 'Subject', 'Strand', 'Tier'],
    columns='Snapshot',
    values='Level'
).reset_index()

# Rename columns
snapshot_pivot.columns.name = None
snapshot_pivot = snapshot_pivot.rename(columns={
    'Snapshot 1': 'Snapshot1_Level',
    'Snapshot 2': 'Snapshot2_Level'
})

# Calculate Growth
snapshot_pivot['Growth'] = snapshot_pivot['Snapshot2_Level'] - snapshot_pivot['Snapshot1_Level']

# Export file to csv
snapshot_pivot.to_csv('snapshot_pivot.csv', index=False)
print("DataFrame exported successfully to 'snapshot_pivot.csv'.")
