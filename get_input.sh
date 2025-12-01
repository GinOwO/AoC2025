#/bin/bash

source .env
path="https://adventofcode.com/2025/day/$1/input"
curl -v --cookie "session=$session" -o "input/$1.txt" $path

cp "template.py" "$1.py"