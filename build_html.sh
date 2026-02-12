#!/bin/bash

# update
sudo apt-get update && sudo apt-get upgrade -y

# requirements
python -m pip install -r requirements.txt

# While 2.0 is not stable
python -m pip install jupyter-book --pre

# Otherwise the links will not be correctly set up for th webpage
export BASE_URL="https://marinholab.github.io/oxbr_dq_robotics_lessons"

cat myst.yml
python -m jupyter book build --html --execute
