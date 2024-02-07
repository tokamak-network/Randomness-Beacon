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

import numpy as np
import matplotlib.pyplot as plt
import json
import os

path = os.getcwd() + '/gasReport.json'
print(path)
with open(path) as f:
    gasReport = json.load(f)

lambdas = ["λ1024", "λ2048", "λ3072"]
colors = ['#ff0000', '#008800', '#0000ff']
ts = ["T2^20", "T2^21", "T2^22", "T2^23", "T2^24", "T2^25"]
tsValue = [2**20, 2**21, 2**22, 2**23, 2**24, 2**25]

gasCostsCommitRecover = gasReport["gasCostsCommitRecover"]

for i in range(len(gasCostsCommitRecover)):
    eachLambda = gasCostsCommitRecover[i]
    x = []
    y = []
    yerr = []
    for j in range(len(eachLambda)):
        temp = eachLambda[j]
        key = lambdas[i] + ts[j]
        data = temp[key]
        x.append(ts[j])
        yValues = []
        for k in range(len(data)):
            gasUsed = data[k]["verifyRecursiveHalvingProofForSetupInternalGasUsed"]
            yValues.append(int(gasUsed))
        y.append(np.mean(yValues))
        yerr.append(np.std(yValues))
        print(np.std(yValues))
    plt.errorbar(x, y, yerr=yerr, color=colors[i], label=lambdas[i])

plt.legend(title="Lambdas")
plt.xlabel('Number of exponentiations', labelpad= 15)
plt.ylabel('Gas used', labelpad= 15)


plt.show()