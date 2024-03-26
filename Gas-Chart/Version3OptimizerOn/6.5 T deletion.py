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
from matplotlib.lines import Line2D
NTXYVInProof = [
[ 1793639, 'λ1024', 'T2^20' ],
[ 1885927, 'λ1024', 'T2^21' ],
[ 1983777, 'λ1024', 'T2^22' ],
[ 2070565, 'λ1024', 'T2^23' ],
[ 2168214, 'λ1024', 'T2^24' ],
[ 2270274, 'λ1024', 'T2^25' ],
[ 3746113, 'λ2048', 'T2^20' ],
[ 3937877, 'λ2048', 'T2^21' ],
[ 4127804, 'λ2048', 'T2^22' ],
[ 4334579, 'λ2048', 'T2^23' ],
[ 4520732, 'λ2048', 'T2^24' ],
[ 4735860, 'λ2048', 'T2^25' ],
[ 6671421, 'λ3072', 'T2^20' ],
[ 7006711, 'λ3072', 'T2^21' ],
[ 7374009, 'λ3072', 'T2^22' ],
[ 7701888, 'λ3072', 'T2^23' ],
[ 8093851, 'λ3072', 'T2^24' ],
[ 8456547, 'λ3072', 'T2^25' ]
]
SkippingTXY= [
[ 1607330, 'λ1024', 'T2^20' ],
[ 1689862, 'λ1024', 'T2^21' ],
[ 1777877, 'λ1024', 'T2^22' ],
[ 1854329, 'λ1024', 'T2^23' ],
[ 1942226, 'λ1024', 'T2^24' ],
[ 2034145, 'λ1024', 'T2^25' ],
[ 3445876, 'λ2048', 'T2^20' ],
[ 3621520, 'λ2048', 'T2^21' ],
[ 3795294, 'λ2048', 'T2^22' ],
[ 3985474, 'λ2048', 'T2^23' ],
[ 4155505, 'λ2048', 'T2^24' ],
[ 4354133, 'λ2048', 'T2^25' ],
[ 6252882, 'λ3072', 'T2^20' ],
[ 6565265, 'λ3072', 'T2^21' ],
[ 6909757, 'λ3072', 'T2^22' ],
[ 7214339, 'λ3072', 'T2^23' ],
[ 7583122, 'λ3072', 'T2^24' ],
[ 7922488, 'λ3072', 'T2^25' ]
]

BitSize = [1024, 2048, 3072]
colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

xNTXYVInProof = [[],[],[]]
yNTXYVInProof = [[],[],[]]
xSkippingTXY = [[],[],[]]
ySkippingTXY = [[],[],[]]

for i in range(0,len(NTXYVInProof),6):
    for j in range(0,6):
        xNTXYVInProof[i//6].append(ts[j])
        yNTXYVInProof[i//6].append(NTXYVInProof[i+j][0])
        xSkippingTXY[i//6].append(ts[j])
        ySkippingTXY[i//6].append(SkippingTXY[i+j][0])

for i in range(0,3):
    plt.plot(xNTXYVInProof[i], yNTXYVInProof[i], color=colors[i], marker=markers[i], label=str(BitSize[i])+" λ")
    plt.plot(xSkippingTXY[i], ySkippingTXY[i], color=colors[i], marker=markers[i], linestyle='--', label=str(BitSize[i])+" λ, Skipped deterministic elements")

plt.xlabel(r'Exponentiation ($\tau$)', labelpad= 15, fontsize = 14)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize = 15)

custom_lines = [Line2D([0], [0], color='tab:red', marker='o', lw=1.5),
                Line2D([0], [0], color='tab:green', marker='^', lw=1.5),
                Line2D([0], [0], color='tab:blue', marker='s', lw=1.5),
                Line2D([0], [0], color='black', linestyle='--', lw=1)]

plt.legend(custom_lines, ['λ = 1024', 'λ = 2048', 'λ = 3072', 'Deleted Dynamic Elements'], prop={'size': 10.2}, bbox_to_anchor=(0.51, 0.759))
#plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0., fontsize = 13)

# custom_lines = [Line2D([0], [0], color=colors[i], lw=2) for i in range(3)] + [Line2D([0], [0], color='black', linestyle=lineStyles[i], lw=2) for i in range(2)]
# plt.legend(custom_lines, [str(BitSize[i]) + ' Bits' for i in range(3)] + ['One N', 'N in Proof'])

plt.gca().yaxis.get_offset_text().set_visible(False)
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)#, right=0.65)  # Adjust the right space as needed)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('6.5 T deletion.png', dpi=500)
plt.show()
