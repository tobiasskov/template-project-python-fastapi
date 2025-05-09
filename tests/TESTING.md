# Testing

Currently, there are two types of testing:

**Example-Based Testing.** This is the traditional way most developers write tests:

- You provide specific input values and expect specific output values
- Tests are deterministic and easy to understand
- You manually choose test cases based on your understanding of the system

**Property-Based Testing.** This approach focuses on testing properties that should always hold true:

- You define properties that your function should satisfy
- The testing framework generates many random inputs to verify these properties
- Better at finding edge cases you might not think of
- Tests are more abstract and focus on behavioral rules

**Tools used:**

- **[pytest](https://docs.pytest.org/en/stable/)** as the main test package, defining the structure and how to parametrize test functions.
- **[polyfactory](https://polyfactory.litestar.dev/latest/)** to generate an instances of a json-schemas/pydantic-model with random values.
  values.
- **[pytest-xdist](https://pytest-xdist.readthedocs.io/en/stable/)** for running tests in parallel.

## Example-Based Testing

Example-Based testing is done to conduct some fast to run and easy to understand tests. The intended use is to test the that changes in the codebase does not break the functionality.

## Property-Based Testing

Property-Based testing is done to ensure the integrity of the thermodynamic simulations. I.e. ensuring that all the allowed input values as specified in the
json-schemas/pydantic models can run in the simulations without giving any errors.

It is not the focus of testing that the simulations should give realistic output, which is handled through validation.

The following suite of tools (python packages) are used to conduct the testing:

### Parameterize test generation

Pytest can be used for parameterizing a test function, i.e. running the same function multiple times.
This can be accomplished using for following decorator:

```python
import pytest

@pytest.mark.parametrize("test_run_id", range(20))
def test_calculate_price_estimate(test_run_id: int):
    pass
```

### Generate json-schemas/pydantic-model with random values

Given a json-schemas/pydantic-model, a random version (which complies with the validators) can be generated
using the `polyfactory` `ModelFactory` class:

```python
import pytest
from polyfactory.factories.pydantic_factory import ModelFactory
from xyz_api.schemas.vehicles import VehicleBaseV1
from xyz_api.core.calculate_price import calculate_expected_price


class VehicleBaseV1Factory(ModelFactory[VehicleBaseV1]):
    ...

@pytest.mark.parametrize("test_run_id", range(20))
def test_calculate_price_estimate(test_run_id: int):
    sim_input = VehicleBaseV1Factory.build()
    price = calculate_expected_price(sim_input)

```

By combining parametrization with random generation in this way, the same test function will be run, X amount of times
(in this example 20) with different random values each time.

### Testing for a subset of a parameter:

If a single parameter has a very high influence on the simulation runtime and it is deemed that it is not necessary
to test on the entire range of possible values (should be used very carefully), then it is possible to specify a
subset of that parameter. This can be accomplished by manually overriding the parameter in test function:

```python
@pytest.mark.parametrize("test_run_id", range(20))
def test_calculate_price_estimate(test_run_id: int):
    sim_input = VehicleBaseV1Factory.build()
    sim_input.model = "Mustang"
    price = calculate_expected_price(sim_input)
```

## Running tests in parallel

Using `pytest-xdist` it is possible to speed up running tests, by running them in parallel:

1. Letting pytest autodetect the number of CPUs on the machine:

```shell
pytest -n auto -v
```

2. Manually specify the number of CPUs:

```shell
pytest -n 16 -v
```

NB: The `bps/output` folder needs to be deleted between each testing run to avoid issues.

## Running only sub-folder or file in test-suite:

If you wish to only run a sub-folder of the test-suite this can be accomplished by (from the project root):

```shell
python -m pytest -v .\tests\example_based
```

Or running in parallel as:

```shell
python -m pytest -n auto -v .\tests\property_based
```

Based on [stackoverflow](https://stackoverflow.com/questions/42996270/change-pytest-rootdir).

It is only possible to run only a single file, e.g:

```shell
python -m pytest -n auto -v .\tests\property_based\test_calculate_price.py
```
