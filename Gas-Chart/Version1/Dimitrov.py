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

# x^( 2^1 ) * y^(2^1)
# dimitrov estimateGasResult 102587n
# precompile estimateGasResult 75242n
# x^( 2^10 ) * y^(2^1)
# dimitrov estimateGasResult 160156n
# precompile estimateGasResult 78353n
# x^( 2^100 ) * y^(2^1)
# dimitrov estimateGasResult 474059n
# precompile estimateGasResult 108553n
# x^( 2^1000 ) * y^(2^1)
# dimitrov estimateGasResult 4641495n
# precompile estimateGasResult 416079n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
x = ["$x^{2^1} * y^{2^1}$", "$x^{2^{10}} * y^{2^1}$", "$x^{2^{100}} * y^{2^1}$", "$x^{2^{1000}} * y^{2^1}$"]

dimitrov = [102587, 160156, 474059, 4641495]
precompile = [75242, 78353, 108553, 416079]

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