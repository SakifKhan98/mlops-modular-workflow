from setuptools import setup, find_packages


# Read the requirements.txt file and add the dependencies to the install_requires list
with open("requirements.txt") as fh:
    required = fh.read().splitlines()

# Readme.md file will be used as the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlops_modular_workflow",
    version="0.1.0",
    author="Sakif Khan",
    author_email="sakifkhan98@gmail.com",
    description="A modular workflow for MLOps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SakifKhan98/mlops-modular-workflow",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=required,
    extras_require={
        "dev": [
            "pytest>=7.1.1",
            "pytest-cov>=2.12.1",
            "flake8>=3.9.0",
            "black>=22.3.0",
            "isort>=5.10.1",
            "mypy>=0.942",
        ],
    },
)
