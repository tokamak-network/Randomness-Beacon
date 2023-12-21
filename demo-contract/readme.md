# Christmas Gift Event using Commit-Reveal-Recover Random Number Generation(RNG)

Raffle App using Commit Reveal Recover<br>

# Getting Started
## Requirements
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - You'll know you did it right if you can run:
    - `git --version` and you see a response like `git version x.x.x`
- [Nodejs](https://nodejs.org/en/)
  - You'll know you've installed nodejs right if you can run:
    - `node --version` and get an output like: `vx.x.x`
- [Yarn](https://yarnpkg.com/getting-started/install) instead of `npm`
  - You'll know you've installed yarn right if you can run:
    - `yarn --version` and get an output like: `x.x.x`
    - You might need to [install it with `npm`](https://classic.yarnpkg.com/lang/en/docs/install/) or `corepack`

## INSTALL (Quick Start)
```shell
git clone https://github.com/tokamak-network/Raffle-Bicorn-RX.git
cd Raffle-Bicorn-RX
yarn
```

## SET .env
```shell
MAINNET_RPC_URL=
SEPOLIA_RPC_URL=
POLYGON_MAINNET_RPC_URL=
PRIVATE_KEY=
ETHERSCAN_API_KEY=
REPORT_GAS=true
COINMARKETCAP_API_KEY=
```
- `MAINNET_RPC_URL`, `SEPOLIA_RPC_URL`, `POLYGON_MAINNET_RPC_URL`
  - Get url from [Infura](https://app.infura.io/dashboard) or [Alchemy](https://alchemy.com/?a=673c802981)
- PRIVATE_KEY
  - The private key of your account (like from [metamask](https://metamask.io/)). **NOTE:** FOR DEVELOPMENT, PLEASE USE A KEY THAT DOESN'T HAVE ANY REAL FUNDS ASSOCIATED WITH IT.
  - You can [learn how to export it here](https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key).
- ETHERSCAN_API_KEY
  - Get api key from [Etherscan](https://etherscan.io/myapikey/)
- COINMARKETCAP_API_KEY
  - Get api key from [CoinMarketCap](https://pro.coinmarketcap.com/account/)

## DEPLOY
### Hardhat
```
yarn hardhat deploy --tags raffle
```
### Sepolia
- Get testnet ETH
  - Head over to [Sepolia Faucet](https://sepoliafaucet.com/) or [faucets.chain.link](https://faucets.chain.link/) and get some testnet ETH. you should see the ETH show up in your metamask.
```
yarn hardhat deploy --network sepolia --tags raffle
```

## Verify on Etherscan
In it's current state, if you have your api key set in .env, it will auto verify sepolia contracts.

However, you can manual verify with:

```
yarn hardhat verify DEPLOYED_CONTRACT_ADDRESS --network sepolia
```

## Testing
```
yarn hardhat test --grep "Raffle Unit Test2"
```