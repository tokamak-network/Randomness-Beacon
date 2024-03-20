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
[ 1891828, 'λ1024', 'T2^20' ],
[ 1993090, 'λ1024', 'T2^21' ],
[ 2096346, 'λ1024', 'T2^22' ],
[ 2198301, 'λ1024', 'T2^23' ],
[ 2295138, 'λ1024', 'T2^24' ],
[ 2407067, 'λ1024', 'T2^25' ],
[ 3854404, 'λ2048', 'T2^20' ],
[ 4060607, 'λ2048', 'T2^21' ],
[ 4264504, 'λ2048', 'T2^22' ],
[ 4480256, 'λ2048', 'T2^23' ],
[ 4672532, 'λ2048', 'T2^24' ],
[ 4897782, 'λ2048', 'T2^25' ],
[ 6803677, 'λ3072', 'T2^20' ],
[ 7155541, 'λ3072', 'T2^21' ],
[ 7522241, 'λ3072', 'T2^22' ],
[ 7875852, 'λ3072', 'T2^23' ],
[ 8241395, 'λ3072', 'T2^24' ],
[ 8630845, 'λ3072', 'T2^25' ]
]
SkippingNTXY = [
[ 1619152, 'λ1024', 'T2^20' ],
[ 1705994, 'λ1024', 'T2^21' ],
[ 1794658, 'λ1024', 'T2^22' ],
[ 1881964, 'λ1024', 'T2^23' ],
[ 1963648, 'λ1024', 'T2^24' ],
[ 2060991, 'λ1024', 'T2^25' ],
[ 3421513, 'λ2048', 'T2^20' ],
[ 3603278, 'λ2048', 'T2^21' ],
[ 3783873, 'λ2048', 'T2^22' ],
[ 3976451, 'λ2048', 'T2^23' ],
[ 4143920, 'λ2048', 'T2^24' ],
[ 4345666, 'λ2048', 'T2^25' ],
[ 6203051, 'λ3072', 'T2^20' ],
[ 6521354, 'λ3072', 'T2^21' ],
[ 6854762, 'λ3072', 'T2^22' ],
[ 7174986, 'λ3072', 'T2^23' ],
[ 7506720, 'λ3072', 'T2^24' ],
[ 7863167, 'λ3072', 'T2^25' ]
]

BitSize = [1024, 2048, 3072]
colors = ['#ff0000', '#008800', '#0000ff']
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
        ySkippingTXY[i//6].append(SkippingNTXY[i+j][0])

for i in range(0,3):
    plt.plot(xNTXYVInProof[i], yNTXYVInProof[i], color=colors[i], marker=markers[i], label=str(BitSize[i])+" λ")
    plt.plot(xSkippingTXY[i], ySkippingTXY[i], color=colors[i], marker=markers[i], linestyle='--', label=str(BitSize[i])+" λ, Skipped deterministic elements")

plt.xlabel('T', labelpad= 15, fontsize = 13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize = 13)

custom_lines = [Line2D([0], [0], color='red', lw=2),
                Line2D([0], [0], color='green', lw=2),
                Line2D([0], [0], color='blue', lw=2),
                Line2D([0], [0], color='black', linestyle='--', lw=2)]

plt.legend(custom_lines, ['λ = 1024', 'λ = 2048', 'λ = 3072', 'Shortening Proof Size'], fontsize=12)
#plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0., fontsize = 13)

# custom_lines = [Line2D([0], [0], color=colors[i], lw=2) for i in range(3)] + [Line2D([0], [0], color='black', linestyle=lineStyles[i], lw=2) for i in range(2)]
# plt.legend(custom_lines, [str(BitSize[i]) + ' Bits' for i in range(3)] + ['One N', 'N in Proof'])

plt.gca().yaxis.get_offset_text().set_visible(False)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.subplots_adjust(left=0.15, bottom=0.2) #, right=0.65)  # Adjust the right space as needed)

plt.show()