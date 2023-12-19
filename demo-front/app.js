import {
    contractAddress,
    contractABI,
    rpcURL
}
from './contractConfig.js';



document.addEventListener('DOMContentLoaded', () => {
    const connectWalletButton = document.getElementById('connectWallet');
    const disconnectWalletButton = document.getElementById('disconnectWallet');
    const betAmountInput = document.getElementById('betAmount');
    const placeBetButton = document.getElementById('placeBet');
    const checkWinnerButton = document.getElementById('checkWinner');
    const statusElement = document.getElementById('status');
    const deadlineElement = document.getElementById('deadline');

    let web3;
    let raffleContract;
    let userAccount;
    
    let currentRound; 
    
    // 이벤트 시간 정보를 저장할 변수
    let eventStartTime;

    const web3PRC = new Web3(rpcURL);
    const contractRPC = new web3PRC.eth.Contract(contractABI, contractAddress);

    // 상금 정보 업데이트 주기 (예: 5분)
    const prizeUpdateInterval = 300000;
    
    
    // 페이지 로드 시 상금 정보 한 번 업데이트
    updatePrizeInfo();

    // 이후 5분 간격으로 상금 정보 업데이트
    setInterval(updatePrizeInfo, prizeUpdateInterval);
    
    
    // 상금 정보 업데이트 함수
    async function updatePrizeInfo() {
        try {
            currentRound = await contractRPC.methods.round().call();
            const prize = await contractRPC.methods.balancesAtRound(currentRound).call();
            document.getElementById('prize-amount').textContent = web3PRC.utils.fromWei(prize, 'ether');
        } catch (error) {
            console.error(`Error updating prize info: ${error.message}`);
        }
    }

    // 이벤트 시간 정보 가져오기 및 업데이트
    async function fetchEventTime() {
        try {
            eventStartTime = Number(await contractRPC.methods.startTime().call());
            updateEventTime();
        } catch (error) {
            console.error(`Error fetching event time: ${error.message}`);
        }
    }

    // 이벤트 시간 정보 시각적 업데이트
    function updateEventTime() {
        const currentTime = Math.floor(Date.now() / 1000);
        const timeDifference = currentTime - eventStartTime;
        const isEventOver = timeDifference > 0;

        const betContainer = document.querySelector('.bet-container');
        const checkWinnerButton = document.getElementById('checkWinner');

        if (isEventOver) {
            // 이벤트가 종료된 경우
            let days = Math.floor(timeDifference / 86400);
            let hours = Math.floor((timeDifference % 86400) / 3600);
            let minutes = Math.floor((timeDifference % 3600) / 60);
            let seconds = timeDifference % 60;

            deadlineElement.innerHTML = `Time passed: <span id="time-left">${days}d ${hours}h ${minutes}m ${seconds}s</span>`;
            
            // 베팅 컨테이너 숨기기
            // betContainer.style.display = 'none';

            // 버튼 텍스트 변경
            checkWinnerButton.textContent = 'Check Last Winner';
        } else {
            // 이벤트가 진행 중인 경우
            let days = Math.floor(-timeDifference / 86400);
            let hours = Math.floor((-timeDifference % 86400) / 3600);
            let minutes = Math.floor((-timeDifference % 3600) / 60);
            let seconds = -timeDifference % 60;

            deadlineElement.innerHTML = `Time left: <span id="time-left">${days}d ${hours}h ${minutes}m ${seconds}s</span>`;
            
            // 베팅 컨테이너 표시
            betContainer.style.display = 'block';

            // 버튼 텍스트 원래대로 설정
            checkWinnerButton.textContent = 'Check Winner';
        }

        // 1초 후에 다시 업데이트
        setTimeout(updateEventTime, 1000);
    }


    // 페이지 로드 시 entranceFee 값을 가져와서 베팅 금액 입력 필드에 설정
    fetchEntranceFee();
    
    // entranceFee 값을 가져오는 함수
    async function fetchEntranceFee() {
        try {
            const entranceFee = await contractRPC.methods.entranceFee().call();
            
            if (entranceFee === 0n) {
                // 게임이 없을 경우 메시지 표시
                betAmountInput.placeholder = 'No active round';
                betAmountInput.disabled = false; // 입력 필드 비활성화 -> true 로 수정필요
                placeBetButton.disabled = false; // 입력 버튼 비활성화 -> true 로 수정필요
            } else {
                // 게임이 있을 경우 기본 베팅 금액 설정
                const entranceFeeInEther = web3PRC.utils.fromWei(entranceFee, 'ether');
                betAmountInput.value = entranceFeeInEther;
                betAmountInput.disabled = false; // 입력 필드 활성화
                placeBetButton.disabled = false; // 입력 버튼 활성화
            }
        } catch (error) {
            console.error(`Error fetching entrance fee: ${error.message}`);
        }
    }


    // 초기 실행 시 이벤트 시간 정보 가져오기
    fetchEventTime();

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

    // 지갑이 연결되면 정보를 업데이트합니다.
    window.ethereum.on('accountsChanged', function (accounts) {
        if (accounts.length > 0) {
            userAccount = accounts[0];
            updateWalletInfo(accounts);
        } else {
            // 지갑 연결 해제시 계정 및 지갑 정보 초기화
            userAccount = null;
            updateWalletInfo([]);
        }
    });

    // 네트워크 정보 업데이트
    function updateNetworkInfo() {
        const networkElement = document.getElementById('network');
        if (web3 == null) {
            networkElement.textContent = "No network";
        } else {

            web3.eth.net.getId()
            .then(networkId => {
                let networkName = '';
                switch (networkId) {
                case 1n:
                    networkName = 'Eth Mainnet';
                    break;
                case 3n:
                    networkName = 'Eth Ropsten';
                    break;
                case 4n:
                    networkName = 'Eth Rinkeby';
                    break;
                case 11155111n:
                    networkName = 'Eth Sepolia';
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
    connectWalletButton.addEventListener('click', async() => {
        if (window.ethereum) {
            window.ethereum.request({
                method: 'eth_requestAccounts'
            })
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

    // 사전에 정의된 금액 전송 (베팅) 및 랜덤값 커밋
    // placeBet 버튼 이벤트 핸들러
    placeBetButton.addEventListener('click', async () => {
        const commitValue = betAmountInput.value;
        if (!commitValue || !userAccount || !raffleContract) {
            statusElement.textContent = 'Please connect to wallet and enter a commit value.';
            return;
        }

        try {
            const entranceFee = await raffleContract.methods.entranceFee().call();

            // commitValue를 Hex 형태로 변환
            let commitValueHex = web3.utils.asciiToHex(commitValue);

            // Hex 문자열의 길이를 조정 -> 수정필요 패딩의 길이
            const requiredLength = 64; // 32바이트 = 64 Hex 문자
            commitValueHex = commitValueHex.padEnd(requiredLength, '0');

            // Hex 문자열의 비트 길이 계산
            const bitLength = commitValueHex.length * 4;

            // enterRafByCommit 함수 호출
            await raffleContract.methods.enterRafByCommit({
                val: commitValueHex,
                neg: false, // 항상 false로 설정
                bitlen: bitLength
            }).send({
                from: userAccount,
                value: entranceFee,
                gasPrice: web3.utils.toWei('10', 'gwei')
            });

            statusElement.textContent = `Bet placed with entrance fee.`;
        } catch (err) {
            statusElement.textContent = `Error placing bet: ${err.message}`;
        }
    });




    // 당첨자 확인 및 버튼 생성
    checkWinnerButton.addEventListener('click', () => {
        contractRPC.methods.winnerAddresses(currentRound)
            .call()
            .then(winnerAddress => {
                let winnerInfo = `🐓🎊Winner🎉🎁 ${winnerAddress}`;
                if (userAccount && winnerAddress.toLowerCase() === userAccount.toLowerCase()) {
                    winnerInfo += " - Congratulations, You are the Winner!";
                    createWithdrawButton();
                    alert("Congratulations! You are the winner of this round!");
                }
                statusElement.innerHTML = `<div class="winner-info">${winnerInfo}</div>`;
            })
            .catch(err => {
                statusElement.textContent = `Error fetching winner: ${err.message}`;
            });
    });

    // Withdraw 버튼 생성
    function createWithdrawButton() {
        const withdrawButton = document.createElement('button');
        withdrawButton.textContent = 'Withdraw Prize';
        withdrawButton.className = 'withdraw-button';
        withdrawButton.onclick = withdrawPrize; // Withdraw 함수 연결
        statusElement.appendChild(withdrawButton);
    }

    // 상금 인출 함수
    function withdrawPrize() {
        if (!userAccount || !raffleContract) {
            alert("Please connect to a wallet.");
            return;
        }

        raffleContract.methods.withdraw(currentRound)
            .send({ from: userAccount })
            .then((receipt) => {
                console.log("Withdrawal successful", receipt);
                alert("Withdrawal successful.");
            })
            .catch(err => {
                console.error("Error during withdrawal: ", err);
                alert(`Error during withdrawal: ${err.message}`);
            });
    }



});
