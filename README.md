# Commit-Reveal-Recover-RNG

Commit-Reveal-Recover RNG (Random Number Generator) is a random number generation project for blockchain.
For secure and safe random number generation, we use the commit-reveal-recover scheme.
We used the [Bicorn-RX](https://eprint.iacr.org/2023/221) mechanism on the ground.
There are changes in our implementation. One big difference is we used the Pietrzak VDF instead of the Wesolowski VDF.
There are two major reasons. Firstly, the hash-to-prime function is too costly on the blockchain. Secondly, [the VDF implementation article](https://drops.dagstuhl.de/storage/01oasics/oasics-vol082-tokenomics2020/OASIcs.Tokenomics.2020.9/OASIcs.Tokenomics.2020.9.pdf) from Tokemnomics shows the Pietrzak's VDF is more efficient in verification which is part of the protocol should be implemented on the blockchain.


## Table of Contents

- [Commit-Reveal-Recover](#commit-reveal-recover)
- [Demo app](#demo-app)
- [VDF-Prover](#VDF-Prover)
- [VDF-Verifier](#VDF-Verifier)
- [License](#license)

## Commit-Reveal-Recover

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

## Demo app

- Demo app page link: https://raffle-bicorn-rx-front.vercel.app/
- Demo app prover: 
- Demo app verifier: 
- Demo app front: 

## VDF-Prover

You need to use our Python VDF code. But you can use another Pietrzak implementation. Theoretically, it will work for verifiers.
The Python code not only supports VDF evaluation/verification but also full commit-reveal-recover simulation.

## VDF-Verifier

VDF Verifier is implemented in Solidity.

## License

The project is available as open source under the terms of the MIT License
