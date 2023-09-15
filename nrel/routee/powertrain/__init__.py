import logging
from pathlib import Path

from .core.features import DataColumn, FeatureSet, Constraints, TargetSet
from .core.model import Model
from .core.model_config import ModelConfig
from .core.powertrain_type import PowertrainType
from .io.api import read_model
from .io.load import list_available_models, load_pretrained_model

__version__ = "1.0.0"

log = logging.getLogger()
log.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)


def package_root() -> Path:
    return Path(__file__).parent
