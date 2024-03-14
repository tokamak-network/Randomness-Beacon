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
dataOneT = [
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
dataTInProof = [
  [ 1866304, 'λ1024', 'T2^20' ],
  [ 1969137, 'λ1024', 'T2^21' ],
  [ 2068732, 'λ1024', 'T2^22' ],
  [ 2171364, 'λ1024', 'T2^23' ],
  [ 2263604, 'λ1024', 'T2^24' ],
  [ 2377000, 'λ1024', 'T2^25' ],
  [ 3794603, 'λ2048', 'T2^20' ],
  [ 3993337, 'λ2048', 'T2^21' ],
  [ 4196576, 'λ2048', 'T2^22' ],
  [ 4406601, 'λ2048', 'T2^23' ],
  [ 4592259, 'λ2048', 'T2^24' ],
  [ 4817673, 'λ2048', 'T2^25' ],
  [ 6705993, 'λ3072', 'T2^20' ],
  [ 7048592, 'λ3072', 'T2^21' ],
  [ 7406292, 'λ3072', 'T2^22' ],
  [ 7756824, 'λ3072', 'T2^23' ],
  [ 8116820, 'λ3072', 'T2^24' ],
  [ 8502882, 'λ3072', 'T2^25' ]
]
BitSize = [1024, 2048, 3072]
colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

xOneT = [[],[],[]]
yOneT = [[],[],[]]
xTInProof = [[],[],[]]
yTInProof = [[],[],[]]

for i in range(0, len(dataOneT), 6):
    for j in range(0,6):
        xOneT[i//6].append(ts[j])
        xTInProof[i//6].append(ts[j])
        yOneT[i//6].append(dataOneT[i+j][0])
        yTInProof[i//6].append(dataTInProof[i+j][0])

for i in range(0,3):
    plt.plot(xOneT[i], yOneT[i], color=colors[i], label="$\lambda$="+str(BitSize[i])+" One T", marker=markers[i], linestyle=lineStyles[0])
    plt.plot(xTInProof[i], yTInProof[i], color=colors[i], label="$\lambda$="+str(BitSize[i])+" T in Proof", marker=markers[i], linestyle=lineStyles[1])

plt.xlabel('T', labelpad= 15, fontsize = 13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize = 13)
plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0., fontsize = 13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
# Adjust the bottom margin
plt.subplots_adjust(left=0.15, bottom=0.2, right=0.65)  # Adjust the right space as needed)
plt.show()