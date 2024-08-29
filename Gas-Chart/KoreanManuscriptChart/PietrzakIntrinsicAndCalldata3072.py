# Copyright 2024 justin
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#   ------bit 3072
#   ---tau 20
#   gasUsed 5765762
#   gasUsed 5772588
#   gasUsed 5773846
#   gasUsed 5774039
#   gasUsed 5763993
#   averageGasUsed 5770045
#   averageCalldataSize in Bytes 11876
#   averageIntrinsicGas 176074
#   averageGasOfFuncDispatch 15295
#   averageHalvingGasUsed 5748268
#   averageModExpGasUsed 4831
#   ---tau 21
#   gasUsed 6055248
#   gasUsed 6052088
#   gasUsed 6083059
#   gasUsed 6066047
#   gasUsed 6080941
#   averageGasUsed 6067476
#   averageCalldataSize in Bytes 12388
#   averageIntrinsicGas 182744
#   averageGasOfFuncDispatch 15963
#   averageHalvingGasUsed 6044922
#   averageModExpGasUsed 4868
#   ---tau 22
#   gasUsed 6377204
#   gasUsed 6389607
#   gasUsed 6371198
#   gasUsed 6374008
#   gasUsed 6385761
#   averageGasUsed 6379555
#   averageCalldataSize in Bytes 12900
#   averageIntrinsicGas 189398
#   averageGasOfFuncDispatch 16632
#   averageHalvingGasUsed 6356221
#   averageModExpGasUsed 4906
#   ---tau 23
#   gasUsed 6659386
#   gasUsed 6697633
#   gasUsed 6677365
#   gasUsed 6659504
#   gasUsed 6665063
#   averageGasUsed 6671790
#   averageCalldataSize in Bytes 13412
#   averageIntrinsicGas 196205
#   averageGasOfFuncDispatch 17301
#   averageHalvingGasUsed 6647679
#   averageModExpGasUsed 4943
#   ---tau 24
#   gasUsed 7004507
#   gasUsed 6977064
#   gasUsed 6995866
#   gasUsed 6975676
#   gasUsed 6980111
#   averageGasUsed 6986644
#   averageCalldataSize in Bytes 13924
#   averageIntrinsicGas 202950
#   averageGasOfFuncDispatch 17972
#   averageHalvingGasUsed 6961752
#   averageModExpGasUsed 4981
#   ---tau 25
#   gasUsed 7320781
#   gasUsed 7295986
#   gasUsed 7282791
#   gasUsed 7281868
#   gasUsed 7309385
#   averageGasUsed 7298162
#   averageCalldataSize in Bytes 14436
#   averageIntrinsicGas 209604
#   averageGasOfFuncDispatch 18644
#   averageHalvingGasUsed 7272487
#   averageModExpGasUsed 5020

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import math
import numpy as np

x = ['20', '21', '22', '23', '24', '25']

y1CalldataSize = [11876, 12388, 12900, 13412, 13924, 14436]
y1CalldataSizeinKB = [i / 1024 for i in y1CalldataSize]
y2IntrinsicGas = [17.6074, 18.2744, 18.9398, 19.6205, 20.2950, 20.9604]

fig, ax1 = plt.subplots()
bar_width = 0.3 # Adjust the bar width
index = np.arange(len(x))
bars = ax1.bar(index - 0.5*bar_width, y1CalldataSizeinKB, width=bar_width, edgecolor='tab:blue')

ax1.set_xticks(index)
ax1.set_xticklabels(x)
ax1.margins(x=0.1)



ax1.set_xlabel('$τ$', fontsize=16)
ax1.set_ylabel('Calldata Size (KB)', labelpad= 7, fontsize=15.5)
ax1.yaxis.set_tick_params(labelsize=13)
fig.gca().yaxis.get_offset_text().set_visible(False)
# def custom_formatter(x, pos):
#     return '{:.0f}'.format(x * 1e-3)
# ax1.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

ax2 = ax1.twinx()
ax2.yaxis.set_tick_params(labelsize=13)
bar_width = 0.3
ax2.bar(index + 0.5*bar_width, y2IntrinsicGas, width=bar_width, color='tab:green', hatch='///', edgecolor='black')

ax2.set_ylabel('Intrinsic Gas ($10^4$)', labelpad= 7, fontsize=15.5)
# Custom formatter to remove decimal points
ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))

plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.grid(True, linestyle="--")
plt.tight_layout()

plt.savefig('pietrzak3072IntrinsicAndCalldata.png', dpi=500)

plt.show()