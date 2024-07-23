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
  [ '0', '3308930', 'λ2048', 'T2^20' ],
  [ '0', '3643402', 'λ2048', 'T2^22' ],
  [ '0', '3989543', 'λ2048', 'T2^24' ],
  [ '1', '3135721', 'λ2048', 'T2^20' ],
  [ '1', '3468478', 'λ2048', 'T2^22' ],
  [ '1', '3813125', 'λ2048', 'T2^24' ],
  [ '2', '2963630', 'λ2048', 'T2^20' ],
  [ '2', '3295899', 'λ2048', 'T2^22' ],
  [ '2', '3638293', 'λ2048', 'T2^24' ],
  [ '3', '2794327', 'λ2048', 'T2^20' ],
  [ '3', '3125881', 'λ2048', 'T2^22' ],
  [ '3', '3465732', 'λ2048', 'T2^24' ],
  [ '4', '2626595', 'λ2048', 'T2^20' ],
  [ '4', '2956873', 'λ2048', 'T2^22' ],
  [ '4', '3295483', 'λ2048', 'T2^24' ],
  [ '5', '2464088', 'λ2048', 'T2^20' ],
  [ '5', '2792098', 'λ2048', 'T2^22' ],
  [ '5', '3128613', 'λ2048', 'T2^24' ],
  [ '6', '2306342', 'λ2048', 'T2^20' ],
  [ '6', '2634809', 'λ2048', 'T2^22' ],
  [ '6', '2967414', 'λ2048', 'T2^24' ],
  [ '7', '2161639', 'λ2048', 'T2^20' ],
  [ '7', '2488209', 'λ2048', 'T2^22' ],
  [ '7', '2821604', 'λ2048', 'T2^24' ],
  [ '8', '2039705', 'λ2048', 'T2^20' ],
  [ '8', '2366820', 'λ2048', 'T2^22' ],
  [ '8', '2695911', 'λ2048', 'T2^24' ],
  [ '9', '1970844', 'λ2048', 'T2^20' ],
  [ '9', '2297629', 'λ2048', 'T2^22' ],
  [ '9', '2620907', 'λ2048', 'T2^24' ],
  [ '10', '1985637', 'λ2048', 'T2^20' ],
  [ '10', '2309998', 'λ2048', 'T2^22' ],
  [ '10', '2634953', 'λ2048', 'T2^24' ],
  [ '11', '2195372', 'λ2048', 'T2^20' ],
  [ '11', '2509716', 'λ2048', 'T2^22' ],
  [ '11', '2838802', 'λ2048', 'T2^24' ],
  [ '12', '2790844', 'λ2048', 'T2^20' ],
  [ '12', '3116128', 'λ2048', 'T2^22' ],
  [ '12', '3444516', 'λ2048', 'T2^24' ],
  [ '13', '4298936', 'λ2048', 'T2^20' ],
  [ '13', '4625115', 'λ2048', 'T2^22' ],
  [ '13', '4955212', 'λ2048', 'T2^24' ],
  [ '14', '7955464', 'λ2048', 'T2^20' ],
  [ '14', '8272395', 'λ2048', 'T2^22' ],
  [ '14', '8596715', 'λ2048', 'T2^24' ],
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
plt.axvline(x=9.00000001, color='black')
plt.text(10, 9030000, 'Minimum', ha='right', fontsize=13)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 10.9,fontsize=15 ) 
plt.ylabel('Gas Used ($10^6$)', labelpad= 18, fontsize=15)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
# Adjust the bottom margin
#plt.subplots_adjust(top=0.55)
plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('8. Delta Chart when Proof Length And Element Pruning Applied.png', dpi=500)
plt.show()