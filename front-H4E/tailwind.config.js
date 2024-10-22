/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#FFE1CC',
        primary: '#92D5C7',
        secondary: '#ecc94b',
        tertiary: '#332623',
      }
    },
  },
  plugins: [],
}