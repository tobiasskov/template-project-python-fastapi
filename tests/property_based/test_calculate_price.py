import inspect
from pathlib import Path

import pytest
from polyfactory.factories.pydantic_factory import ModelFactory

from xyz_api.core.calculate_price import calculate_expected_price
from xyz_api.schemas.vehicles import VehicleBaseV1

from .test_utils import save_test_input_and_output
from .test_utils import test_session_timestamp as test_session_timestamp


class VehicleBaseV1Factory(ModelFactory[VehicleBaseV1]): ...


@pytest.mark.parametrize("test_run_id", range(200))
def test_calculate_price_estimate(test_run_id: int, test_session_timestamp: str):
    save_test_input_and_output(
        func=calculate_expected_price,
        input_schema=VehicleBaseV1Factory.build(),
        file_name=Path(__file__).stem,
        function_name=inspect.currentframe().f_code.co_name,
        test_run_id=test_run_id,
        timestamp=test_session_timestamp,
    )
