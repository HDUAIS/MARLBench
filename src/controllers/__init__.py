REGISTRY = {}

from .basic_controller import BasicMAC
from .separate_controller import SeparateMAC
from .noise_controller import NoiseMAC

from .maddpg_controller import MADDPGMAC

REGISTRY["basic_mac"] = BasicMAC
REGISTRY["separate_mac"]=SeparateMAC
REGISTRY["noise_mac"] = NoiseMAC

REGISTRY["maddpg_mac"] = MADDPGMAC