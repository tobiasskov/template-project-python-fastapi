import os
import traceback
from datetime import datetime
from pathlib import Path
from typing import Callable

import pytest
from pydantic import BaseModel


@pytest.fixture(scope="session")
def test_session_timestamp():
    return datetime.now().strftime("%Y-%m-%d--%H-%M-%S")


def save_test_input_and_output(
    func: Callable,
    input_schema: BaseModel,
    file_name: str,
    function_name: str,
    test_run_id: int,
    timestamp: str,
):
    parent_output_folder = Path(__file__).parent.joinpath("test_results")
    run_output_folder = parent_output_folder.joinpath(
        f"[file]{file_name}[function]{function_name}[time]{timestamp}"
    )
    test_output_folder = run_output_folder.joinpath(f"[id]{test_run_id}")
    if not os.path.isdir(test_output_folder):
        os.makedirs(test_output_folder)

    # Always save the input schema:
    with open(test_output_folder.joinpath("input_schema.json"), "w") as outfile:
        outfile.write(input_schema.model_dump_json(indent=2))

    try:
        # Act: Call the function you want to test
        func_output = func(input_schema)

        with open(test_output_folder.joinpath("output.out"), "w") as outfile:
            outfile.write(f"{func_output}")

        return func_output

    except Exception as error:
        with open(test_output_folder.joinpath("error.err"), "w") as outfile:
            outfile.writelines(traceback.format_exception(error))

        with open(run_output_folder.joinpath(f"[id]{test_run_id}.err"), "w") as outfile:
            outfile.writelines(traceback.format_exception(error))

        raise Exception(error)
