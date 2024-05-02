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
ts = ["2^{22}", "2^{23}", "2^{24}"]
data = [
  [ '0', '3643402', 'λ2048', 'T2^22' ],
  [ '0', '3826182', 'λ2048', 'T2^23' ],
  [ '0', '3989543', 'λ2048', 'T2^24' ],
  [ '1', '3468478', 'λ2048', 'T2^22' ],
  [ '1', '3649559', 'λ2048', 'T2^23' ],
  [ '1', '3813125', 'λ2048', 'T2^24' ],
  [ '2', '3295899', 'λ2048', 'T2^22' ],
  [ '2', '3475634', 'λ2048', 'T2^23' ],
  [ '2', '3638293', 'λ2048', 'T2^24' ],
  [ '3', '3125881', 'λ2048', 'T2^22' ],
  [ '3', '3303148', 'λ2048', 'T2^23' ],
  [ '3', '3465732', 'λ2048', 'T2^24' ],
  [ '4', '2956873', 'λ2048', 'T2^22' ],
  [ '4', '3134860', 'λ2048', 'T2^23' ],
  [ '4', '3295483', 'λ2048', 'T2^24' ],
  [ '5', '2792098', 'λ2048', 'T2^22' ],
  [ '5', '2971324', 'λ2048', 'T2^23' ],
  [ '5', '3128613', 'λ2048', 'T2^24' ],
  [ '6', '2634809', 'λ2048', 'T2^22' ],
  [ '6', '2811170', 'λ2048', 'T2^23' ],
  [ '6', '2967414', 'λ2048', 'T2^24' ],
  [ '7', '2488209', 'λ2048', 'T2^22' ],
  [ '7', '2664384', 'λ2048', 'T2^23' ],
  [ '7', '2821604', 'λ2048', 'T2^24' ],
  [ '8', '2366820', 'λ2048', 'T2^22' ],
  [ '8', '2540952', 'λ2048', 'T2^23' ],
  [ '8', '2695911', 'λ2048', 'T2^24' ],
  [ '9', '2297629', 'λ2048', 'T2^22' ],
  [ '9', '2470594', 'λ2048', 'T2^23' ],
  [ '9', '2620907', 'λ2048', 'T2^24' ],
  [ '10', '2309998', 'λ2048', 'T2^22' ],
  [ '10', '2481625', 'λ2048', 'T2^23' ],
  [ '10', '2634953', 'λ2048', 'T2^24' ],
  [ '11', '2509716', 'λ2048', 'T2^22' ],
  [ '11', '2678874', 'λ2048', 'T2^23' ],
  [ '11', '2838802', 'λ2048', 'T2^24' ],
  [ '12', '3116128', 'λ2048', 'T2^22' ],
  [ '12', '3281754', 'λ2048', 'T2^23' ],
  [ '12', '3444516', 'λ2048', 'T2^24' ],
  [ '13', '4625115', 'λ2048', 'T2^22' ],
  [ '13', '4790519', 'λ2048', 'T2^23' ],
  [ '13', '4955212', 'λ2048', 'T2^24' ],
  [ '14', '8272395', 'λ2048', 'T2^22' ],
  [ '14', '8434021', 'λ2048', 'T2^23' ],
  [ '14', '8596715', 'λ2048', 'T2^24' ]
]
colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(int(data[i][0]))
    y[i%3].append(int(data[i][1]))
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00000001, color='black')
plt.text(9.9, 9010000, 'Minimum', ha='right', fontsize=13)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$T$', fontsize=13, title_fontsize=13)
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