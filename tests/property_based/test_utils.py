from datetime import datetime
from pathlib import Path
from typing import Callable


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
        f"{file_name}___{function_name}___{timestamp}"
    )
    test_output_folder = run_output_folder.joinpath(f"test_run_id_{test_run_id}")
    if not os.path.isdir(test_output_folder):
        os.makedirs(test_output_folder)

    # Always save the input schema:
    with open(pydantic_model_save_name, "w") as outfile:
        outfile.write(input_schema.model_dump_json())

    try:
        # Act: Call the function you want to test
        func_output = func(input_schema)
        return func_output

    except Exception as error:
        now = datetime.now()
        current_time = now.strftime("%Y_%m_%d__%H_%M_%S")

        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        # Save input pydantic model as json:
        pydantic_model_save_name = output_folder.joinpath(
            f"{current_time}__{filepath.stem}__{func.__name__}__id_{test_run_id}__input.pkl"
        )

        # Save error message:
        error_message_save_name = output_folder.joinpath(
            f"{current_time}__{filepath.stem}__{func.__name__}__id_{test_run_id}__error.err"
        )
        with open(error_message_save_name, "w") as outfile:
            outfile.writelines(traceback.format_exception(error))

        raise Exception(error)
