#!/bin/bash

# To use this script in a new setup, make sure to grant executable permissions as needed

# Variables
PROJECT_FOLDER_NAME="AlmostFunny"
RUNNING_USER="vscode"

# Create project folder in logs and add vscode user access for logging
cd /var/log && mkdir "${PROJECT_FOLDER_NAME}" && chown "${RUNNING_USER}" "/var/log/${PROJECT_FOLDER_NAME}"

# Add vscode ability to install packages
usermod -a -G vscode "${RUNNING_USER}"

# Adjust permissions
chgrp -R vscode /usr/local
chmod -R g+rwx /usr/local