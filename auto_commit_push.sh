#!/bin/bash

# Navigate to your Git repository (replace with your actual path)
cd ~/repos/LearnWithMe || exit

# Add all unstaged changes
git add .

# Commit with a default message including a timestamp
commit_message="Auto commit on $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_message"

git fetch

git pull
# Push changes to the current branch
git push 

echo "Changes committed and pushed successfully."

