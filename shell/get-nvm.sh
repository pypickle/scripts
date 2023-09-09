#!/bin/bash

# Check the user's current shell
user_shell=$(basename "$SHELL")

# Install curl if not already installed
if ! command -v curl &> /dev/null; then
  sudo apt install curl -y
fi

# Install NVM
curl -o- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash

# Source the appropriate configuration file based on the user's shell
if [ "$user_shell" = "bash" ]; then
  source ~/.bashrc
elif [ "$user_shell" = "zsh" ]; then
  source ~/.zshrc
else
  echo "Unsupported shell: $user_shell"
  exit 1
fi

# Install the latest LTS version of Node.js
nvm install --lts

# Set the default Node.js version
nvm alias default node

echo "Node.js and NVM setup completed."
