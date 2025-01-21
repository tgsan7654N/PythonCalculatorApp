from setuptools import setup, find_packages

setup(
    name="PythonCalculatorApp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt5"
    ],
    entry_points={
        "console_scripts": [
            "calculator-app=calculator_app.main:main"
        ]
    },
    author="Thomas Sanchez",
    description="A simple PyQt5-based calculator app",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tgsan7654N/calculator_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)