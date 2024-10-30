from setuptools import setup, find_packages

setup(
    name="easy-insight",
    version="0.1.0",
    description="A simple library for easy exploratory data analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Durgesh Rathod",
    author_email="durgeshrathod.777@gmail.com",
    url="https://github.com/DurgeshRathod/easy-insight.git",  # Update this to your GitHub repo
    license="MIT",
    packages=find_packages(),  # This includes the eda_tools submodule
    
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "matplotlib>=3.2.0",
        # Add any other dependencies here
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)

