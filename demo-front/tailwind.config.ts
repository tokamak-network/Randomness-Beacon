import headlessuiPlugin from "@headlessui/tailwindcss"
import { type Config } from "tailwindcss"
module.exports = {
    content: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
    theme: {
        container: {
            center: true,
        },
        //extend: {},
    },
    plugins: [headlessuiPlugin],
}
