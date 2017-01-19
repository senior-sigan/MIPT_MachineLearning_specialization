#!/bin/bash

cat data/checkins.dat | python3 dat_to_csv.py | gzip > data/checkins.csv.gz