#!/usr/bin/env bash
set -euo pipefail

# Demo login. Configure credentials in the environment before running.
: "${LOGIN_USER:?Set LOGIN_USER before running}"
: "${LOGIN_PASSWORD:?Set LOGIN_PASSWORD before running}"

read -r -p "Username: " username
read -r -s -p "Password: " password
printf '\n'

if [[ "$username" == "$LOGIN_USER" && "$password" == "$LOGIN_PASSWORD" ]]; then
	echo "Login successful."
else
	echo "Invalid username or password." >&2
	exit 1
fi
