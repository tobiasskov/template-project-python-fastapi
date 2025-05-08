import inspect

import pytest
from polyfactory.factories.pydantic_factory import ModelFactory

from xyz_api.core.calculate_price import calculate_expected_price
from xyz_api.schemas.vehicles import VehicleBaseV1


class VehicleBaseV1Factory(ModelFactory[VehicleBaseV1]): ...


@pytest.mark.parametrize(
    "test_run_id, timestamp",
    [(i, datetime.now().strftime("%Y_%m_%d__%H_%M_%S")) for i in range(20)],
)
def test_calculate_price_estimate(test_run_id: int):
    # Get the current function name
    function_name = inspect.currentframe().f_code.co_name
    file_name = Path(__file__).stem

    sim_input = VehicleBaseV1Factory.build()
    price = calculate_expected_price(sim_input)
