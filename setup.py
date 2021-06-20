import setuptools
from src.example_package import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testingCICD",
    version=__version__,
    author="digitalTevel",
    author_email="digitalTevel@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Elon-Abulafia/testingCICD",
    project_urls={
        "Bug Tracker": "https://github.com/Elon-Abulafia/testingCICD/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src/example_package"},
    packages=["src/example_package", "tests"],
    python_requires=">=3.6",
)
