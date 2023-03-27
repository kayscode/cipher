/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./chat/templates/chat/*.html",
      "./chat/templates/chat/**/*.html",
      "./templates/**/*.{html,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}