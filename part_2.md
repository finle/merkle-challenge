# Part 2

I am most likely sure we cannot use the data gathered in Part 1 to front-run. Reasoning behind this is that the the LogFill events retrieved in Part 1 are emitted from already mined transactions therefore already committed. If these transactions have already been committed and have already been filled, price has already been influenced and I will be too late to perform some kind of action to maximize my profits.

If someone were to front-run, they would have a better chance by monitoring the mempool (pending transaction pool) and looking for some kind of huge transaction on X token. From here the front-runner could set a higher gas price than the gas price of the huge pending transaction so miners would prioritize the front-runner's transaction causing the huge pending transaction to fail or mined on a subsequent block.

Another scenario is where a front-runner is a miner. The front-runner miner can then ignore gas prices and place their front-running transaction into a block at whatever sequential order. 

There are several solutions to front-running, but in my opinion they aren't that great or scale well to where we want it to be.

## Solution 1) P2P trades

The 0x protocol allows for two parties to trade between each other without any risk of some third party or outsider fulfilling the open order. Simply fill in the taker key with the address of the taker and anyone else attempting to fulfill the order will have their transaction canceled because of one of the features of the 0x smart contract.

### Advantages:
-No risk of traders/miners front-running

### Disadvantages:
-Parties must be in negotiation stages for the trade
-Parties cannot liquidate on demand and forget the orders
-User experience in doing this order generation is crap and different from filling an order

## Solution 2) Trade executor middleman smart contract

Use a trade executor middleman smart contract cryptographically sign transactions before establishing the settlement on the Ethereum blockchain. 

### How it works is:
-Maker will establish their order for one ERC20 token for another ERC20 token (most of the time people just trade one token for ETH anyways) with an expiration date. Maker also provides a fee to the relayer which is paid out on chain settlement.
-Relayer gets the maker order, verifies funds of the maker, and then if everything goes well the order is added to the relayer's order book.
-Takers can fill a maker's order. These taker orders forward information to the trusted trade executor smart contract in which the trade executor will approve the transaction by cryptographically signing the trade.
-Trade executor creates an Ethereum transaction that includes the trade executor's cryptographic signature. THis is then publicly published on the Ethereum blockchain.

### Advantages:
-Reduces front-running from traders and miners
-Makers can cancel orders without creating an on-chain transaction by sending some kind of cancel call to the trade executor smart contract if functionality is provided.
-Trusted smart contract trade executor can blacklist addresses that attempt to front-run or known to front-run.
-User experience for a maker is quite fast when adding in an order since this is done off-chain.

### Disadvantages:
-There is centralization involved at the trade executor smart contract level. If this smart contract isn't audited or contains bugs, the whole system can be compromised.
-This trusted trade executor may abuse its power and favor front-running or certain traders.
-User experience 
-Taker pays more gas fees