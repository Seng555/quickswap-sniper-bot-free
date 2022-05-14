
walletAddress = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"                     #Your Wall address From trustwallet or MetaMask or another wallet.
private_key = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270" #Wallet private_key

spend = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"  # WMATIC OR BUSD OR USDT OR OTHER (Default MATIC) contract for buy the token

AmountForSnipe = 1 # Amount how much you want buy the token in spend.
MinLiquidityAdded = 20  # Set how much minimum liquidity added in pair address that you want to buy. set in spend. (eg : 2, 4, 7). if spend is WMATIC, 2 mean 2 WMATIC liquidity added.
MaxSlippage = 25  # Max Slippage or Prince Impact
SellToken = 1   # 0 = Not Sell after buy, 1 = Sell token after buy by take profit
Takeprofit = 250  # In percent

transactionRevertTime = 1000 #Limit for make transaction
gasAmount = 500000 #Minimul limit is 210000, more much more better.
gasPrice = 7 #Customize your GWEI (gas fee) here, cannot decimal. (eg : 5, 10, 25).

quickswapRouterAddress = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"
quickswapFactoryAddress = "0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32"

polygon_rpc = "https://polygon-rpc.com"          #BSC JSON-RPC