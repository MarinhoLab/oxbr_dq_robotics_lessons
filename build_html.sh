#!/bin/bash

# update
sudo apt-get update && sudo apt-get upgrade -y

# While 2.0 is not stable
python -m pip install jupyter-book --pre

# Otherwise the links will not be correctly set up for th webpage
export BASE_URL="https://marinholab.github.io/oxbr_dq_robotics_lessons"

# Run once without the devel
cat myst.yml
python -m jupyter book build --html --execute
