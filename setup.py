import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="API build from CSV",
    version="1.0.0",
    author="Benjamin Pradon",
    author_email="pradonbenjamin@gmail.com",
    description="This is how to get from a CSV file to an API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/textSolver34761/from_csv_to_API",
    project_urls={
        "Bug Tracker": "https://github.com/textSolver34761/from_csv_to_API/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Intended Audience :: Education"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
