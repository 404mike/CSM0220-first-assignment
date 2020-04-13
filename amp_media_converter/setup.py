import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amp-media-converter", # Replace with your own username
    version="0.0.1",
    author="Michael Jones",
    author_email="dmj12@aber.ac.uk",
    description="A package to convert images and other media",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/404mike/CSM0220-first-assignment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)