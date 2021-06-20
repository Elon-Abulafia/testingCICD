import setuptools

version = {}
with open("...example_package/version.py") as fp:
    exec(fp.read(), version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testingCICD",
    version=version['__version__'],
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
    package_dir={"": "example_package"},
    packages=setuptools.find_packages(where="example_package"),
    python_requires=">=3.6",
)
