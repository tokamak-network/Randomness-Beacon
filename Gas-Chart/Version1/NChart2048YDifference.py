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
  [ 3788253, 'λ2048', 'T2^20' ],
  [ 3986632, 'λ2048', 'T2^21' ],
  [ 4189499, 'λ2048', 'T2^22' ],
  [ 4399000, 'λ2048', 'T2^23' ],
  [ 4584430, 'λ2048', 'T2^24' ],
  [ 4809456, 'λ2048', 'T2^25' ],
]
dataNInProof = [
  [ 3916498, 'λ2048', 'T2^20' ],
  [ 4122869, 'λ2048', 'T2^21' ],
  [ 4332564, 'λ2048', 'T2^22' ],
  [ 4548546, 'λ2048', 'T2^23' ],
  [ 4742327, 'λ2048', 'T2^24' ],
  [ 4973745, 'λ2048', 'T2^25' ],
]
BitSize = [2048]
colors = ['#ff0000', '#0000ff']
markers = ['o', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

x = []
y = []

for i in range(0, len(dataOneN)):
    x.append(ts[i])
    y.append(dataNInProof[i][0] - dataOneN[i][0])

plt.plot(x, y, color=colors[0], marker=markers[0], linestyle=lineStyles[0])


plt.xlabel('T', labelpad= 15, fontsize=13)
plt.ylabel('Gas Difference', labelpad= 15, fontsize=13)
plt.legend(fontsize=12)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
# Adjust the bottom margin
plt.subplots_adjust(left=0.2, bottom=0.2)
plt.show()