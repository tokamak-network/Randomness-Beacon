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
#   x^2^2 33584 8219 3482
#   x^2^4 39471 12855 4165
#   x^2^8 51383 22715 5530
#   x^2^16 75312 41993 8261
#   x^2^32 123792 81019 13722
#   x^2^64 223256 160946 24645
#   x^2^128 432329 328301 46490
#   x^2^256 891014 693040 90190
#   x^2^512 2000687 1542539 177580
#   x^2^1024 4959023 3721685 352368
#   x^2^2048 13831600 10000578 701943

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter
#x = ["$x^{2^2}$", "$x^{2^4}$", "$x^{2^8}$", "$x^{2^{16}}$", "$x^{2^{32}}$", "$x^{2^{64}}$", "$x^{2^{128}}$", "$x^{2^{256}}$", "$x^{2^{512}}$", "$x^{2^{1024}}$", "$x^{2^{2048}}$"]
x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

expBySquareIterative = [33584, 39471, 51383, 75312, 123792, 223256, 432329, 891014, 2000687, 4959023, 13831600]
expBySquareAndMultiply = [8219, 12855, 22715, 41993, 81019, 160946, 328301, 693040, 1542539, 3721685, 10000578]
precompileModExp = [3482, 4165, 5530, 8261, 13722, 24645, 46490, 90190, 177580, 352368, 701943]


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
plt.savefig('2. modexp(log).png', dpi=500)
plt.show()