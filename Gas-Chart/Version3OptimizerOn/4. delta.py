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
[ 0, 4131580, 'λ2048', 'T2^22' ],
[ 0, 4338398, 'λ2048', 'T2^23' ],
[ 0, 4524584, 'λ2048', 'T2^24' ],
[ 1, 3932997, 'λ2048', 'T2^22' ],
[ 1, 4137935, 'λ2048', 'T2^23' ],
[ 1, 4324264, 'λ2048', 'T2^24' ],
[ 2, 3736964, 'λ2048', 'T2^22' ],
[ 2, 3940390, 'λ2048', 'T2^23' ],
[ 2, 4125672, 'λ2048', 'T2^24' ],
[ 3, 3543674, 'λ2048', 'T2^22' ],
[ 3, 3744440, 'λ2048', 'T2^23' ],
[ 3, 3929512, 'λ2048', 'T2^24' ],
[ 4, 3351539, 'λ2048', 'T2^22' ],
[ 4, 3552835, 'λ2048', 'T2^23' ],
[ 4, 3735821, 'λ2048', 'T2^24' ],
[ 5, 3163758, 'λ2048', 'T2^22' ],
[ 5, 3366152, 'λ2048', 'T2^23' ],
[ 5, 3545689, 'λ2048', 'T2^24' ],
[ 6, 2983633, 'λ2048', 'T2^22' ],
[ 6, 3182961, 'λ2048', 'T2^23' ],
[ 6, 3361399, 'λ2048', 'T2^24' ],
[ 7, 2814391, 'λ2048', 'T2^22' ],
[ 7, 3013367, 'λ2048', 'T2^23' ],
[ 7, 3192596, 'λ2048', 'T2^24' ],
[ 8, 2670491, 'λ2048', 'T2^22' ],
[ 8, 2867227, 'λ2048', 'T2^23' ],
[ 8, 3044114, 'λ2048', 'T2^24' ],
[ 9, 2570100, 'λ2048', 'T2^22' ],
[ 9, 2764719, 'λ2048', 'T2^23' ],
[ 9, 2941399, 'λ2048', 'T2^24' ],
[ 10, 2569988 , 'λ2048', 'T2^22' ],
[ 10, 2758688, 'λ2048', 'T2^23' ],
[ 10, 2938663, 'λ2048', 'T2^24' ],
[ 11, 2747641, 'λ2048', 'T2^22' ],
[ 11, 2938981, 'λ2048', 'T2^23' ],
[ 11, 3120647, 'λ2048', 'T2^24' ],
[ 12, 3332896, 'λ2048', 'T2^22' ],
[ 12, 3513812, 'λ2048', 'T2^23' ],
[ 12, 3697927, 'λ2048', 'T2^24' ],
[ 13, 4821724, 'λ2048', 'T2^22' ],
[ 13, 5009264, 'λ2048', 'T2^23' ],
[ 13, 5195785, 'λ2048', 'T2^24' ],
[ 14, 8443857, 'λ2048', 'T2^22' ],
[ 14, 8627038, 'λ2048', 'T2^23' ],
[ 14, 8810992, 'λ2048', 'T2^24' ]
]

#colors = ['#ff0000', '#008800', '#0000ff']
colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(data[i][0])
    y[i%3].append(data[i][1])
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=10.00285,  color='black')
plt.text(10.9, 9290000, 'Minimum', ha='right', fontsize=15)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title=r'$\tau$', fontsize=18, title_fontsize=18)
plt.xlabel('Number of Skipped Proof',labelpad= 10.9,fontsize=21 ) #y=-0.1
plt.ylabel('Gas Used ($10^6$)', labelpad= 18, fontsize=21)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
# Adjust the bottom margin
#plt.subplots_adjust(top=0.55)
plt.subplots_adjust(bottom=0.1)
plt.grid(True, linestyle="--")
# fig_size = plt.gcf().get_size_inches() # Get current size
# fig_size[1] += 0.1
# plt.gcf().set_size_inches(fig_size) # Set new size
plt.tight_layout()
plt.savefig('4. delta.png', dpi=500)
plt.show()