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

# x^( 2^2 )
# exp_by_square_iterative_gasestimate 66801n
# exp_by_square_and_multiply_gasestimate 40302n
# precompileModExpGasEstimate 34441n
# x^( 2^4 )
# exp_by_square_iterative_gasestimate 73603n
# exp_by_square_and_multiply_gasestimate 45744n
# precompileModExpGasEstimate 35135n
# x^( 2^8 )
# exp_by_square_iterative_gasestimate 87278n
# exp_by_square_and_multiply_gasestimate 57225n
# precompileModExpGasEstimate 36521n
# x^( 2^16 )
# exp_by_square_iterative_gasestimate 114614n
# exp_by_square_and_multiply_gasestimate 79736n
# precompileModExpGasEstimate 39144n
# x^( 2^32 )
# exp_by_square_iterative_gasestimate 169895n
# exp_by_square_and_multiply_gasestimate 125228n
# precompileModExpGasEstimate 44669n
# x^( 2^64 )
# exp_by_square_iterative_gasestimate 283000n
# exp_by_square_and_multiply_gasestimate 218087n
# precompileModExpGasEstimate 55505n
# x^( 2^128 )
# exp_by_square_iterative_gasestimate 519121n
# exp_by_square_and_multiply_gasestimate 411306n
# precompileModExpGasEstimate 77520n
# x^( 2^256 )
# exp_by_square_iterative_gasestimate 1032461n
# exp_by_square_and_multiply_gasestimate 827913n
# precompileModExpGasEstimate 121691n
# x^( 2^512 )
# exp_by_square_iterative_gasestimate 2250934n
# exp_by_square_and_multiply_gasestimate 1780996n
# precompileModExpGasEstimate 210694n
# x^( 2^1024 )
# exp_by_square_iterative_gasestimate 5427134n
# exp_by_square_and_multiply_gasestimate 4167310n
# precompileModExpGasEstimate 388551n
# x^( 2^2048 )
# exp_by_square_iterative_gasestimate 14735446n
# exp_by_square_and_multiply_gasestimate 10860551n
# precompileModExpGasEstimate 744152n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter
#x = ["$x^{2^2}$", "$x^{2^4}$", "$x^{2^8}$", "$x^{2^{16}}$", "$x^{2^{32}}$", "$x^{2^{64}}$", "$x^{2^{128}}$", "$x^{2^{256}}$", "$x^{2^{512}}$", "$x^{2^{1024}}$", "$x^{2^{2048}}$"]
x = ['2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048']
expBySquareIterative = [66801, 73603, 87278, 114614, 169895, 283000, 519121, 1032461, 2250934, 5427134, 14735446]
expBySquareAndMultiply = [40302, 45744, 57225, 79736, 125228, 218087, 411306, 827913, 1780996, 4167310, 10860551]
precompileModExp = [34441, 35135, 36521, 39144, 44669, 55505, 77520, 121691, 210694, 388551, 744152]


colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Baseline Model")
plt.plot(x, expBySquareAndMultiply, color=colors[1], marker=markers[1], label="Square And Multiply")
plt.plot(x, precompileModExp, color=colors[2], marker=markers[2], label="Precompile ModExp")

plt.legend(fontsize=17)
plt.xlabel('Exponentiation ($\\tau$ of $x^{2^\\tau}$)', fontsize=22.5)
plt.ylabel('Gas Used ($10^6$)', labelpad= 7, fontsize=21)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
x_numerical = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048])
plt.xticks(fontsize=16, rotation = 45)
plt.yticks(fontsize=17)
# margin
plt.grid(True, linestyle="--")
plt.tight_layout()
# Add text 'x^{2^t}' to the plot
# Adjust 'x_coord' and 'y_coord' to position the text appropriately
# x_coord = len(x) - 0.6  # Position at the end of the x-axis
# y_coord = min(min(expBySquareIterative), min(expBySquareAndMultiply), min(precompileModExp)) * -150  # Adjust this as needed
# plt.text(x_coord, y_coord, r'$x^{2^t}$', fontsize=15, ha='right', va='bottom')
plt.savefig('2. modexp(log).png', dpi=500)
plt.show()