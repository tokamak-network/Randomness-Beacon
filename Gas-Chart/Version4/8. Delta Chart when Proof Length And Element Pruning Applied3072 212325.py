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
data = [
  [ '0', '6367354', 'λ3072', 'T2^21' ],
  [ '0', '6996898', 'λ3072', 'T2^23' ],
  [ '0', '7683479', 'λ3072', 'T2^25' ],
  [ '1', '6049646', 'λ3072', 'T2^21' ],
  [ '1', '6675222', 'λ3072', 'T2^23' ],
  [ '1', '7360038', 'λ3072', 'T2^25' ],
  [ '2', '5733634', 'λ3072', 'T2^21' ],
  [ '2', '6363254', 'λ3072', 'T2^23' ],
  [ '2', '7038292', 'λ3072', 'T2^25' ],
  [ '3', '5421889', 'λ3072', 'T2^21' ],
  [ '3', '6052915', 'λ3072', 'T2^23' ],
  [ '3', '6718714', 'λ3072', 'T2^25' ],
  [ '4', '5114344', 'λ3072', 'T2^21' ],
  [ '4', '5741953', 'λ3072', 'T2^23' ],
  [ '4', '6406365', 'λ3072', 'T2^25' ],
  [ '5', '4814939', 'λ3072', 'T2^21' ],
  [ '5', '5439096', 'λ3072', 'T2^23' ],
  [ '5', '6099550', 'λ3072', 'T2^25' ],
  [ '6', '4530125', 'λ3072', 'T2^21' ],
  [ '6', '5154619', 'λ3072', 'T2^23' ],
  [ '6', '5808321', 'λ3072', 'T2^25' ],
  [ '7', '4275906', 'λ3072', 'T2^21' ],
  [ '7', '4892043', 'λ3072', 'T2^23' ],
  [ '7', '5542271', 'λ3072', 'T2^25' ],
  [ '8', '4098686', 'λ3072', 'T2^21' ],
  [ '8', '4718680', 'λ3072', 'T2^23' ],
  [ '8', '5369083', 'λ3072', 'T2^25' ],
  [ '9', '3967114', 'λ3072', 'T2^21' ],
  [ '9', '4614955', 'λ3072', 'T2^23' ],
  [ '9', '5254521', 'λ3072', 'T2^25' ],
  [ '10', '4086776', 'λ3072', 'T2^21' ],
  [ '10', '4704821', 'λ3072', 'T2^23' ],
  [ '10', '5341138', 'λ3072', 'T2^25' ],
  [ '11', '4588115', 'λ3072', 'T2^21' ],
  [ '11', '5203672', 'λ3072', 'T2^23' ],
  [ '11', '5841926', 'λ3072', 'T2^25' ],
  [ '12', '5977931', 'λ3072', 'T2^21' ],
  [ '12', '6578898', 'λ3072', 'T2^23' ],
  [ '12', '7208317', 'λ3072', 'T2^25' ],
  [ '13', '9081839', 'λ3072', 'T2^21' ],
  [ '13', '9677264', 'λ3072', 'T2^23' ],
  [ '13', '10303349', 'λ3072', 'T2^25' ],
  [ '14', '16131292', 'λ3072', 'T2^21' ],
  [ '14', '16719577', 'λ3072', 'T2^23' ],
  [ '14', '17331914', 'λ3072', 'T2^25' ]
]
ts = ["21", "23",  "25"]
colors = ["tab:red", "tab:green", "tab:blue"]
 # circle, triangle, square
markers = ['o', '^', 's']
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(int(data[i][0]))
    y[i%3].append(int(data[i][1]))
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00285,  color='black')
plt.text(10, 18150000, 'Minimum', ha='right', fontsize=13)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 10.9,fontsize=15 ) #y=-0.1
plt.ylabel('Gas Used ($10^6$)', labelpad= 7, fontsize=15)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, _):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(custom_formatter))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('8. Delta Chart when Proof Length And Element Pruning Applied3072.png', dpi=500)
plt.show()