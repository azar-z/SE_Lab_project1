#!/bin/bash

git fetch --tags
git checkout v1.0.0

python app.py
