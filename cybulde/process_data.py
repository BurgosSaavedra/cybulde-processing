from cybulde.config_schemas.data_processing_config_schema import DataProcessingConfig
from cybulde.utils.config_utils import get_config
from cybulde.utils.data_utils import get_raw_data_with_version
from cybulde.utils.gcp_utils import access_secret_version


@get_config(config_path="../configs", config_name="data_processing_config")
def process_data(config: DataProcessingConfig) -> None:
    print(config)
    return

    version = "v1"
    data_local_save_dir = "./data/raw"
    dvc_remote_repo = "https://github.com/BurgosSaavedra/cybulde-data.git"
    dvc_data_folder = "data/raw"
    github_user_name = "BurgosSaavedra"
    github_access_token = access_secret_version("mlopsproject-413606", "cybulde-data-github-access-token")

    get_raw_data_with_version(
        version=version,
        data_local_save_dir=data_local_save_dir,
        dvc_remote_repo=dvc_remote_repo,
        dvc_data_folder=dvc_data_folder,
        github_user_name=github_user_name,
        github_access_token=github_access_token,
    )

if __name__ == "__main__":
    process_data()  # type: ignore