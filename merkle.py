import pprint
import requests
from web3 import Web3


def getLogFillEvents(blockNumber):
    blockNumberHex = Web3.toHex(blockNumber)
    url = "https://api.infura.io/v1/jsonrpc/mainnet/eth_getLogs"
    querystring = {
        "params": "[{\"address\": \"0x12459c951127e0c374ff9105dda097662a027093\", \"fromBlock\": \"%s\"}]" \
                  % blockNumberHex
    }
    print(querystring)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "67ac5617-3087-f100-7100-7053a92c284c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()



if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(getLogFillEvents(6138105))


