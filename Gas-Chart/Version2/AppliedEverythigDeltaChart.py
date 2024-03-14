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
  [ 0, 3812394, 'λ2048', 'T2^22' ],
  [ 0, 4003581, 'λ2048', 'T2^23' ],
  [ 0, 4170383, 'λ2048', 'T2^24' ],
  [ 1, 3629464, 'λ2048', 'T2^22' ],
  [ 1, 3820191, 'λ2048', 'T2^23' ],
  [ 1, 3985359, 'λ2048', 'T2^24' ],
  [ 2, 3448702, 'λ2048', 'T2^22' ],
  [ 2, 3636290, 'λ2048', 'T2^23' ],
  [ 2, 3800986, 'λ2048', 'T2^24' ],
  [ 3, 3272839, 'λ2048', 'T2^22' ],
  [ 3, 3455921, 'λ2048', 'T2^23' ],
  [ 3, 3618947, 'λ2048', 'T2^24' ],
  [ 4, 3096073, 'λ2048', 'T2^22' ],
  [ 4, 3276943, 'λ2048', 'T2^23' ],
  [ 4, 3439765, 'λ2048', 'T2^24' ],
  [ 5, 2922464, 'λ2048', 'T2^22' ],
  [ 5, 3102407, 'λ2048', 'T2^23' ],
  [ 5, 3265198, 'λ2048', 'T2^24' ],
  [ 6, 2754928, 'λ2048', 'T2^22' ],
  [ 6, 2934606, 'λ2048', 'T2^23' ],
  [ 6, 3097042, 'λ2048', 'T2^24' ],
  [ 7, 2601514, 'λ2048', 'T2^22' ],
  [ 7, 2777817, 'λ2048', 'T2^23' ],
  [ 7, 2941820, 'λ2048', 'T2^24' ],
  [ 8, 2470614, 'λ2048', 'T2^22' ],
  [ 8, 2645229, 'λ2048', 'T2^23' ],
  [ 8, 2809183, 'λ2048', 'T2^24' ],
  [ 9, 2385186, 'λ2048', 'T2^22' ],
  [ 9, 2557626, 'λ2048', 'T2^23' ],
  [ 9, 2721487, 'λ2048', 'T2^24' ],
  [ 10, 2399814, 'λ2048', 'T2^22' ],
  [ 10, 2566266, 'λ2048', 'T2^23' ],
  [ 10, 2730371, 'λ2048', 'T2^24' ],
  [ 11, 2591846, 'λ2048', 'T2^22' ],
  [ 11, 2761255, 'λ2048', 'T2^23' ],
  [ 11, 2925500, 'λ2048', 'T2^24' ],
  [ 12, 3184194, 'λ2048', 'T2^22' ],
  [ 12, 3352280, 'λ2048', 'T2^23' ],
  [ 12, 3519398, 'λ2048', 'T2^24' ],
  [ 13, 4692416, 'λ2048', 'T2^22' ],
  [ 13, 4861332, 'λ2048', 'T2^23' ],
  [ 13, 5030589, 'λ2048', 'T2^24' ],
  [ 14, 8289184, 'λ2048', 'T2^22' ],
  [ 14, 8496112, 'λ2048', 'T2^23' ],
  [ 14, 8660687, 'λ2048', 'T2^24' ]
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
plt.axvline(x=9.00000001, linestyle='dotted', color='black')
plt.text(9.9, 9290000, 'Minimum', ha='right', fontsize=11)
# plt.annotate('Minimum', xy=(10.00000001, 4200000), xytext=(0, 50), 
#              textcoords='offset points', ha='right', va='bottom',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.legend(title="T", fontsize=13, title_fontsize=13)
plt.xlabel('Delta', labelpad= 15, fontsize=13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Adjust the bottom margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.2)
plt.show()