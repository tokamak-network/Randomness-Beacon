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
import { Typography, Modal, TextArea } from "web3uikit"
export default function SetModal({
    editItem,
    isModalOpen,
    onClose,
    setValue,
    modalInputValue,
    setModalInputValue,
}) {
    return (
        <div>
            <div>
                <Modal
                    cancelText="Cancel"
                    id="v-center"
                    key="v-center"
                    isVisible={isModalOpen}
                    okText="Set"
                    onCancel={() => {
                        onClose()
                    }}
                    onCloseButtonPressed={() => {
                        onClose()
                    }}
                    onOk={() => {
                        setValue(modalInputValue)
                    }}
                    title={
                        <div style={{ display: "flex", gap: 10 }}>
                            <Typography color="#68738D" variant="h3">
                                Edit {editItem}
                            </Typography>
                        </div>
                    }
                >
                    <div className="mb-3" id="textareadiv">
                        <TextArea
                            id="textArea"
                            onChange={(e) => setModalInputValue(e.target.value)}
                            label={editItem}
                            width="100%"
                            value={modalInputValue}
                            placeholder="Object Value"
                        />
                    </div>
                </Modal>
            </div>
        </div>
    )
}
