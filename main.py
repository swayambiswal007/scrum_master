import json
from utils import analyze_standup

# Step 1: Read team input
with open("team_input.json", "r") as file:
    team_data = json.load(file)

# Step 2: Analyze
summary = analyze_standup(team_data)

# Step 3: Display
print("\n✅ Team Summary:")
for task in summary["tasks"]:
    print("-", task)

print("\n🚧 Blockers:")
for blocker in summary["blockers"]:
    print("-", blocker)
