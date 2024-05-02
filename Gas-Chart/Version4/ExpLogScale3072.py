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
# exp_by_square_iterative_gasestimate 81245n
# exp_by_square_and_multiply_gasestimate 45652n
# precompileModExpGasEstimate 39362n
# x^( 2^4 )
# exp_by_square_iterative_gasestimate 88963n
# exp_by_square_and_multiply_gasestimate 52030n
# precompileModExpGasEstimate 40904n
# x^( 2^8 )
# exp_by_square_iterative_gasestimate 104501n
# exp_by_square_and_multiply_gasestimate 65391n
# precompileModExpGasEstimate 43988n
# x^( 2^16 )
# exp_by_square_iterative_gasestimate 135540n
# exp_by_square_and_multiply_gasestimate 91705n
# precompileModExpGasEstimate 50156n
# x^( 2^32 )
# exp_by_square_iterative_gasestimate 198847n
# exp_by_square_and_multiply_gasestimate 144963n
# precompileModExpGasEstimate 62735n
# x^( 2^64 )
# exp_by_square_iterative_gasestimate 328752n
# exp_by_square_and_multiply_gasestimate 254002n
# precompileModExpGasEstimate 87164n
# x^( 2^128 )
# exp_by_square_iterative_gasestimate 601384n
# exp_by_square_and_multiply_gasestimate 482172n
# precompileModExpGasEstimate 136508n
# x^( 2^256 )
# exp_by_square_iterative_gasestimate 1199250n
# exp_by_square_and_multiply_gasestimate 979056n
# precompileModExpGasEstimate 237165n
# x^( 2^512 )
# exp_by_square_iterative_gasestimate 2634720n
# exp_by_square_and_multiply_gasestimate 2134154n
# precompileModExpGasEstimate 437058n
# x^( 2^1024 )
# exp_by_square_iterative_gasestimate 6435140n
# exp_by_square_and_multiply_gasestimate 5090449n
# precompileModExpGasEstimate 836741n
# x^( 2^2048 )
# exp_by_square_iterative_gasestimate 17754157n
# exp_by_square_and_multiply_gasestimate 13587274n
# precompileModExpGasEstimate 1636849n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter
#x = ["$x^{2^2}$", "$x^{2^4}$", "$x^{2^8}$", "$x^{2^{16}}$", "$x^{2^{32}}$", "$x^{2^{64}}$", "$x^{2^{128}}$", "$x^{2^{256}}$", "$x^{2^{512}}$", "$x^{2^{1024}}$", "$x^{2^{2048}}$"]
x = ['2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048']
expBySquareIterative = [81245, 88963, 104501, 135540, 198847, 328752, 601384, 1199250, 2634720, 6435140, 17754157]
expBySquareAndMultiply = [45652, 52030, 65391, 91705, 144963, 254002, 482172, 979056, 2134154, 5090449, 13587274]
precompileModExp = [39362, 40904, 43988, 50156, 62735, 87164, 136508, 237165, 437058, 836741, 1636849]


colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Exponentiation by Squaring")
plt.plot(x, expBySquareAndMultiply, color=colors[1], marker=markers[1], label="Square and Multiply")
plt.plot(x, precompileModExp, color=colors[2], marker=markers[2], label="Precompile ModExp")

plt.legend(fontsize=13)
plt.xlabel('Exponentiation ($\\tau$ of $x^{2^\\tau}$)', fontsize=15)
plt.ylabel('Gas Used ($10^6$)', labelpad= 7, fontsize=15)
plt.gca().yaxis.get_offset_text().set_visible(False)
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
x_numerical = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048])
plt.xticks(fontsize=13, rotation = 45)
plt.yticks(fontsize=13)
# margin
plt.grid(True, linestyle="--")
plt.tight_layout()
# Add text 'x^{2^t}' to the plot
# Adjust 'x_coord' and 'y_coord' to position the text appropriately
# x_coord = len(x) - 0.6  # Position at the end of the x-axis
# y_coord = min(min(expBySquareIterative), min(expBySquareAndMultiply), min(precompileModExp)) * -150  # Adjust this as needed
# plt.text(x_coord, y_coord, r'$x^{2^t}$', fontsize=15, ha='right', va='bottom')
plt.savefig('2. modexp(log)3072.png', dpi=500)
plt.show()