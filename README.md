# Commit-Reveal-Recover-RNG

Commit-Reveal-Recover RNG (Random Number Generator) is a random number generation project for blockchain. 
For secure and safe random number generation, we use the commit-reveal-recover scheme.
As a detailed mechanism, we use Bicorn-RX from the Bicorn article.
The big difference is we used the Pietrzak VDF.
Also, we support Commit-Recover option. (described later)


## Table of Contents
  - [Commit-Reveal-Recover](#commit-reveal-recover)
  - [VDF-Prover](#VDF-Prover)
  - [VDF-Verifier](#VDF-Verifier)
  - [Demo app](#demo-app)
  - [Deployment](#deployment)
  - [License](#license)

## Commit-Reveal-Recover

Description for Commit-Reveal-Recover

## VDF-Prover

You need to use our Python VDF code. But you can use another Pietrzak implementation. Theoretically, it will work for verifiers.
The Python code not only supports VDF evaluation/verification but also full commit-reveal-recover simulation.

## VDF-Verifier

VDF Verifier is implemented in Solidity.

## Demo app

- Demo app link
- Demo app screenshot
- Demo app structure (solidity, frontend)
- How to get test tokens (faucets)

## Deployment

- hardhat instruction (recommended)



## License
The project is available as open source under the terms of the MIT License