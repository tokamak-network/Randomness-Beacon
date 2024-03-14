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

# x^( 2^1 ) * y^( 2^1 )
# dimitrov estimateGasResult 105955n
# precompile estimateGasResult 76872n
# x^( 2^10 ) * y^( 2^10 )
# dimitrov estimateGasResult 144088n
# precompile estimateGasResult 83147n
# x^( 2^100 ) * y^( 2^100 )
# dimitrov estimateGasResult 536750n
# precompile estimateGasResult 144654n
# x^( 2^1000 ) * y^( 2^1000 )
# dimitrov estimateGasResult 5596400n
# precompile estimateGasResult 759158n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
x = ["$x^{2^1} * y^{2^1}$", "$x^{2^{10}} * y^{2^{10}}$", "$x^{2^{100}} * y^{2^{100}}$", "$x^{2^{1000}} * y^{2^{1000}}$"]

dimitrov = [105955, 144088, 536750, 5596400]
precompile = [76872, 83147, 144654, 759158]

colors = ['#ff0000','#0000ff']
markers = ['o', 's'] 

plt.plot(x, dimitrov, color=colors[0], marker=markers[0], label="Dimitrov")
plt.plot(x, precompile, color=colors[1], marker=markers[1], label="Precompile")

plt.legend()
plt.xlabel('Multi Exponentiation', labelpad= 15)
plt.ylabel('Gas Used', labelpad= 15)
# margin
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.15)
plt.show()