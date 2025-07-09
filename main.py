import sys
import pandas as pd

def get_users(path):
    users = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            users.append(line)
    return users

def main(excel_path, mapping_path):
    df_csv = pd.read_excel(excel_path)
    users = get_users(mapping_path)

    users_problems = {}

    for i, row in df_csv.iterrows():
        users_problems[str(row["Team"]).lower()] = int(row["Score"])
    
    for user in users:
        flag = False
        for full_user in users_problems:
            if user.lower() not in full_user.lower():
                continue
            
            print(user,users_problems[full_user],sep="\t")
            flag = True
            break
        if not flag:
            print(user,0,sep="\t")

if __name__ == "__main__":
    main(*sys.argv[1:])
