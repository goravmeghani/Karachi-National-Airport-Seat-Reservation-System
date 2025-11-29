import React from 'react';

const cookies = [
  {
    name: 'Classic Chocolate Chip',
    description: 'The timeless classic, packed with rich chocolate chunks.',
    price: '$2.50',
    emoji: '🍪',
  },
  {
    name: 'Oatmeal Raisin',
    description: 'A chewy delight with a hint of cinnamon and sweet raisins.',
    price: '$2.25',
    emoji: '😋',
  },
  {
    name: 'Double Fudge Brownie',
    description: 'Decadently rich and fudgy, for the ultimate chocolate lover.',
    price: '$3.00',
    emoji: '🍫',
  },
  {
    name: 'Snickerdoodle',
    description: 'Soft, chewy, and coated in a delicious cinnamon-sugar mix.',
    price: '$2.25',
    emoji: '✨',
  }
];

const testimonials = [
  {
    quote: "These are hands down the best cookies I've ever had. The Chocolate Chip is pure perfection!",
    name: 'Sarah J.',
  },
  {
    quote: "I order from The Cookie Jar Co. every week for my office. Everyone loves them!",
    name: 'Michael B.',
  },
];

function App() {
  return (
    <div className="bg-brand-cream min-h-screen">
      
      {/* Header */}
      <header className="bg-brand-brown/80 backdrop-blur-sm sticky top-0 z-10">
        <div className="container mx-auto px-6 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-heading font-bold text-brand-cream">The Cookie Jar Co.</h1>
          <nav className="hidden md:flex space-x-8">
            <a href="#our-cookies" className="text-brand-cream hover:text-brand-accent transition-colors">Our Cookies</a>
            <a href="#about-us" className="text-brand-cream hover:text-brand-accent transition-colors">About Us</a>
            <a href="#contact" className="text-brand-cream hover:text-brand-accent transition-colors">Contact</a>
          </nav>
        </div>
      </header>

      <main>
        {/* Hero Section */}
        <section className="text-center py-20 px-6 bg-brand-light-brown text-brand-dark">
          <div className="container mx-auto">
            <h2 className="text-6xl font-heading font-black text-brand-dark mb-4">Baked with Love.</h2>
            <p className="text-xl mb-8 max-w-2xl mx-auto">Experience the unforgettable taste of our artisanal cookies, made from scratch with the finest ingredients.</p>
            <a href="#our-cookies" className="bg-brand-accent text-brand-dark font-bold py-3 px-8 rounded-full hover:bg-yellow-500 transition-transform transform hover:scale-105">Discover Our Flavors</a>
          </div>
        </section>

        {/* Featured Cookies Section */}
        <section id="our-cookies" className="py-20">
          <div className="container mx-auto px-6">
            <h3 className="text-4xl font-heading font-bold text-center mb-12 text-brand-dark">Our Signature Cookies</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
              {cookies.map((cookie, index) => (
                <div key={index} className="bg-white rounded-lg shadow-lg p-6 text-center transform hover:-translate-y-2 transition-transform">
                  <span className="text-6xl mb-4 inline-block">{cookie.emoji}</span>
                  <h4 className="text-xl font-bold font-heading mb-2 text-brand-brown">{cookie.name}</h4>
                  <p className="text-brand-light-brown mb-4">{cookie.description}</p>
                  <p className="text-lg font-bold text-brand-accent">{cookie.price}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* About Us Section */}
        <section id="about-us" className="py-20 bg-white">
          <div className="container mx-auto px-6">
            <div className="flex flex-col md:flex-row items-center gap-12">
              <div className="md:w-1/2">
                <h3 className="text-4xl font-heading font-bold mb-4 text-brand-dark">Our Story</h3>
                <p className="text-brand-light-brown mb-4">
                  The Cookie Jar Co. started in a small kitchen with a big dream: to create the world's most delicious cookies. We believe in the power of a simple, well-made treat to bring joy to everyday moments.
                </p>
                <p className="text-brand-light-brown">
                  Using family recipes passed down through generations, we pour our heart into every batch, ensuring each cookie is as perfect as the last.
                </p>
              </div>
              <div className="md:w-1/2">
                <div className="bg-brand-cream rounded-lg p-8 shadow-md">
                   <p className="text-9xl text-center">🍪</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Testimonials Section */}
        <section className="py-20">
          <div className="container mx-auto px-6">
            <h3 className="text-4xl font-heading font-bold text-center mb-12 text-brand-dark">What Our Customers Say</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
              {testimonials.map((testimonial, index) => (
                <div key={index} className="bg-brand-brown/10 p-6 rounded-lg">
                  <p className="text-brand-dark italic mb-4">"{testimonial.quote}"</p>
                  <p className="font-bold text-right text-brand-brown">- {testimonial.name}</p>
                </div>
              ))}
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer id="contact" className="bg-brand-dark text-brand-cream py-12">
        <div className="container mx-auto px-6 text-center">
          <h3 className="text-2xl font-heading font-bold mb-4">The Cookie Jar Co.</h3>
          <p className="mb-4">123 Cookie Lane, Bakerville, CA 90210</p>
          <p className="mb-4">hello@thecookiejar.co</p>
          <div className="flex justify-center space-x-6 mb-8">
            <a href="#" className="hover:text-brand-accent">Facebook</a>
            <a href="#" className="hover:text-brand-accent">Instagram</a>
            <a href="#" className="hover:text-brand-accent">Twitter</a>
          </div>
          <p className="text-sm text-brand-light-brown">&copy; {new Date().getFullYear()} The Cookie Jar Co. All Rights Reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
