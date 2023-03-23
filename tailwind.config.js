/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./chat/templates/chat/*.{html,js}",
      "./chat/templates/chat/**/*.{html,js}",
      "./cipher/templates/**/*.{html,js}",
      "./templates/**/*.{html,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}