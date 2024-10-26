from ape import plugins
from ape.api.networks import LOCAL_NETWORK_NAME, ForkedNetworkAPI, NetworkAPI, create_network_type
from .ecosystem import NETWORKS, Ronin, RoninConfig

#ecosystem: Ronin
#network: mainnet
#provider: RPC

@plugins.register(plugins.Config)
def config_class():
    return RoninConfig

@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Ronin


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "ronin", network_name, create_network_type(*network_params)
        #yield "ronin", f"{network_name}-fork", ForkedNetworkAPI
    # NOTE: This works for local providers, as they get chain_id from themselves
    #yield "ronin", LOCAL_NETWORK_NAME, NetworkAPI

