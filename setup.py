import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="pads",  # Replace with your own username
    version="0.0.1",
    author="Cambridge Yang",
    author_email="camyang@csail.mit.com",
    description="A installable package for the PADS tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thisiscam/PADS.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)