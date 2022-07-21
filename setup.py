from setuptools import find_packages, setup

setup(
    name="m4i-data-management",
    version="1.0.14",
    author="Aurelius Enterprise",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        #"avro",
        #"confluent_kafka==1.8.2",
        "dict_hash",
        "elasticsearch==8.3.0",
        #"fastavro",
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
