REGISTRY = {}

from .rnn_agent import RNNAgent
from .latent_ce_dis_rnn_agent import LatentCEDisRNNAgent
from .noise_rnn_agent import RNNAgent as NoiseRNNAgent

REGISTRY["rnn"] = RNNAgent
REGISTRY["latent_ce_dis_rnn"] = LatentCEDisRNNAgent
REGISTRY["noise_rnn"] = NoiseRNNAgent