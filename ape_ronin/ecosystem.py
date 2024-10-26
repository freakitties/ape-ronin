from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
#    create_network_config,
)
from ape_ethereum.ecosystem import NetworkConfig, BaseEthereumConfig
from typing import Optional, Type, cast
from ape.utils import DEFAULT_LIVE_NETWORK_BASE_FEE_MULTIPLIER
from pathlib import Path

NETWORKS = {
    # chain_id, network_id
    "mainnet": (2020, 2020),
    "saigon": (2021, 2021),
}


class RoninNetworkConfig(NetworkConfig):
    default_provider: Optional[str] = "ronin-node"
    executable: Optional[str] = None
    ipc_path: Optional[Path] = None
    data_dir: Optional[Path] = None    


def create_network_config(
    required_confirmations: int = 2,
    base_fee_multiplier: float = DEFAULT_LIVE_NETWORK_BASE_FEE_MULTIPLIER,
    cls: Type = RoninNetworkConfig,
    **kwargs,
) -> RoninNetworkConfig:
    return cls(
        base_fee_multiplier=base_fee_multiplier,
        required_confirmations=required_confirmations,
        **kwargs,
    )
            
class BaseRoninConfig(BaseEthereumConfig):
    default_network: Optional[str] = "mainnet"            

class RoninConfig(BaseRoninConfig):
    mainnet: NetworkConfig = create_network_config(block_time=3)
    saigon: NetworkConfig = create_network_config(block_time=3)

class Ronin(Ethereum):
    @property
    def config(self) -> RoninConfig:  # type: ignore
        # Load from config file
        return cast(RoninConfig, self.config_manager.get_config(self.name))
