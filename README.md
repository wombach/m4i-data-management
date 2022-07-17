# VOX Data Management
This library contains all core functionality for publishing data sources to, and consuming data source from, the Van Oord data management platform.

The library also houses the implementations of connectors for various data sources in Van Oord.

## Automated CI build

This repository is tied to GitHub actions. Every new accepted merge request to master/main will initiate a new release of the code. Steps to develop and trigger the CI propperly:

1. Before you start your development create a new branch from master/main
2. Write your code
3. Once you are done with code writing, update the `setup.py` with the module depenencies and increment the version number.
4. Create merge request in github to master/main, and follow the CI build in the Actions tab on the GitHub website.

Once the CI job succeeded you should be able to find your package tagged in GitHub


## Installation

Please ensure your `Python` environment is on version `3.7`. Some dependencies do not work with any later versions of `Python`.

To install `vox-data-management` and all required dependencies to your active `Python` environment, please run the following command from the project root folder:

```
pip install -e .
```

To install `vox-data-management` including development dependencies, please run the following command instead:

```
pip install -e .[dev]
```

Please make a copy of `sample_config_env` and rename the files to `config_env`.
Please set the configuration parameters and credentials for `Elastic` and `Confluent`, as well as for the connectors you want to use.

The `config_env` files should be located in the root folder of the project, or otherwise on the `PYTHON_PATH`.


How to make a `sample_config_env`:

For the script to identify which environment variables are part of the configuration, a prefix (default= ‘config_’ ), is added to the key. It is also possible to create key, values pairs that can become a more complex structure (list, dictionary).
To make the list, each item inside must be its own key, value pair.   The key of the items in the list must end with ‘__NUMBER’ to identify .
To make a dictionary nested structure, the different levels are separated by ‘__STRING’

|Environment Variable|Python Translation|
|------------:|---------:|
| config_key=value | ``key=value`` |
| | |
| config_list__0=item_1| ``list=[item_1, item_2]``|
| config_list__1=item_2| |
| | |
| config_dict__one=value_1| ``dict={one:value_1, two:value_2}``|
| config_dict__two=value_2| |

To load the config from the file for testing:
```python
from vox_data_management import load_config_from_env
load_config_from_env()
```

## Testing

This project uses `pytest` as its unit testing framework.
To run the unit tests, please install `pytest` and then execute the `pytest` command from the project root folder.

Unit tests are grouped per module.
Unit test modules are located in the same folder as their respective covered modules.
They can be recognized by the `test__` module name prefix, followed by the name of the covered module.

## Contacts

| Name              | Role                | Email                         |
| ----------------- | ------------------- | ----------------------------- |
| Andreas Wombacher | IT Architect        | andreas.wombacher@vanoord.com |
| Maarten van Veen  | IT Project Engineer | maarten.vanveen@vanoord.com   |
