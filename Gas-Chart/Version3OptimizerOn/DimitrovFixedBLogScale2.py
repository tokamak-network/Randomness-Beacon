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


# x^( 2^32 ) * y^(2^1)
# dimitrov estimateGasResult 214108n
# precompile estimateGasResult 82622n
# x^( 2^64 ) * y^(2^1)
# dimitrov estimateGasResult 308178n
# precompile estimateGasResult 93853n
# x^( 2^128 ) * y^(2^1)
# dimitrov estimateGasResult 503757n
# precompile estimateGasResult 115380n
# x^( 2^256 ) * y^(2^1)
# dimitrov estimateGasResult 925216n
# precompile estimateGasResult 159659n
# x^( 2^512 ) * y^(2^1)
# dimitrov estimateGasResult 1887832n
# precompile estimateGasResult 246707n
# x^( 2^1024 ) * y^(2^1)
# dimitrov estimateGasResult 4293516n
# precompile estimateGasResult 421799n
# x^( 2^2048 ) * y^(2^1)
# dimitrov estimateGasResult 11024365n
# precompile estimateGasResult 771858n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import FuncFormatter

x = ["$x^{2^{32}}  y^{2}$", "$x^{2^{64}}  y^{2}$", "$x^{2^{128}}  y^{2}$", "$x^{2^{256}}  y^{2}$", "$x^{2^{512}}  y^{2}$", "$x^{2^{1024}}  y^{2}$", "$x^{2^{2048}}  y^{2}$"]

dimitrov = [214108, 308178, 503757, 925216, 1887832, 4293516, 11024365]
precompile = [82622, 93853, 115380, 159659, 246707, 421799, 771858]

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