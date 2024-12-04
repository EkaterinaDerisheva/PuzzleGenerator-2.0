#!/bin/bash
git clone https://github.com/EkaterinaDerisheva/PuzzleGenerator-2.0.git
cd PuzzleGenerator-2.0
git checkout develop
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r ../requirements.txt