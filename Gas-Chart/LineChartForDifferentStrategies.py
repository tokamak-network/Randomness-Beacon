# Copyright 2024 justin
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import json
import os

path = os.getcwd() + '/gasReportForDifferentStrategies.json'
with open(path) as f:
    gasReport = json.load(f)

lambdas = ["λ1024", "λ2048", "λ3072"]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#17becf', '#8c564b']
markers = ['D', 'o', 's', '^' ,'v', '$V$']
ts = ["T2^20", "T2^21", "T2^22", "T2^23", "T2^24", "T2^25"]
tsValue = [2**20, 2**21, 2**22, 2**23, 2**24, 2**25]
strategies = ["commitRecover", "commitRecoverWithTInProof", "commitRecoverWithNTInProof", "commitRecoverWithNTInProofVerifyAndProcessSeparate", "commitRecoverWithNTInProofVerifyAndProcessSeparateFileSeparate", "commitRecoverWithNTInProofVerifyAndProcessSeparateFileSeparateWithoutOptimizer"]
strategiesLabels = ["s0+s1+s2+s3+s4+s5", "s0+s1+s2+s3+s4", "s0+s1+s2+s3", "s0+s1+s2", "s0+s1", "s0"]
lambdaIndex = 0
alpha = [1, 1, 1, 0.8, 0.8, 1]
lineStyes = ['-', '--', ':']

for s in range(len(strategies)):
    eachStrategy = gasReport[strategies[s]]
    for lambdaIndex in range(len(lambdas)):
        oneLambdaData = eachStrategy[lambdaIndex]
        x = []
        y = []
        for i in range(len(oneLambdaData)):#6
            key = lambdas[lambdaIndex] + ts[i]
            data = oneLambdaData[i][key][0]['recoverGas']
            x.append(ts[i])
            y.append(int(data))
        print(key)
        plt.plot(x, y, color=colors[s], marker=markers[s], label = lambdas[lambdaIndex] + " " + strategiesLabels[s], alpha=alpha[s], linestyle=lineStyes[lambdaIndex])
plt.legend(title="Strategies", loc='upper left', bbox_to_anchor=(1, 1))
plt.xlabel('Number of exponentiations', labelpad= 15)
plt.ylabel('Gas used', labelpad= 15)
plt.gcf().set_size_inches(9, 7)
plt.tight_layout()
plt.show()