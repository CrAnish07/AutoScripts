import os
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = r"D:\AutoCommits"  
FILE_NAME = "example.txt"  
COMMIT_MESSAGE = "Automated commit"  
BRANCH_NAME = "main" 
REMOTE_NAME   = "origin"

# Runs a git command in the repository directory.
def run_git_command(command):
    try:
        result = subprocess.run(command, cwd=REPO_PATH, text=True, check=True, capture_output=True)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}:\n{e.stderr.strip()}")
        raise

# Creates or updates the text file with a timestamp.
def create_or_update_file():
    file_path = os.path.join(REPO_PATH, FILE_NAME)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"File updated at {timestamp}\n"
    
    with open(file_path, "a") as file:
        file.write(content)
    print(f"Updated {FILE_NAME} with timestamp: {timestamp}")

# Automates Git commit and push.
def automate_git_commit_and_push():
    # Stage the changes
    # 1) Fetch & rebase remote changes to avoid non-fast-forward
    print("Fetching & rebasing remote changes…")
    run_git_command(["git", "fetch", REMOTE_NAME, BRANCH_NAME])
    run_git_command(["git", "rebase", f"{REMOTE_NAME}/{BRANCH_NAME}"])

    # 2) Now update the file
    create_or_update_file()
    
    # 3) Stage, commit
    run_git_command(["git", "add", FILE_NAME])
    run_git_command(["git", "commit", "-m", COMMIT_MESSAGE])
    print("Committed changes")
    
    # Push to the remote repository
    run_git_command(["git", "push", REMOTE_NAME, BRANCH_NAME])
    print("Pushed changes to the remote repository")

if __name__ == "__main__":
    automate_git_commit_and_push()
