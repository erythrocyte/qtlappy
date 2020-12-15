import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qtlappy",  # Replace with your own username
    version="0.0.1",
    author="erythrocyte",
    author_email="erythrocyte.rbc@gmail.com",
    description="2D reservoir simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.org/erythrocyte/qtlappy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['wheel'],
    python_requires='>=3.6',
)
