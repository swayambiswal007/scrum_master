def analyze_standup(team_data):
    summary = {"tasks": [], "blockers": []}

    for member in team_data["team"]:
        name = member["name"]
        yesterday = member["yesterday"]
        today = member["today"]
        blocker = member["blockers"]

        summary["tasks"].append(f"{name} did: {yesterday}. Plans: {today}")
        
        if blocker.strip() != "":
            summary["blockers"].append(f"{name} is blocked by: {blocker}")
    
    return summary
