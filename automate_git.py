import os
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = "/path/to/your/local/repo"  # Replace with the path to your Git repo
FILE_NAME = "example.txt"  # File to be created or updated
COMMIT_MESSAGE = "Automated commit"  # Commit message
BRANCH_NAME = "main"  # Change if using a different branch

def create_or_update_file():
    """Creates or updates the text file with a timestamp."""
    file_path = os.path.join(REPO_PATH, FILE_NAME)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"File updated at {timestamp}\n"
    
    with open(file_path, "a") as file:
        file.write(content)
    print(f"Updated {FILE_NAME} with timestamp: {timestamp}")

def run_git_command(command):
    """Runs a git command in the repository directory."""
    try:
        result = subprocess.run(
            command, cwd=REPO_PATH, text=True, check=True, capture_output=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(e.stderr)
        raise

def automate_git_commit_and_push():
    """Automates Git commit and push."""
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
