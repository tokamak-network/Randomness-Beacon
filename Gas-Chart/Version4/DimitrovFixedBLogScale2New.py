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

#   Dimitrov MultiExp Precompile MultiExp
#   x^2^2 * y^(2^1) 86918 33122
#   x^2^4 * y^(2^1) 91620 33724
#   x^2^8 * y^(2^1) 101018 35080
#   x^2^16 * y^(2^1) 120241 37823
#   x^2^32 * y^(2^1) 159315 43306
#   x^2^64 * y^(2^1) 239309 54169
#   x^2^128 * y^(2^1) 406668 76003
#   x^2^256 * y^(2^1) 771330 119757
#   x^2^512 * y^(2^1) 1620875 207096
#   x^2^1024 * y^(2^1) 3800056 381931
#   x^2^2048 * y^(2^1) 10079163 731495

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter

# x = ["$x^{2^{32}}  y^{2}$", "$x^{2^{64}}  y^{2}$", "$x^{2^{128}}  y^{2}$", "$x^{2^{256}}  y^{2}$", "$x^{2^{512}}  y^{2}$", "$x^{2^{1024}}  y^{2}$", "$x^{2^{2048}}  y^{2}$"]
x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

dimitrov = [86918, 91620, 101018, 120241, 159315, 239309, 406668, 771330, 1620875, 3800056, 10079163]
precompile = [33122, 33724, 35080, 37823, 43306, 54169, 76003, 119757, 207096, 381931, 731495]

colors = ["tab:red", "tab:blue"]
markers = ['o', 's']

plt.plot(x, dimitrov, color=colors[0], marker=markers[0], label="Dimitrov")
plt.plot(x, precompile, color=colors[1], marker=markers[1], label="Precompile")

plt.legend(fontsize=13)
plt.xlabel('Multi Exponentiation ($\\tau$ of ${x^{2^{2^\\tau}}}{y^{2}}$)',  fontsize=16)
plt.ylabel('Gas Used ($10^6$)', labelpad= 7,fontsize=15.5)

# Turn off the offset text and add a custom text annotation
plt.xticks(fontsize=13, rotation = 45)
plt.yticks(fontsize=13)
plt.gca().yaxis.get_offset_text().set_visible(False)
# plt.text(0, 1.01, '$10^7$', transform=plt.gca().transAxes, va='bottom')
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
# margin
plt.grid(True, linestyle="--")
# # Adjust the size of the figure
# fig_size = plt.gcf().get_size_inches() # Get current size
# fig_size[0] += 0.1 # Increase width by 1 inch (you can adjust this value as needed)
# plt.gcf().set_size_inches(fig_size) # Set new size
plt.tight_layout()
plt.savefig('Dimitrov-2048.png', dpi=500)
plt.show()