import sys, subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of packages to install
packages = ["plotly", "matplotlib", "seaborn", "Pillow", "streamlit"]

# Install packages
for package in packages:
    install(package)