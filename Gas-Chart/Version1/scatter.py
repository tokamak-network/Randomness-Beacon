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

path = os.getcwd() + '/gasReport.json'
with open(path) as f:
    gasReport = json.load(f)

lambdas = ["λ1024", "λ2048", "λ3072"]
colors = ['#ff0000', '#008800', '#0000ff']
ts = ["T2^20", "T2^21", "T2^22", "T2^23", "T2^24", "T2^25"]
tsValue = [2**20, 2**21, 2**22, 2**23, 2**24, 2**25]

gasCostsCommitRecover = gasReport["gasCostsCommitRecover"]
datasets = {'a': [], 'b': [], 'c': []}
for i in range(len(gasCostsCommitRecover)):
    eachLambda = gasCostsCommitRecover[i]
    for j in range(len(eachLambda)):
        temp = eachLambda[j]
        key = lambdas[i] + ts[j]
        data = temp[key]
        for k in range(len(data)):
            gasUsed = data[k]["verifyRecursiveHalvingProofForSetupInternalGasUsed"]
            # print(lambdas[i])
            # print(ts[j])
            # print(gasUsed)
            # print(colors[i])
            datasets['a'].append(ts[j])
            datasets['b'].append(int(gasUsed))
            datasets['c'].append(colors[i])
            datasets['label'] = lambdas[i]
plt.scatter('a', 'b', c='c', edgecolors='none', alpha= 0.3, data = datasets)
plt.legend(lambdas, colors, ncols=3, title="Lambdas")
plt.xlabel('Number of exponentiations', labelpad= 15)
plt.ylabel('Gas used', labelpad= 15)
plt.yticks(np.arange(1000000, 9000000, 1000000))

# Create a legend
legend_elements = [mlines.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i], markersize=5) for i in range(len(lambdas))]
plt.legend(legend_elements, lambdas,)

#print(np.arange(1000000, 9000000, 1000000))
# plt.xticks(tsValue, ts)
plt.show()

