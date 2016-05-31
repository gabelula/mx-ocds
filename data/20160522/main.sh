#!/bin/bash

echo 'IMPORT DATA INTO MONGODB'
echo '-----------'
python import.py

echo 'REVIEW WHAT CAN BE REVIEWD AUTOMATICALLY'
echo '--------------------'
python process.py

echo 'USE MONGODB COMPASS TO VISUALIZE!'

#echo 'PLOT PROCESSED DATA'
#echo '---------------------'
#python plot.py
