from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config
from cybulde.utils.gcp_utils import access_secret_version


@get_config(config_path="../configs", config_name="config")
def process_data(config: Config) -> None:
    print(config)

    my_dummy_secret = access_secret_version("585353665029", "dummy-secret")
    print(f"{my_dummy_secret}")

if __name__ == "__main__":
    process_data()  # type: ignore