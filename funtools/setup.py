from setuptools import setup, find_packages

setup(
    name="funtools",
    version="0.1",
    description="A fun Python toolkit for GUI, charts, captchas, games, and more!",
    author="Alan Mbe",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "pygame",
        "pymunk",
        "Pillow"
        "imp"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
