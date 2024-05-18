#!/bin/bash

# Variables
PASSWORD="S2pedutech@1234"            # Your SSH password
USER="root"                          # The default user for Amazon Linux
HOST="109.106.255.69"              # The public IP or DNS of your EC2 instance

# The list of commands to run
COMMANDS="./bashFile.sh"

# SSH into the EC2 instance and run the list of commands
sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no "$USER@$HOST" "$COMMANDS"

