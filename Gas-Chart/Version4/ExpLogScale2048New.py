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

#   Exponentiation by Squaring, Square and Multiply, Precompile ModExp
#   x^2^2 32879 7555 2879
#   x^2^4 38645 12121 3562
#   x^2^8 50317 21611 4927
#   x^2^16 73767 40379 7658
#   x^2^32 121287 78385 13119
#   x^2^64 218830 156272 24042
#   x^2^128 424063 319547 45887
#   x^2^256 875069 676126 89587
#   x^2^512 1969381 1509305 176977
#   x^2^1024 4896997 3655811 351765
#   x^2^2048 13708135 9869424 701340

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter
#x = ["$x^{2^2}$", "$x^{2^4}$", "$x^{2^8}$", "$x^{2^{16}}$", "$x^{2^{32}}$", "$x^{2^{64}}$", "$x^{2^{128}}$", "$x^{2^{256}}$", "$x^{2^{512}}$", "$x^{2^{1024}}$", "$x^{2^{2048}}$"]
x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

expBySquareIterative = [32879, 38645, 50317, 73767, 121287, 218830, 424063, 875069, 1969381, 4896997, 13708135]
expBySquareAndMultiply = [7555, 12121, 21611, 40379, 78385, 156272, 319547, 676126, 1509305, 3655811, 9869424]
precompileModExp = [2879, 3562, 4927, 7658, 13119, 24042, 45887, 89587, 176977, 351765, 701340]


colors = ["tab:red", "tab:green", "tab:blue"]
markers = ['o', '^', 's']  # circle, triangle, square

plt.plot(x, expBySquareIterative, color=colors[0], marker=markers[0], label="Exponentiation by Squaring")
plt.plot(x, expBySquareAndMultiply, color=colors[1], marker=markers[1], label="Square and Multiply")
plt.plot(x, precompileModExp, color=colors[2], marker=markers[2], label="Precompile ModExp")

plt.legend(fontsize=13)
plt.xlabel('Exponentiation ($\\tau$ of $x^{2^{2^\\tau}}$)', fontsize=16)
plt.ylabel('Gas Used ($10^6$)', labelpad= 7, fontsize=15.5)
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
plt.savefig('modexp-2048.png', dpi=500)
plt.show()