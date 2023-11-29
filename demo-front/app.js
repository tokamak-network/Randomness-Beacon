import { contractAddress, contractABI, rpcURL } from './contractConfig.js';
// const contractAddress = "0x674C18bD1eF0d273bF87C9dce477c874e49B61c0";

const rpcURL = "https://rpc.titan-goerli.tokamak.network";
const contractABI = [{"type":"constructor","stateMutability":"nonpayable","inputs":[{"type":"uint256","name":"_entranceFee","internalType":"uint256"}]},{"type":"event","name":"CalculatedOmega","inputs":[{"type":"uint256","name":"round","internalType":"uint256","indexed":false},{"type":"uint256","name":"omega","internalType":"uint256","indexed":false},{"type":"uint256","name":"calculatedTimestamp","internalType":"uint256","indexed":false},{"type":"bool","name":"isCompleted","internalType":"bool","indexed":false}],"anonymous":false},{"type":"event","name":"CommitC","inputs":[{"type":"address","name":"participant","internalType":"address","indexed":false},{"type":"uint256","name":"commit","internalType":"uint256","indexed":false},{"type":"string","name":"commitsString","internalType":"string","indexed":false},{"type":"uint256","name":"commitCount","internalType":"uint256","indexed":false},{"type":"uint256","name":"commitTimestamp","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"RaffleEntered","inputs":[{"type":"address","name":"_entrant","internalType":"address","indexed":true},{"type":"uint256","name":"_amount","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"RaffleWinner","inputs":[{"type":"address","name":"_winner","internalType":"address","indexed":true},{"type":"uint256","name":"_round","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"Recovered","inputs":[{"type":"address","name":"msgSender","internalType":"address","indexed":false},{"type":"uint256","name":"recov","internalType":"uint256","indexed":false},{"type":"uint256","name":"omegaRecov","internalType":"uint256","indexed":false},{"type":"uint256","name":"recoveredTimestamp","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"RevealA","inputs":[{"type":"address","name":"participant","internalType":"address","indexed":false},{"type":"uint256","name":"a","internalType":"uint256","indexed":false},{"type":"uint256","name":"revealLeftCount","internalType":"uint256","indexed":false},{"type":"uint256","name":"revealTimestamp","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"Start","inputs":[{"type":"address","name":"msgSender","internalType":"address","indexed":false},{"type":"uint256","name":"startTime","internalType":"uint256","indexed":false},{"type":"uint256","name":"commitDuration","internalType":"uint256","indexed":false},{"type":"uint256","name":"commitRevealDuration","internalType":"uint256","indexed":false},{"type":"uint256","name":"n","internalType":"uint256","indexed":false},{"type":"uint256","name":"g","internalType":"uint256","indexed":false},{"type":"uint256","name":"h","internalType":"uint256","indexed":false},{"type":"uint256","name":"T","internalType":"uint256","indexed":false},{"type":"uint256","name":"round","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"balance","internalType":"uint256"}],"name":"balancesAtRound","inputs":[{"type":"uint256","name":"round","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"calculateOmega","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"checkStage","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"commitDuration","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"commitRevealDuration","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"c","internalType":"uint256"},{"type":"uint256","name":"a","internalType":"uint256"},{"type":"address","name":"participantAddress","internalType":"address"}],"name":"commitRevealValues","inputs":[{"type":"uint256","name":"round","internalType":"uint256"},{"type":"uint256","name":"index","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"commitsString","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"count","inputs":[]},{"type":"function","stateMutability":"payable","outputs":[],"name":"enterRafByCommit","inputs":[{"type":"uint256","name":"_commit","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"entranceFee","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"getWinnerAddress","inputs":[{"type":"uint256","name":"_round","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"recover","inputs":[{"type":"uint256","name":"_round","internalType":"uint256"},{"type":"tuple[]","name":"proofs","internalType":"struct Pietrzak_VDF.VDFClaim[]","components":[{"type":"uint256","name":"n","internalType":"uint256"},{"type":"uint256","name":"x","internalType":"uint256"},{"type":"uint256","name":"y","internalType":"uint256"},{"type":"uint256","name":"T","internalType":"uint256"},{"type":"uint256","name":"v","internalType":"uint256"}]}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"reveal","inputs":[{"type":"uint256","name":"_a","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"round","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"enum CommitRecover.Stages"}],"name":"stage","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"start","inputs":[{"type":"uint256","name":"_commitDuration","internalType":"uint256"},{"type":"uint256","name":"_commitRevealDuration","internalType":"uint256"},{"type":"uint256","name":"_n","internalType":"uint256"},{"type":"tuple[]","name":"_proofs","internalType":"struct Pietrzak_VDF.VDFClaim[]","components":[{"type":"uint256","name":"n","internalType":"uint256"},{"type":"uint256","name":"x","internalType":"uint256"},{"type":"uint256","name":"y","internalType":"uint256"},{"type":"uint256","name":"T","internalType":"uint256"},{"type":"uint256","name":"v","internalType":"uint256"}]}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"startTime","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"index","internalType":"uint256"},{"type":"bool","name":"committed","internalType":"bool"},{"type":"bool","name":"revealed","internalType":"bool"}],"name":"userInfosAtRound","inputs":[{"type":"address","name":"owner","internalType":"address"},{"type":"uint256","name":"round","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"omega","internalType":"uint256"},{"type":"uint256","name":"bStar","internalType":"uint256"},{"type":"uint256","name":"numOfParticipants","internalType":"uint256"},{"type":"uint256","name":"g","internalType":"uint256"},{"type":"uint256","name":"h","internalType":"uint256"},{"type":"uint256","name":"n","internalType":"uint256"},{"type":"uint256","name":"T","internalType":"uint256"},{"type":"bool","name":"isCompleted","internalType":"bool"},{"type":"bool","name":"isAllRevealed","internalType":"bool"}],"name":"valuesAtRound","inputs":[{"type":"uint256","name":"round","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"winnerAddress","internalType":"address"}],"name":"winnerAddresses","inputs":[{"type":"uint256","name":"round","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"withdraw","inputs":[{"type":"uint256","name":"_round","internalType":"uint256"}]}];

document.addEventListener('DOMContentLoaded', () => {
    const connectWalletButton = document.getElementById('connectWallet');
    const disconnectWalletButton = document.getElementById('disconnectWallet');
    const betAmountInput = document.getElementById('betAmount');
    const placeBetButton = document.getElementById('placeBet');
    const checkWinnerButton = document.getElementById('checkWinner');
    const statusElement = document.getElementById('status');
	const deadlineElement = document.getElementById('time-left');
	const startTime = 1700920681; // 예시 timestamp 값
	const commitDuration = 360000; // 예시 commitDuration 값 (100시간)
	const prizeAtRound = 100; // 예시 상금 값 (100ETH)
	
	let web3;
    let raffleContract;
    let userAccount;
	
	updateContractInfo(); // 페이지 로드 시 정보를 업데이트합니다.


	// 상금을 업데이트하는 함수를 비동기 함수로 작성
	async function updatePrize(round) {
	  try {
		const prize = await raffleContract.methods.balancesAtRound(round).call();
		const prizeElement = document.getElementById('prize-collected');
		prizeElement.textContent = web3.utils.fromWei(prize, 'ether') + ' ETH';
	  } catch (error) {
		console.error(`Error fetching prize for round ${round}:`, error);
	  }
	}

	

	// 남은 시간을 계산하고 표시하는 함수
	function updateDeadline() {
		const currentTime = Math.floor(Date.now() / 1000); // 현재 시간을 초 단위로 변환
		const deadlineTime = startTime + commitDuration; // 마감 시간 계산
		const timeLeft = deadlineTime - currentTime; // 남은 시간 계산


		if (timeLeft > 0) {
			const hours = Math.floor(timeLeft / 3600);
			const minutes = Math.floor((timeLeft % 3600) / 60);
			const seconds = timeLeft % 60;

			deadlineElement.textContent = `${hours}:${minutes}:${seconds}`;
		} else {
			deadlineElement.textContent = 'Event is Over';
		}
	}
	
	// 남은 시간을 주기적으로 업데이트
	setInterval(updateDeadline, 1000);
	// 남은 상금을 주기적으로 업데이트, 예시로 라운드는 2 (이 값도 같이 가져와야함 원래는)
	// 남은 상금을 주기적으로 업데이트
	setInterval(() => {
	  if (userAccount && raffleContract) {
		updatePrize(2); // 예제로 라운드 2를 사용
	  }
	}, 100000);


	// 지갑 정보 업데이트
	function updateWalletInfo(accounts) {
		const walletElement = document.getElementById('wallet');
		if (accounts.length === 0) {
			walletElement.textContent = 'No wallet connected';
		} else {
			const account = accounts[0];
			const shortAccount = account.substring(0, 6) + '...' + account.substring(account.length - 4);
			walletElement.textContent = shortAccount;
		}
	}
	
	
	// 상금과 남은 시간을 업데이트하는 함수입니다.
	async function updateContractInfo() {
	  if (!userAccount || !raffleContract) {
		// 월렛이 연결되어 있지 않으면 메시지를 표시합니다.
		document.getElementById('prize-collected').textContent = "To check the event info, you need to connect the wallet";
		document.getElementById('time-left').textContent = "To check the event info, you need to connect the wallet";
	  } else {
		try {
		  // 월렛이 연결되어 있으면 상금과 남은 시간을 업데이트합니다.
		  const currentRound = await raffleContract.methods.round().call();
		  const prize = await raffleContract.methods.balancesAtRound(currentRound).call();
		  document.getElementById('prize-collected').textContent = web3.utils.fromWei(prize, 'ether') + ' ETH';
	  
		  const startTimeValue = await raffleContract.methods.startTime().call();
		  const currentTime = Math.floor(Date.now() / 1000);
		  const timeLeft = startTimeValue - currentTime;

		  // 남은 시간을 업데이트합니다.
		  if (timeLeft > 0) {
			const deadlineElement = document.getElementById('time-left');
			const hours = Math.floor(timeLeft / 3600);
			const minutes = Math.floor((timeLeft % 3600) / 60);
			const seconds = timeLeft % 60;

			deadlineElement.textContent = `${hours}:${minutes}:${seconds}`;
		  } else {
			deadlineElement.textContent = 'Event is Over';
		  }
		} catch (error) {
		  console.error(`Error updating contract info: ${error.message}`);
		}
	  }
	}


	// 지갑이 연결되면 상금과 남은 시간 정보를 업데이트합니다.
	window.ethereum.on('accountsChanged', function (accounts) {
	  if (accounts.length > 0) {
		userAccount = accounts[0];
		updateWalletInfo(accounts);
		updateContractInfo(); // 지갑 연결시 정보 업데이트
	  } else {
		// 지갑 연결 해제시 초기 메시지로 변경
		document.getElementById('prize-collected').textContent = "To check the event info, you need to connect the wallet";
		document.getElementById('time-left').textContent = "";
      
		userAccount = null;
		updateWalletInfo([]);
	  }
	});

	

	// 네트워크 정보 업데이트
	function updateNetworkInfo() {
		const networkElement = document.getElementById('network'); // 여기에 정의가 필요합니다.
		if (web3 == null) {
			networkElement.textContent = "No network";
		}
		else {
			
			web3.eth.net.getId()
				.then(networkId => {
					let networkName = '';
					switch(networkId) {
						case 1n:
							networkName = 'Eth Mainnet';
							break;
						case 3n:
							networkName = 'Eth Ropsten';
							break;
						case 4n:
							networkName = 'Eth Rinkeby';
							break;
						case 5n:
							networkName = 'Eth Goerli';
							break;  
						case 5050n:
							networkName = 'Titan-Goerli';
							break;
						default:
							networkName = 'Unknown';
					}
					networkElement.textContent = networkName; // 이제 올바르게 업데이트됩니다.
				})
				.catch(err => {
					console.error('Error getting network:', err);
				});
		}
	}



	// Web3 인스턴스 초기화 및 이벤트 리스너 설정
	function initializeWeb3() {
		if (typeof window.ethereum !== 'undefined') {
			web3 = new Web3(window.ethereum);
			raffleContract = new web3.eth.Contract(contractABI, contractAddress);

			// 네트워크 정보 업데이트 함수 호출
			updateNetworkInfo();

			// 계정 변경 이벤트 리스너
			window.ethereum.on('accountsChanged', function (accounts) {
				if (accounts.length === 0) {
					userAccount = null;
					updateWalletInfo([]); // 계정 정보 업데이트
					// 연결된 계정이 없다는 것을 UI에 업데이트
					const walletElement = document.getElementById('wallet');
					walletElement.textContent = 'No wallet connected';
				} else {
					userAccount = accounts[0];
					updateWalletInfo(accounts); // 계정 정보 업데이트
					// 계정 정보를 UI에 업데이트
					const walletElement = document.getElementById('wallet');
					const shortAccount = userAccount.substring(0, 6) + '...' + userAccount.substring(userAccount.length - 4);
					walletElement.textContent = shortAccount;
				}
			});

			// 네트워크 변경 이벤트 리스너
			window.ethereum.on('chainChanged', (_chainId) => {
				window.location.reload();
			});
		} else {
			console.error('Ethereum wallet is not available');
		}
	}

	
    // 지갑 연결
	connectWalletButton.addEventListener('click', async () => {
		if (window.ethereum) {
			window.ethereum.request({ method: 'eth_requestAccounts' })
				.then(accounts => {
					initializeWeb3();
					userAccount = accounts[0];
					updateWalletInfo(accounts); // 지갑 정보 업데이트
					updateNetworkInfo(); // 네트워크 정보 업데이트
					statusElement.textContent = `Connected: ${userAccount}`;
					connectWalletButton.style.display = 'none';
					disconnectWalletButton.style.display = 'block';

				})
				.catch(err => {
					statusElement.textContent = `Error: ${err.message}`;
				});
		} else {
			statusElement.textContent = 'Please install MetaMask.';
		}
	});

    // 지갑 연결 해제
    disconnectWalletButton.addEventListener('click', () => {
        userAccount = null;
        raffleContract = null;
        web3 = null;
        statusElement.textContent = 'Wallet disconnected.';
		updateNetworkInfo('No network'); // 네트워크 정보를 초기화합니다.
		updateWalletInfo(); // 지갑 정보를 초기화합니다.
        connectWalletButton.style.display = 'block';
        disconnectWalletButton.style.display = 'none';
    });
	


    // 베팅
    placeBetButton.addEventListener('click', () => {
		const betAmount = betAmountInput.value;
		if (!betAmount || !userAccount || !raffleContract) {
			statusElement.textContent = 'Please connect to wallet and enter a bet amount.';
			return;
		}

		// betAmount를 BigNumber로 변환
		const betAmountBN = web3.utils.BN(betAmount);

		raffleContract.methods.enterRafByCommit(betAmountBN)
			.send({
				from: userAccount,
				value: web3.utils.toWei(betAmount, 'ether'),
				gasPrice: web3.utils.toWei('10', 'gwei')
			})
			.then(() => {
				statusElement.textContent = `Bet placed with ${betAmount} ETH.`;
			})
			.catch(err => {
				statusElement.textContent = `Error placing bet: ${err.message}`;
			});
	});

    // 당첨자 확인
    checkWinnerButton.addEventListener('click', () => {
        if (!userAccount || !raffleContract) {
            statusElement.textContent = 'Please connect to wallet.';
            return;
        }

        raffleContract.methods.getWinnerAddress(/* round number */)
            .call()
            .then(winnerAddress => {
                statusElement.textContent = `Winner Address: ${winnerAddress}`;
            })
            .catch(err => {
                statusElement.textContent = `Error fetching winner: ${err.message}`;
            });
    });


});
