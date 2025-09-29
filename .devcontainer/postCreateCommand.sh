#!/bin/bash

# Python configuration

# Python utilities list
declare -a python_utilities=(
	"pre-commit"
	"pytest"
	"ruff"
	"uv"
	)

# Install Python utilities
for utility in "${python_utilities[@]}"
do
	pipx install "$utility"
done

# Node configuration

# Node utilities list
declare -a node_utilities=(
	"create-vue"
	# "typescript"
	# "ts-node"
	# "bun"
	# "tsx"
	# "vite"
	)

# Install Node utilities
for utility in "${node_utilities[@]}"
do
	npm install -g "$utility"
done




# Add common shell commands
echo 'alias gitback="git reset --soft HEAD~1"' >> ~/.zshrc
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc