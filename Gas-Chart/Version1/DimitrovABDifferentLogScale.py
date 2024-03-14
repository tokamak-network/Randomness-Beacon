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

# x^( 2^2 ) * y^( 2^1 )
# dimitrov estimateGasResult 137219n
# precompile estimateGasResult 76688n
# x^( 2^4 ) * y^( 2^2 )
# dimitrov estimateGasResult 145607n
# precompile estimateGasResult 78809n
# x^( 2^8 ) * y^( 2^4 )
# dimitrov estimateGasResult 162532n
# precompile estimateGasResult 80487n
# x^( 2^16 ) * y^( 2^8 )
# dimitrov estimateGasResult 197504n
# precompile estimateGasResult 84430n
# x^( 2^32 ) * y^( 2^16 )
# dimitrov estimateGasResult 265642n
# precompile estimateGasResult 92147n
# x^( 2^64 ) * y^( 2^32 )
# dimitrov estimateGasResult 405463n
# precompile estimateGasResult 108900n
# x^( 2^128 ) * y^( 2^64 )
# dimitrov estimateGasResult 692622n
# precompile estimateGasResult 141862n
# x^( 2^256 ) * y^( 2^128 )
# dimitrov estimateGasResult 1299525n
# precompile estimateGasResult 207422n
# x^( 2^512 ) * y^( 2^256 )
# dimitrov estimateGasResult 2636271n
# precompile estimateGasResult 337990n
# x^( 2^1024 ) * y^( 2^512 )
# dimitrov estimateGasResult 5810733n
# precompile estimateGasResult 600990n
# x^( 2^2048 ) * y^( 2^1024 )
# dimitrov estimateGasResult 14164068n
# precompile estimateGasResult 1126002n

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

x = ["$x^{2^2} * y^{2^1}$", "$x^{2^4} * y^{2^2}$", "$x^{2^8} * y^{2^4}$", "$x^{2^{16}} * y^{2^8}$", "$x^{2^{32}} * y^{2^{16}}$", "$x^{2^{64}} * y^{2^{32}}$", "$x^{2^{128}} * y^{2^{64}}$", "$x^{2^{256}} * y^{2^{128}}$", "$x^{2^{512}} * y^{2^{256}}$", "$x^{2^{1024}} * y^{2^{512}}$", "$x^{2^{2048}} * y^{2^{1024}}$"]

dimitrov = [137219, 145607, 162532, 197504, 265642, 405463, 692622, 1299525, 2636271, 5810733, 14164068]
precompile = [76688, 78809, 80487, 84430, 92147, 108900, 141862, 207422, 337990, 600990, 1126002]

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