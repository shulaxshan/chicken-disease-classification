#### If using variables/ file path only one time,we can write those into the constant file (it won't change)

from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")