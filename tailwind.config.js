/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'brand-brown': '#6b4f4b',
        'brand-light-brown': '#a07c6e',
        'brand-cream': '#fff4e6',
        'brand-accent': '#ffb04f',
        'brand-dark': '#3c2f2f',
      },
      fontFamily: {
        'heading': ['"Playfair Display"', 'serif'],
        'body': ['"Lato"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
