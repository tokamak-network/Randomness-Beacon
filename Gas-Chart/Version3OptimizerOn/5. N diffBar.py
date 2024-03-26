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
import numpy as np
NTXYVInProof = [
[ 1793639, 'λ1024', 'T2^20' ],
[ 1885927, 'λ1024', 'T2^21' ],
[ 1983777, 'λ1024', 'T2^22' ],
[ 2070565, 'λ1024', 'T2^23' ],
[ 2168214, 'λ1024', 'T2^24' ],
[ 2270274, 'λ1024', 'T2^25' ],
[ 3746113, 'λ2048', 'T2^20' ],
[ 3937877, 'λ2048', 'T2^21' ],
[ 4127804, 'λ2048', 'T2^22' ],
[ 4334579, 'λ2048', 'T2^23' ],
[ 4520732, 'λ2048', 'T2^24' ],
[ 4735860, 'λ2048', 'T2^25' ],
[ 6671421, 'λ3072', 'T2^20' ],
[ 7006711, 'λ3072', 'T2^21' ],
[ 7374009, 'λ3072', 'T2^22' ],
[ 7701888, 'λ3072', 'T2^23' ],
[ 8093851, 'λ3072', 'T2^24' ],
[ 8456547, 'λ3072', 'T2^25' ]
]
SkippingN = [
[ 1717527, 'λ1024', 'T2^20' ],
[ 1805756, 'λ1024', 'T2^21' ],
[ 1899500, 'λ1024', 'T2^22' ],
[ 1982221, 'λ1024', 'T2^23' ],
[ 2075445, 'λ1024', 'T2^24' ],
[ 2173609, 'λ1024', 'T2^25' ],
[ 3623872, 'λ2048', 'T2^20' ],
[ 3808993, 'λ2048', 'T2^21' ],
[ 3991757, 'λ2048', 'T2^22' ],
[ 4191712, 'λ2048', 'T2^23' ],
[ 4371969, 'λ2048', 'T2^24' ],
[ 4579959, 'λ2048', 'T2^25' ],
[ 6500116, 'λ3072', 'T2^20' ],
[ 6825692, 'λ3072', 'T2^21' ],
[ 7183687, 'λ3072', 'T2^22' ],
[ 7502263, 'λ3072', 'T2^23' ],
[ 7884119, 'λ3072', 'T2^24' ],
[ 8237084, 'λ3072', 'T2^25' ]
]

BitSize = [1024, 2048, 3072]
#colors = ['black', 'silver', 'gray']  # Different shades of grey
colors = ["tab:red", "tab:green", "tab:blue"]
edgecolors=['black', 'black', 'gray']
patterns = [None, 'xx' , None]  # Patterns for the bars
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]

# Calculate differences
differences = {size: [] for size in BitSize}
for i, (ntxy, skip) in enumerate(zip(NTXYVInProof, SkippingN)):
    lambda_size = int(ntxy[1][1:])
    differences[lambda_size].append(ntxy[0] - skip[0])

# Bar plotting
bar_width = 0.25
index = np.arange(len(ts))

fig, ax = plt.subplots()
plt.grid(True, linestyle="--", axis='y', alpha=0.65)
for i, size in enumerate(BitSize):
    plt.bar(index + i * bar_width, differences[size], bar_width, color=colors[i], edgecolor = edgecolors[i],
            label=f"{size}", hatch=patterns[i])

plt.xlabel('Exponentiation ($\\tau$)',labelpad= 15, fontsize = 14)
plt.ylabel('Gas Savings ($10^4$)',labelpad= 7.5, fontsize = 14)
plt.xticks(index + bar_width, ts)
legend = plt.legend(title = "λ", loc='upper left',framealpha=0.2, edgecolor='black', prop={'size': 11.5})
legend.get_frame().set_linewidth(1.0)  # You can adjust the linewidth to your preference

plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, _):
    return '{:.0f}'.format(x * 1e-4)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(custom_formatter))
plt.yticks(fontsize=12)
plt.xticks(fontsize=13)

#plt.grid(True, linestyle="--")
plt.tight_layout()
plt.savefig('5. N diff.png', dpi=500)
plt.show()