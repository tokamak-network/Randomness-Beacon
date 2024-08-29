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

#  ---tau 20
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
import matplotlib.lines as mlines
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter

#  calldataSizeInBytes, IntrinsicGas
data = [
    [ 8932, 128812 ],
    [ 9316, 133429 ],
    [ 9700, 138107 ],
    [ 10084, 142758 ],
    [ 10468, 147479 ],
    [ 10852, 152070 ]
]

labels = ['calldata size (Bytes)', 'Intrinsic Gas']
colors = ['tab:red','tab:blue']
markers = ['o', '^', 's']  # circle, triangle, square
ts = ["$2^{20}$", "$2^{21}$", "$2^{22}$", "$2^{23}$", "$2^{24}$", "$2^{25}$"]
lineStyles = ['-', '--']

x = ts
y1 = [data[i][0] for i in range(0,6)]
y2 = [data[i][1] for i in range(0,6)]


#Define the width of the bars
bar_width = 0.2

# Set the positions of the bars and labels on the X axis
index = np.arange(len(labels))

# Create the figure and the two axes
fig, ax_gas = plt.subplots()

ax_gas.bar(index - 1.5*bar_width, y1, bar_width, label='Calldata Size (Bytes)', color=colors[0])
ax_gas.bar(index - 0.5*bar_width, y2, bar_width, label='Intrinsic Gas', hatch='xx', color=colors[1], edgecolor='black')

# Set the labels, title, and custom x-axis tick labels, etc.
ax_gas.set_xlabel('Exponentiation (τ)')



# fig, ax1 = plt.subplots()
# ax1.bar(x, y1, color=colors[0], label=labels[0])

# ax2 = ax1.twinx()
# ax2.bar(x, y2, color=colors[1], label=labels[1])


plt.show()