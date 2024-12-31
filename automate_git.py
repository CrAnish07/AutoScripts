import os
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = "D:\AutoCommits"  
FILE_NAME = "example.txt"  
COMMIT_MESSAGE = "Automated commit"  
BRANCH_NAME = "commit_changes" 

# Creates or updates the text file with a timestamp.
def create_or_update_file():
    file_path = os.path.join(REPO_PATH, FILE_NAME)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"File updated at {timestamp}\n"
    
    with open(file_path, "a") as file:
        file.write(content)
    print(f"Updated {FILE_NAME} with timestamp: {timestamp}")

# Runs a git command in the repository directory.
def run_git_command(command):
    try:
        result = subprocess.run(command, cwd=REPO_PATH, text=True, check=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(e.stderr)
        raise

# Automates Git commit and push.
def automate_git_commit_and_push():
    # Stage the changes
    run_git_command(["git", "add", FILE_NAME])
    print(f"Staged changes for {FILE_NAME}")
    
    # Commit the changes
    run_git_command(["git", "commit", "-m", COMMIT_MESSAGE])
    print("Committed changes")
    
    # Push to the remote repository
    run_git_command(["git", "push", "origin", BRANCH_NAME])
    print("Pushed changes to the remote repository")

if __name__ == "__main__":
    create_or_update_file()
    automate_git_commit_and_push()
