from setuptools import find_packages, setup

setup(
    name="nxtgen-vox-data-management",
    version="1.0.14",
    author="Van Oord Data Management",
    packages=find_packages(),
    python_requires="~=3.7",
    install_requires=[
        "avro",
        "confluent_kafka",
        "dict_hash",
        "elasticsearch==8.1.0",
        "fastavro",
        "jsonschema",
        "pandas",
        "pytest",
        "requests",
        "typing_extensions",
        "deepdiff",
        "python-dotenv",
    ],
    extras_require={
        "dev": [
            "mock",
            "pytest",
            "pytest-cov"
        ]
    }
)
