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
dataOneN = [
  [ 1860190, 'λ1024', 'T2^20' ],
  [ 1962678, 'λ1024', 'T2^21' ],
  [ 2061923, 'λ1024', 'T2^22' ],
  [ 2163918, 'λ1024', 'T2^23' ],
  [ 2256095, 'λ1024', 'T2^24' ],
  [ 2369127, 'λ1024', 'T2^25' ],
  [ 3788253, 'λ2048', 'T2^20' ],
  [ 3986632, 'λ2048', 'T2^21' ],
  [ 4189499, 'λ2048', 'T2^22' ],
  [ 4399000, 'λ2048', 'T2^23' ],
  [ 4584430, 'λ2048', 'T2^24' ],
  [ 4809456, 'λ2048', 'T2^25' ],
  [ 6699424, 'λ3072', 'T2^20' ],
  [ 7041627, 'λ3072', 'T2^21' ],
  [ 7398934, 'λ3072', 'T2^22' ],
  [ 7748782, 'λ3072', 'T2^23' ],
  [ 8108660, 'λ3072', 'T2^24' ],
  [ 8494305, 'λ3072', 'T2^25' ]
]
dataNInProof = [
  [ 1942560, 'λ1024', 'T2^20' ],
  [ 2049454, 'λ1024', 'T2^21' ],
  [ 2153153, 'λ1024', 'T2^22' ],
  [ 2259593, 'λ1024', 'T2^23' ],
  [ 2356515, 'λ1024', 'T2^24' ],
  [ 2473822, 'λ1024', 'T2^25' ],
  [ 3916498, 'λ2048', 'T2^20' ],
  [ 4122869, 'λ2048', 'T2^21' ],
  [ 4332564, 'λ2048', 'T2^22' ],
  [ 4548546, 'λ2048', 'T2^23' ],
  [ 4742327, 'λ2048', 'T2^24' ],
  [ 4973745, 'λ2048', 'T2^25' ],
  [ 6876822, 'λ3072', 'T2^20' ],
  [ 7229436, 'λ3072', 'T2^21' ],
  [ 7596921, 'λ3072', 'T2^22' ],
  [ 7956718, 'λ3072', 'T2^23' ],
  [ 8326702, 'λ3072', 'T2^24' ],
  [ 8721443, 'λ3072', 'T2^25' ]
]
BitSize = [1024, 2048, 3072]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

x = [[],[],[]]
y = [[],[],[]]

for i in range(0, len(dataOneN), 6):
    for j in range(0,6):
        x[i//6].append(ts[j])
        y[i//6].append(dataNInProof[i+j][0] - dataOneN[i+j][0])

for i in range(0,3):
    plt.plot(x[i], y[i], color=colors[i], marker=markers[i], label=str(BitSize[i])+" Bits")

plt.xlabel('T', labelpad= 15, fontsize=13)
plt.ylabel('Gas Difference', labelpad= 15,  fontsize=13)
plt.legend(fontsize=12)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

# Adjust the bottom margin
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)
plt.show()
