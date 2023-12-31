# Commit-Reveal-Recover-RNG

Commit-Reveal-Recover RNG (Random Number Generator) is a random number generation project for blockchain.
For secure and safe random number generation, we use the commit-reveal-recover scheme.
We used the [Bicorn-RX](https://eprint.iacr.org/2023/221) mechanism on the ground.
There are changes in our implementation. One big difference is we used the Pietrzak VDF instead of the Wesolowski VDF.
There are two major reasons. Firstly, the hash-to-prime function is too costly on the blockchain. Secondly, [the VDF implementation article](https://drops.dagstuhl.de/storage/01oasics/oasics-vol082-tokenomics2020/OASIcs.Tokenomics.2020.9/OASIcs.Tokenomics.2020.9.pdf) from Tokemnomics shows the Pietrzak's VDF is more efficient in verification which is part of the protocol should be implemented on the blockchain.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Demo app](#demo-app)
- [VDF-Prover](#VDF-Prover)
- [VDF-Verifier](#VDF-Verifier)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Introduction

Why Commit-Reveal-Recover Scheme and VDFs Matter? Generating random numbers on a blockchain requires mechanisms that ensure trustworthiness, fairness, and security. This is where the Commit-Reveal-Recover scheme and Verifiable Delay Functions (VDFs) play a crucial role. 

### 1. Trustworthy Randomness
- **Importance**: Ensuring a source of randomness that is impervious to manipulation or prediction by any participant is critical for applications like lotteries, gaming, or smart contract execution on a blockchain.

### 2. Commit-Reveal-Recover Scheme
- **Commit Phase**: Participants commit to a value secretly, typically via a hash of their secret number, preventing post-hoc changes.
- **Reveal Phase**: Participants reveal their secret numbers, and the final random number is derived from these.
- **Recover Phase**: Ensures the random number generation process can continue even if a participant fails to reveal their number, maintaining integrity.

### 3. Role of Verifiable Delay Functions (VDFs)
- **Time-locking**: VDFs impose a known and significant computational time delay, deterring manipulation attempts in the commit phase.
- **Unpredictability and Verifiability**: Adds an element of secure unpredictability and verifiability, crucial for fairness in decentralized environments.

### 4. Enhancing Security and Fairness
- **Summary**: By integrating these mechanisms, blockchain systems can generate random numbers that are secure, tamper-proof, and fair, essential for maintaining the integrity of numerous blockchain-based applications.


## Features

- Secure random number generation for blockchain applications.
- Implementation of the Commit-Reveal-Recover scheme.
- Integration of Pietrzak's Verifiable Delay Function (VDF) for enhanced efficiency.

## Installation
### Requirements
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
- pip packages
  - To run this project, you need to install the required Python libraries. You can do this easily using the `./VDF-prover/requirements.txt` file, which lists all the necessary dependencies. Execute the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```

### Quick Start
```shell
git clone --recurse-submodules https://github.com/tokamak-network/Commit-Reveal-Recover-RNG.git
cd demo-front2
yarn
yarn dev
```

## Usage 


1. Install 
> In a different terminal / command line
```
cd demo-contract/Raffle-Bicorn-RX
yarn
```

2. set .env at root folder of Raffle-Bicorn-RX
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

3. Run your local blockchain with the Christmas Gift Distribution code
```
yarn hardhat node
```
> You can read more about how to use that repo from its [README.md](https://github.com/tokamak-network/Raffle-Bicorn-RX/blob/main/README.md)

4. Add hardhat network to your metamask/wallet

- Get the RPC_URL of your hh node (usually `http://127.0.0.1:8545/`)
- Go to your wallet and add a new network. [See instructions here.](https://metamask.zendesk.com/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC)
  - Network Name: Hardhat-Localhost
  - New RPC URL: http://127.0.0.1:8545/
  - Chain ID: 31337
  - Currency Symbol: ETH (or GO)
  - Block Explorer URL: None
Ideally, you'd then [import one of the accounts](https://metamask.zendesk.com/hc/en-us/articles/360015489331-How-to-import-an-Account) from hardhat to your wallet/metamask. 

5. Run this code

Back in a different terminal with the code from this repo, run:

```
yarn dev
```

6. Go to UI and have fun!

Head over to your [localhost](http://localhost:3000) and play with the Christmas Gift Distribution Event!

### UI Usage
- setup
- commit
- recovery

## Demo app

- Demo app: [Demo App Link]()

## Contributing
We welcome contributions to the project. Please refer to our contribution guidelines for more information on how to participate.

## Contact
[Your Contact Information - for queries, collaborations, or further discussions.]

## License

The project is available as open source under the terms of the MIT License
