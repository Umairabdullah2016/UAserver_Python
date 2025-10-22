from setuptools import setup, find_packages

setup(
    name='UAserver_Python',          # Your package name
    version='0.1.0',                 # Version number
    packages=find_packages(),        # Automatically find all existing packages
    install_requires=[],             # Add dependencies here if needed
    author='Umair Abdullah',         # Your name
    description='My Python Package', # Short description
    python_requires='>=3.13, <3.15', # Compatible with Python 3.13 and 3.14
    include_package_data=True,       # Include non-Python files if you have any
)
