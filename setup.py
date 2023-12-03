import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="pyTSP",
        version="0.0.3",
        author="Behnam Lal",
        author_email="dev@behnamlal.xyz",
        description="A simple and module TSP solver",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/CheesyChocolate/TSP",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Affero General Public License v3",
            "Operating System :: OS Independent"
            ],
        python_requires='>=3.6',
        install_requires=[
            'numpy',
            'matplotlib',
                     ],
        )
