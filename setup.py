from setuptools import setup

setup(
    name='UAserver_Python',          # Your package name
    version='1.1.1',                 # Must be non-empty and valid
    packages=[
        "BaldiWindows",
        "ZuhairGaming",
        "emulator",
        "python5",
        "tkinterHP"
    ],                                # Explicitly list your package folders
    install_requires=[],             # Add dependencies here if needed
    author='Umair Abdullah',         # Your name
    description='My Python Package', # Short description
    python_requires='>=3.10, <3.15', # Compatible with Python 3.13 and 3.14
    include_package_data=True,       # Include non-Python files if specified in MANIFEST.in
)
