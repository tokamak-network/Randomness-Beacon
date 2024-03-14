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

# x^( 2^400 )  y^( 2^400 )
# dimitrov estimateGasResult 1994600n
# precompile estimateGasResult 348906n
# x^( 2^800 )  y^( 2^800 )
# dimitrov estimateGasResult 4294433n
# precompile estimateGasResult 622752n
# x^( 2^1200 )  y^( 2^1200 )
# dimitrov estimateGasResult 7000468n
# precompile estimateGasResult 896840n
# x^( 2^1600 )  y^( 2^1600 )
# dimitrov estimateGasResult 10113683n
# precompile estimateGasResult 1170160n
# x^( 2^2000 )  y^( 2^2000 )
# dimitrov estimateGasResult 13632929n
# precompile estimateGasResult 1443521n
# x^( 2^2400 )  y^( 2^2400 )
# dimitrov estimateGasResult 17559539n
# precompile estimateGasResult 1717079n
# x^( 2^2800 )  y^( 2^2800 )
# dimitrov estimateGasResult 21892008n
# precompile estimateGasResult 1990466n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2^{400}}  y^{2^{400}}$", "$x^{2^{800}}  y^{2^{800}}$", "$x^{2^{1200}}  y^{2^{1200}}$", "$x^{2^{1600}}  y^{2^{1600}}$", "$x^{2^{2000}}  y^{2^{2000}}$", "$x^{2^{2400}}  y^{2^{2400}}$", "$x^{2^{2800}}  y^{2^{2800}}$"]

dimitrov = [1994600, 4294433, 7000468, 10113683, 13632929, 17559539, 21892008]
precompile = [348906, 622752, 896840, 1170160, 1443521, 1717079, 1990466]

colors = ['#ff0000','#0000ff']
markers = ['o', 's']

plt.plot(x, dimitrov, color=colors[0], marker=markers[0], label="Dimitrov")
plt.plot(x, precompile, color=colors[1], marker=markers[1], label="Precompile")

plt.legend()
plt.xlabel('Multi Exponentiation', labelpad= 15,  fontsize=13)
plt.ylabel('Gas Used ($10^7$)', labelpad= 15,  fontsize=13)

plt.gca().yaxis.get_offset_text().set_visible(False)
# plt.xticks(fontsize=11)
# margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.2)
plt.show()