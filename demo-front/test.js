<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Web3 Contract Interaction</title>
    <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
    <script>
        // Asynchronous function to interact with the contract
        async function interactWithContract() {
            try {
                const rpcURL = "YOUR_RPC_URL_HERE"; // Replace with your RPC URL
                const contractAddress = "YOUR_CONTRACT_ADDRESS_HERE"; // Replace with your contract address
                const contractABI = YOUR_CONTRACT_ABI_HERE; // Replace with your contract ABI

                const web3Test = new Web3(rpcURL);
                const contract = new web3Test.eth.Contract(contractABI, contractAddress);

                const r = await contract.methods.round().call();
                document.getElementById('output').innerText = `Value of r: ${r}`;
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('output').innerText = 'fail';
            }
        }
    </script>
</head>
<body>
    <h1>Web3 Contract Interaction</h1>
    <button onclick="interactWithContract()">Interact with Contract</button>
    <p id="output"></p>
</body>
</html>
