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

# ------bit 2048
#   ---tau 20
#   gasUsed 3072101
#   gasUsed 3056491
#   gasUsed 3061265
#   gasUsed 3071581
#   gasUsed 3067929
#   averageGasUsed 3065873
#   averageCalldataSize in Bytes 8932
#   averageIntrinsicGas 128812
#   averageGasOfFuncDispatch 14627
#   averageHalvingGasUsed 3045807
#   averageModExpGasUsed 3743
#   ---tau 21
#   gasUsed 3230534
#   gasUsed 3232997
#   gasUsed 3225463
#   gasUsed 3236613
#   gasUsed 3233996
#   averageGasUsed 3231920
#   averageCalldataSize in Bytes 9316
#   averageIntrinsicGas 133429
#   averageGasOfFuncDispatch 15260
#   averageHalvingGasUsed 3211115
#   averageModExpGasUsed 3776
#   ---tau 22
#   gasUsed 3386746
#   gasUsed 3395529
#   gasUsed 3398717
#   gasUsed 3395552
#   gasUsed 3398741
#   averageGasUsed 3395057
#   averageCalldataSize in Bytes 9700
#   averageIntrinsicGas 138107
#   averageGasOfFuncDispatch 15894
#   averageHalvingGasUsed 3373512
#   averageModExpGasUsed 3807
#   ---tau 23
#   gasUsed 3559786
#   gasUsed 3563504
#   gasUsed 3544401
#   gasUsed 3573746
#   gasUsed 3567843
#   averageGasUsed 3561856
#   averageCalldataSize in Bytes 10084
#   averageIntrinsicGas 142758
#   averageGasOfFuncDispatch 16528
#   averageHalvingGasUsed 3539570
#   averageModExpGasUsed 3840
#   ---tau 24
#   gasUsed 3713151
#   gasUsed 3733208
#   gasUsed 3738834
#   gasUsed 3723215
#   gasUsed 3736251
#   averageGasUsed 3728931
#   averageCalldataSize in Bytes 10468
#   averageIntrinsicGas 147479
#   averageGasOfFuncDispatch 17163
#   averageHalvingGasUsed 3705905
#   averageModExpGasUsed 3872
#   ---tau 25
#   gasUsed 3894307
#   gasUsed 3887773
#   gasUsed 3894502
#   gasUsed 3904450
#   gasUsed 3907628
#   averageGasUsed 3897732
#   averageCalldataSize in Bytes 10852
#   averageIntrinsicGas 152070
#   averageGasOfFuncDispatch 17799
#   averageHalvingGasUsed 3873963
#   averageModExpGasUsed 3905

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import math
import numpy as np

x = ['20', '21', '22', '23', '24', '25']

y1CalldataSize = [8932, 9316, 9700, 10084, 10468, 10852]
y1CalldataSizeinKB = [i / 1024 for i in y1CalldataSize]
y2IntrinsicGas = [12.8812, 13.3429, 13.8107, 14.2758, 14.7479, 15.2070]

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


plt.xticks(fontsize=13)
plt.grid(True, linestyle="--")
plt.tight_layout()

plt.savefig('pietrzak2048IntrinsicAndCalldata.png', dpi=500)

plt.show()