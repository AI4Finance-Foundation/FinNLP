from setuptools import setup, find_packages

# Read requirements.txt, ignore comments
try:
    with open("requirements.txt", "r") as f:
        REQUIRES = [line.split('#', 1)[0].strip() for line in f if line.strip()]
except:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name="FinNLP",
    version="0.0.1",
    include_package_data=True,
    author="AI4Finance Foundation",
    author_email="contact@ai4finance.org",
    url="https://github.com/AI4Finance-Foundation/FinNLP",
    license="MIT",
    packages=find_packages(),
    install_requires=REQUIRES,
    description="FinNLP",
    long_description="""FinNLP""",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="Financial Large Language Models",
    platforms=["any"],
    python_requires=">=3.6",
)
