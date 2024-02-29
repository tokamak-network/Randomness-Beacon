// Copyright 2023 justin
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// import ReactJson from "react-json-view-with-toggle"
import dynamic from "next/dynamic"
import Header from "../components/Header"
import { createTestCaseV2 } from "../utils/testFunctions"
const ReactJson = dynamic(() => import("react-json-view-with-toggle"), {
    ssr: false,
})
//import ReactJson from "react-json-view-with-toggle"
export default function TestCase() {
    const setUpParams = createTestCaseV2()
    return (
        <>
            <Header />{" "}
            <div className="container text-lg mx-5 mt-3">
                <h1 className="text-2xl font-bold">Test Case Example</h1>
                <div className="my-2">
                    n g h T setupProofs randomList commitList omega recoveredOmega recoveryProofs
                </div>
                <ReactJson src={setUpParams} />
            </div>
        </>
    )
}
