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
[ 0, 3647756, 'λ2048', 'T2^22' ],
[ 0, 3831007, 'λ2048', 'T2^23' ],
[ 0, 3994412, 'λ2048', 'T2^24' ],
[ 1, 3472585, 'λ2048', 'T2^22' ],
[ 1, 3654106, 'λ2048', 'T2^23' ],
[ 1, 3817748, 'λ2048', 'T2^24' ],
[ 2, 3299749, 'λ2048', 'T2^22' ],
[ 2, 3479939, 'λ2048', 'T2^23' ],
[ 2, 3642650, 'λ2048', 'T2^24' ],
[ 3, 3129497, 'λ2048', 'T2^22' ],
[ 3, 3307187, 'λ2048', 'T2^23' ],
[ 3, 3469855, 'λ2048', 'T2^24' ],
[ 4, 2960230, 'λ2048', 'T2^22' ],
[ 4, 3138657, 'λ2048', 'T2^23' ],
[ 4, 3299349, 'λ2048', 'T2^24' ],
[ 5, 2795221, 'λ2048', 'T2^22' ],
[ 5, 2974855, 'λ2048', 'T2^23' ],
[ 5, 3132244, 'λ2048', 'T2^24' ],
[ 6, 2637675, 'λ2048', 'T2^22' ],
[ 6, 2814459, 'λ2048', 'T2^23' ],
[ 6, 2970787, 'λ2048', 'T2^24' ],
[ 7, 2490849, 'λ2048', 'T2^22' ],
[ 7, 2667407, 'λ2048', 'T2^23' ],
[ 7, 2824751, 'λ2048', 'T2^24' ],
[ 8, 2369185, 'λ2048', 'T2^22' ],
[ 8, 2543717, 'λ2048', 'T2^23' ],
[ 8, 2698784, 'λ2048', 'T2^24' ],
[ 9, 2290828, 'λ2048', 'T2^22' ],
[ 9, 2463480, 'λ2048', 'T2^23' ],
[ 9, 2618446, 'λ2048', 'T2^24' ],
[ 10, 2311847, 'λ2048', 'T2^22' ],
[ 10, 2483847, 'λ2048', 'T2^23' ],
[ 10, 2637298, 'λ2048', 'T2^24' ],
[ 11, 2511255, 'λ2048', 'T2^22' ],
[ 11, 2680746, 'λ2048', 'T2^23' ],
[ 11, 2840834, 'λ2048', 'T2^24' ],
[ 12, 3117367, 'λ2048', 'T2^22' ],
[ 12, 3283334, 'λ2048', 'T2^23' ],
[ 12, 3439552, 'λ2048', 'T2^24' ],
[ 13, 4626270, 'λ2048', 'T2^22' ],
[ 13, 4791977, 'λ2048', 'T2^23' ],
[ 13, 4956846, 'λ2048', 'T2^24' ],
[ 14, 8273531, 'λ2048', 'T2^22' ],
[ 14, 8435476, 'λ2048', 'T2^23' ],
[ 14, 8598319, 'λ2048', 'T2^24' ]
]
colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(data[i][0])
    y[i%3].append(data[i][1])
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=9.00000001, color='black')
plt.text(9.9, 9080000, 'Minimum', ha='right', fontsize=15)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=18, title_fontsize=18)
plt.xlabel('Number of Skipped Proof', labelpad= 10.9,fontsize=21 ) 
plt.ylabel('Gas Used ($10^6$)', labelpad= 18, fontsize=21)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
# Adjust the bottom margin
#plt.subplots_adjust(top=0.55)
plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('8. Delta Chart when Proof Length And Element Pruning Applied.png', dpi=500)
plt.show()