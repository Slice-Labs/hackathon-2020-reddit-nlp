#!/bin/bash

# Create a virtual environment in the current directory
python3 -m venv venv

# Activate the virtual environment
if [ -f ./venv/bin/activate ]; then
    source ./venv/bin/activate
else
    source ./venv/Scripts/activate
fi

# Upgrade pip and install the requirements
pip3 install --upgrade pip

# install requirements.txt if present
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt
fi

# Install ipykernel to be able to set up the kernels we need
pip3 install ipykernel

# We will try to install Jupyter Notebook and Jupyterlab, too. (and any dependencies)
pip3 install jupyter notebook jupyterlab

# Install a Jupyter kernel named to correspond with the current directory name
# Note: if there is a name conflict, this kernel will overwrite the existing one
python3 -m ipykernel install --user --name=venv_reddit

echo "🆗 Success! Your virtual environment has been set up, and a Jupyter Kernel has been created."
echo "Keep calm and 🐍 on."
