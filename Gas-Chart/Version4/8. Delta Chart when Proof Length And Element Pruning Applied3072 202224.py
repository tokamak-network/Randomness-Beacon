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
  [ '0', '6065357', 'λ3072', 'T2^20' ],
  [ '0', '6701878', 'λ3072', 'T2^22' ],
  [ '0', '7354495', 'λ3072', 'T2^24' ],
  [ '1', '5748738', 'λ3072', 'T2^20' ],
  [ '1', '6383071', 'λ3072', 'T2^22' ],
  [ '1', '7032908', 'λ3072', 'T2^24' ],
  [ '2', '5435247', 'λ3072', 'T2^20' ],
  [ '2', '6065631', 'λ3072', 'T2^22' ],
  [ '2', '6713091', 'λ3072', 'T2^24' ],
  [ '3', '5124954', 'λ3072', 'T2^20' ],
  [ '3', '5753613', 'λ3072', 'T2^22' ],
  [ '3', '6397061', 'λ3072', 'T2^24' ],
  [ '4', '4820408', 'λ3072', 'T2^20' ],
  [ '4', '5446081', 'λ3072', 'T2^22' ],
  [ '4', '6090540', 'λ3072', 'T2^24' ],
  [ '5', '4523561', 'λ3072', 'T2^20' ],
  [ '5', '5145851', 'λ3072', 'T2^22' ],
  [ '5', '5785397', 'λ3072', 'T2^24' ],
  [ '6', '4239607', 'λ3072', 'T2^20' ],
  [ '6', '4857883', 'λ3072', 'T2^22' ],
  [ '6', '5498098', 'λ3072', 'T2^24' ],
  [ '7', '3981547', 'λ3072', 'T2^20' ],
  [ '7', '4597578', 'λ3072', 'T2^22' ],
  [ '7', '5232785', 'λ3072', 'T2^24' ],
  [ '8', '3785477', 'λ3072', 'T2^20' ],
  [ '8', '4425788', 'λ3072', 'T2^22' ],
  [ '8', '5059652', 'λ3072', 'T2^24' ],
  [ '9', '3680363', 'λ3072', 'T2^20' ],
  [ '9', '4318050', 'λ3072', 'T2^22' ],
  [ '9', '4947040', 'λ3072', 'T2^24' ],
  [ '10', '3782566', 'λ3072', 'T2^20' ],
  [ '10', '4409533', 'λ3072', 'T2^22' ],
  [ '10', '5037178', 'λ3072', 'T2^24' ],
  [ '11', '4300682', 'λ3072', 'T2^20' ],
  [ '11', '4908917', 'λ3072', 'T2^22' ],
  [ '11', '5537941', 'λ3072', 'T2^24' ],
  [ '12', '5683888', 'λ3072', 'T2^20' ],
  [ '12', '6290043', 'λ3072', 'T2^22' ],
  [ '12', '6909863', 'λ3072', 'T2^24' ],
  [ '13', '8801861', 'λ3072', 'T2^20' ],
  [ '13', '9390036', 'λ3072', 'T2^22' ],
  [ '13', '10007353', 'λ3072', 'T2^24' ],
  [ '14', '15857049', 'λ3072', 'T2^20' ],
  [ '14', '16432336', 'λ3072', 'T2^22' ],
  [ '14', '17040333', 'λ3072', 'T2^24' ],
]
ts = ["20", "22",  "24"]
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
plt.text(10, 17950000, 'Minimum', ha='right', fontsize=13)
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