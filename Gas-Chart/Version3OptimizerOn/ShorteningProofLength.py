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
[ 0, 4268869, 'λ2048', 'T2^22' ],
[ 0, 4484684, 'λ2048', 'T2^23' ],
[ 0, 4677011, 'λ2048', 'T2^24' ],
[ 1, 4062898, 'λ2048', 'T2^22' ],
[ 1, 4278109, 'λ2048', 'T2^23' ],
[ 1, 4468634, 'λ2048', 'T2^24' ],
[ 2, 3859607, 'λ2048', 'T2^22' ],
[ 2, 4071623, 'λ2048', 'T2^23' ],
[ 2, 4261529, 'λ2048', 'T2^24' ],
[ 3, 3661606, 'λ2048', 'T2^22' ],
[ 3, 3868811, 'λ2048', 'T2^23' ],
[ 3, 4056527, 'λ2048', 'T2^24' ],
[ 4, 3462938, 'λ2048', 'T2^22' ],
[ 4, 3667365, 'λ2048', 'T2^23' ],
[ 4, 3854603, 'λ2048', 'T2^24' ],
[ 5, 3267382, 'λ2048', 'T2^22' ],
[ 5, 3470406, 'λ2048', 'T2^23' ],
[ 5, 3657462, 'λ2048', 'T2^24' ],
[ 6, 3077966, 'λ2048', 'T2^22' ],
[ 6, 3280941, 'λ2048', 'T2^23' ],
[ 6, 3466515, 'λ2048', 'T2^24' ],
[ 7, 2903018, 'λ2048', 'T2^22' ],
[ 7, 3102792, 'λ2048', 'T2^23' ],
[ 7, 3288678, 'λ2048', 'T2^24' ],
[ 8, 2750351, 'λ2048', 'T2^22' ],
[ 8, 2948468, 'λ2048', 'T2^23' ],
[ 8, 3133541, 'λ2048', 'T2^24' ],
[ 9, 2643574, 'λ2048', 'T2^22' ],
[ 9, 2839878, 'λ2048', 'T2^23' ],
[ 9, 3024061, 'λ2048', 'T2^24' ],
[ 10, 2633139, 'λ2048', 'T2^22' ],
[ 10, 2827490, 'λ2048', 'T2^23' ],
[ 10, 3012383, 'λ2048', 'T2^24' ],
[ 11, 2809373, 'λ2048', 'T2^22' ],
[ 11, 3001226, 'λ2048', 'T2^23' ],
[ 11, 3186446, 'λ2048', 'T2^24' ],
[ 12, 3381062, 'λ2048', 'T2^22' ],
[ 12, 3572015, 'λ2048', 'T2^23' ],
[ 12, 3758923, 'λ2048', 'T2^24' ],
[ 13, 4870507, 'λ2048', 'T2^22' ],
[ 13, 5062116, 'λ2048', 'T2^23' ],
[ 13, 5251932, 'λ2048', 'T2^24' ],
[ 14, 8485766, 'λ2048', 'T2^22' ],
[ 14, 8671847, 'λ2048', 'T2^23' ],
[ 14, 8857414, 'λ2048', 'T2^24' ]
]

colors = ['#ff0000', '#008800', '#0000ff']
markers = ['o', '^', 's']  # circle, triangle, square
x = [[],[],[]]
y = [[],[],[]]
for i in range(len(data)):
    x[i%3].append(data[i][0])
    y[i%3].append(data[i][1])
for i in range(3):
    plt.plot(x[i], y[i], color=colors[i], label="$"+ts[i]+"$", marker=markers[i])
plt.axvline(x=10.00285,  color='black')
plt.text(10.9, 9290000, 'Minimum', ha='right', fontsize=11)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title="T", fontsize=13, title_fontsize=13)
plt.xlabel('Number of Skipped Proof', labelpad= 15, fontsize=13, y=-0.1)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Adjust the bottom margin
plt.subplots_adjust(left=0.17)
plt.subplots_adjust(bottom=0.2)
plt.grid(True, linestyle="--")
plt.savefig('4. delta.png', dpi=500)
plt.show()