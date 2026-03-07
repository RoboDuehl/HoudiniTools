#!/bin/bash

#system integration step 
python3 system_integration.py

#create user data package 
python3 create_package_json.py

#copy package file into Houdini
cp packages/company_vars.json /Users/andal/Library/Preferences/houdini/21.0/packages

echo "All steps done" 
