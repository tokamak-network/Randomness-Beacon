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


# x^( 2^32 )  y^(2)
# dimitrov estimateGasResult 234620n
# precompile estimateGasResult 85318n
# x^( 2^64 )  y^(2)
# dimitrov estimateGasResult 345955n
# precompile estimateGasResult 96736n
# x^( 228 )  y^(2)
# dimitrov estimateGasResult 575536n
# precompile estimateGasResult 118096n
# x^( 2^256 )  y^(2)
# dimitrov estimateGasResult 1063563n
# precompile estimateGasResult 162552n
# x^( 2^512 )  y^(2)
# dimitrov estimateGasResult 2150881n
# precompile estimateGasResult 249378n
# x^( 2024 )  y^(2)
# dimitrov estimateGasResult 4779288n
# precompile estimateGasResult 424522n
# x^( 2^2048 )  y^(2)
# dimitrov estimateGasResult 11840116n
# precompile estimateGasResult 774621n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter

x = ["$x^{2^{32}}  y^{2}$", "$x^{2^{64}}  y^{2}$", "$x^{2^{128}}  y^{2}$", "$x^{2^{256}}  y^{2}$", "$x^{2^{512}}  y^{2}$", "$x^{2^{1024}}  y^{2}$", "$x^{2^{2048}}  y^{2}$"]

dimitrov = [234620, 345955, 575536, 1063563, 2150881, 4779288, 11840116]
precompile = [85318, 96736, 118096, 162552, 249378, 424522, 774621]

colors = ['#ff0000','#0000ff']
markers = ['o', 's']

plt.plot(x, dimitrov, color=colors[0], marker=markers[0], label="Dimitrov")
plt.plot(x, precompile, color=colors[1], marker=markers[1], label="Precompile")

plt.legend(fontsize=13)
plt.xlabel('Multi Exponentiation', labelpad= 15, fontsize=13)
plt.ylabel('Gas Used ($10^6$)', labelpad= 15, fontsize=13)

# Turn off the offset text and add a custom text annotation
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().yaxis.get_offset_text().set_visible(False)
# plt.text(0, 1.01, '$10^7$', transform=plt.gca().transAxes, va='bottom')
def custom_formatter(x, pos):
    return '{:.0f}'.format(x * 1e-6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
# margin
plt.subplots_adjust(left=0.17)
plt.subplots_adjust(bottom=0.2)
plt.grid(True, linestyle="--")
plt.savefig('3. modexp(Dimitrov).png', dpi=500)
plt.show()