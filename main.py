import sys
import pandas as pd

def load_usernames(file_path):
    """
    Loads a list of usernames from a text file.
    Each line is expected to contain one username.
    """
    usernames = []
    with open(file_path, 'r') as file:
        for line in file:
            usernames.append(line.strip())
    return usernames

def load_team_scores(excel_path):
    """
    Loads team scores from an Excel file.
    Returns a dictionary mapping team names (in lowercase) to their score.
    """
    df = pd.read_excel(excel_path)
    team_scores = {}

    for _, row in df.iterrows():
        team_name = str(row["Team"]).strip().lower()
        score = int(row["Score"])
        team_scores[team_name] = score

    return team_scores

def match_usernames_to_scores(usernames, team_scores):
    """
    For each username, prints its corresponding score based on partial match with team names.
    If no match is found, prints 0 as the score.
    """
    for username in usernames:
        matched = False
        for team_name in team_scores:
            if username.lower() in team_name:
                print(username, team_scores[team_name], sep="\t")
                matched = True
                break
        if not matched:
            print(username, 0, sep="\t")

def main(excel_path, usernames_path):
    usernames = load_usernames(usernames_path)
    team_scores = load_team_scores(excel_path)
    match_usernames_to_scores(usernames, team_scores)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <excel_file> <usernames_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])

