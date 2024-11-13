import os
import re
import shutil
import subprocess
import requests

GITHUB_USER = "Datura-ai"
BASE_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
WORK_DIR = "./repo_temp"

# Load keywords from process.dump
with open('process.dump', 'r') as f:
    data = f.read()

# Extract words (potential keywords) from the data
keywords = re.findall(r'[\w\.-]+', data)

# List to store results for individual files
file_hits = []

# Delete the directory if it already exists
if os.path.exists(WORK_DIR):
    shutil.rmtree(WORK_DIR)

# Ensure the working directory exists
os.makedirs(WORK_DIR, exist_ok=True)

# Get repositories
repos_response = requests.get(BASE_URL)
if repos_response.status_code == 200:
    repos = repos_response.json()
    for repo in repos:
        repo_name = repo['name']
        repo_url = repo['clone_url']
        print(f"Cloning repository: {repo_name}")
        
        # Clone the repository
        repo_path = os.path.join(WORK_DIR, repo_name)
        subprocess.run(["git", "clone", repo_url, repo_path], check=True)

        # Walk through all .py files in the cloned repository
        for root, _, files in os.walk(repo_path):
            for file in files:
                # Process only .py files
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        # Read file content and count hits for each keyword
                        print(f"Reading file: {file_path}")
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            file_content = f.read()
                            hits_in_file = sum(file_content.count(keyword) for keyword in keywords)
                            
                            # Only store if there are any hits
                            if hits_in_file > 0:
                                file_hits.append({
                                    'repo': repo_name,
                                    'file_path': file_path,
                                    'hits': hits_in_file,
                                    'download_url': file_path.replace(repo_path, f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/main")
                                })
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

        # Remove the repository folder after processing
        shutil.rmtree(repo_path)
        print(f"Removed repository: {repo_name}")

else:
    print("Failed to retrieve repositories.")

# Sort files by hits in descending order and keep only the top 20
top_files = sorted(file_hits, key=lambda x: x['hits'], reverse=True)[:20]

# Display top 20 results
print("\nTop 20 Files with Most Hits:")
for idx, file_info in enumerate(top_files, 1):
    print(f"{idx}. Repo: {file_info['repo']} | File: {file_info['file_path']} | Hits: {file_info['hits']}")

# Download the file with the most hits and save it as found.py
if top_files:
    top_file = top_files[0]
    download_url = top_file['download_url']
    response = requests.get(download_url)
    if response.status_code == 200:
        with open("found.py", "w") as f:
            f.write(response.text)
        print(f"\nDownloaded the top file to 'found.py' from {download_url}")
    else:
        print("Failed to download the top file.")
else:
    print("No files with hits found.")
