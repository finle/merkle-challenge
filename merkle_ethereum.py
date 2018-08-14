import eth_utils
import pprint
import requests
import sys

from ethereum import abi


def get_raw_logfill_events(block_number):
    """
    Retrieve list of raw LogFill events given a block number.

    @param block_number: integer of Ethereum block number.
    @return: list of raw LogFill events.
    """
    block_number_hex = eth_utils.to_hex(block_number)
    url = "https://api.infura.io/v1/jsonrpc/mainnet/eth_getLogs"
    query_string = {
        "params": "[{\"address\": \"0x12459c951127e0c374ff9105dda097662a027093\", \"fromBlock\": \"%s\", \"toBlock\": \"%s\"}]" \
                  % (block_number_hex, block_number_hex)
    }
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=query_string)
    logfill_events = [event for event in response.json()["result"] \
                      if event["topics"][0] == "0x0d0b9391970d9a25552f37d436d2aae2925e2bfe1b2a923754bada030c498cb3"]
    return logfill_events


def decode_raw_events(events):
    """
    Decode list of raw events into something more human readable.

    @param events: list of raw events.
    @return: list of decoded events.
    """
    true, false = True, False
    contract_0x_abi = [{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"isRoundingError","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"filled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"cancelled","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"fillOrdersUpTo","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"cancelTakerTokenAmount","type":"uint256"}],"name":"cancelOrder","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ZRX_TOKEN_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrKillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrKillOrder","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderHash","type":"bytes32"}],"name":"getUnavailableTakerTokenAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"signer","type":"address"},{"name":"hash","type":"bytes32"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"isValidSignature","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"numerator","type":"uint256"},{"name":"denominator","type":"uint256"},{"name":"target","type":"uint256"}],"name":"getPartialAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"TOKEN_TRANSFER_PROXY_CONTRACT","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"fillTakerTokenAmounts","type":"uint256[]"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8[]"},{"name":"r","type":"bytes32[]"},{"name":"s","type":"bytes32[]"}],"name":"batchFillOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5][]"},{"name":"orderValues","type":"uint256[6][]"},{"name":"cancelTakerTokenAmounts","type":"uint256[]"}],"name":"batchCancelOrders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"},{"name":"fillTakerTokenAmount","type":"uint256"},{"name":"shouldThrowOnInsufficientBalanceOrAllowance","type":"bool"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"fillOrder","outputs":[{"name":"filledTakerTokenAmount","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"orderAddresses","type":"address[5]"},{"name":"orderValues","type":"uint256[6]"}],"name":"getOrderHash","outputs":[{"name":"","type":"bytes32"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"EXTERNAL_QUERY_GAS_LIMIT","outputs":[{"name":"","type":"uint16"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"VERSION","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"inputs":[{"name":"_zrxToken","type":"address"},{"name":"_tokenTransferProxy","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"taker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"filledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"filledTakerTokenAmount","type":"uint256"},{"indexed":false,"name":"paidMakerFee","type":"uint256"},{"indexed":false,"name":"paidTakerFee","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogFill","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"maker","type":"address"},{"indexed":true,"name":"feeRecipient","type":"address"},{"indexed":false,"name":"makerToken","type":"address"},{"indexed":false,"name":"takerToken","type":"address"},{"indexed":false,"name":"cancelledMakerTokenAmount","type":"uint256"},{"indexed":false,"name":"cancelledTakerTokenAmount","type":"uint256"},{"indexed":true,"name":"tokens","type":"bytes32"},{"indexed":false,"name":"orderHash","type":"bytes32"}],"name":"LogCancel","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"errorId","type":"uint8"},{"indexed":true,"name":"orderHash","type":"bytes32"}],"name":"LogError","type":"event"}]
    translated_contract = abi.ContractTranslator(contract_0x_abi)
    decoded_events = []
    for event in events:
        # Must convert topics from hexadecimal to int for the API to work.
        topics = list(map(lambda topic: int(topic, 0), event["topics"]))
        # Must convert raw data into decoded hex.
        decoded_hex_data = eth_utils.decode_hex(event["data"])
        decoded_events.append(translated_contract.decode_event(topics, decoded_hex_data))
    return decoded_events


def get_logfill_events(block_number):
    """
    Wrapper function to get LogFill events.

    @param block_number: integer of Ethereum block number to retrieve LogFill events from.
    @return: list of decoded LogFill events.
    """
    raw_events = get_raw_logfill_events(block_number)
    return decode_raw_events(raw_events)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Please provide a single argument for block number.')
    try:
        block_number = int(sys.argv[1])
    except:
        sys.exit('Block number needs to be an int.')
    pp = pprint.PrettyPrinter(indent=4)
    decoded_events = get_logfill_events(block_number)
    for event in decoded_events:
        pp.pprint(event)
