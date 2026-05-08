from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML Template with embedded CSS/JS for single file
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Samosa Junction - Crispy Outside, Legendary Inside</title>
    <meta name="description" content="Premium handmade samosas with authentic Indian flavors. Fresh ingredients, 25+ varieties, fast delivery in Bardhaman. Order now!">
    
    <!-- SEO Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Restaurant",
        "name": "Samosa Junction",
        "description": "Premium handmade samosas with authentic Indian flavors",
        "telephone": "+919876543210",
        "email": "hello@samosajunction.com",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "GT Road",
            "addressLocality": "Bardhaman",
            "addressRegion": "West Bengal",
            "addressCountry": "India"
        },
        "servesCuisine": "Indian Street Food",
        "priceRange": "$$"
    }
    </script>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        saffron: '#FF9933',
                        cream: '#FFF8E7',
                        deepbrown: '#3D2B1F',
                        gold: '#FFD700'
                    }
                }
            }
        }
    </script>

    <!-- GSAP -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * { font-family: 'Inter', sans-serif; }
        h1,h2,h3 { font-family: 'Playfair Display', serif; }
        
        .glass { 
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .gradient-bg {
            background: linear-gradient(135deg, #FF9933 0%, #F4A261 50%, #E76F51 100%);
        }
        
        .samosa-pattern {
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(255,255,255,0.1) 1px, transparent 1px),
                radial-gradient(circle at 80% 20%, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 50px 50px;
        }
        
        .dark .glass { background: rgba(0,0,0,0.3); }
        .dark { color-scheme: dark; }
        
        .floating-whatsapp {
            position: fixed;
            width: 60px;
            height: 60px;
            bottom: 40px;
            right: 40px;
            background: #25D366;
            color: #FFF;
            border-radius: 50px;
            text-align: center;
            font-size: 30px;
            box-shadow: 2px 2px 20px rgba(0,0,0,0.3);
            z-index: 1000;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        
        .menu-card {
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform: translateY(20px);
            opacity: 0;
        }
        
        .menu-card:hover {
            transform: translateY(-15px) scale(1.02);
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
        }
        
        .hero-bg {
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
                        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 800'%3E%3Crect fill='%23FF9933' width='1200' height='800'/%3E%3Ccircle fill='%23FFD700' opacity='0.3' cx='200' cy='200' r='150'/%3E%3Ccircle fill='%23E76F51' opacity='0.2' cx='1000' cy='600' r='200'/%3E%3Cpath fill='%23F4A261' opacity='0.4' d='M300 500Q400 450 500 500T700 500'/%3E%3C/svg%3E");
            background-size: cover;
            background-position: center;
        }
    </style>
</head>
<body class="bg-cream dark:bg-deepbrown text-deepbrown dark:text-cream overflow-x-hidden">
    
    <!-- Loading Animation -->
    <div id="loader" class="fixed inset-0 bg-gradient-to-r from-saffron to-gold z-[9999] flex items-center justify-center">
        <div class="w-16 h-16 border-4 border-white border-t-transparent border-saffron rounded-full animate-spin"></div>
    </div>

    <!-- Sticky Navbar -->
    <nav class="fixed top-0 w-full z-50 glass backdrop-blur-xl px-6 py-4 transition-all duration-300">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <div class="text-2xl font-bold bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">
                Samosa Junction
            </div>
            <ul class="hidden md:flex space-x-8">
                <li><a href="#home" class="hover:text-saffron transition-colors">Home</a></li>
                <li><a href="#about" class="hover:text-saffron transition-colors">About</a></li>
                <li><a href="#menu" class="hover:text-saffron transition-colors">Menu</a></li>
                <li><a href="#testimonials" class="hover:text-saffron transition-colors">Reviews</a></li>
                <li><a href="#contact" class="hover:text-saffron transition-colors">Contact</a></li>
            </ul>
            <div class="flex items-center space-x-4">
                <button id="theme-toggle" class="p-2 rounded-full hover:bg-white/20 transition-all">
                    <span class="dark:hidden">🌙</span>
                    <span class="hidden dark:inline">☀️</span>
                </button>
                <a href="https://wa.me/919876543210" class="bg-saffron text-white px-6 py-2 rounded-full font-semibold hover:bg-gold transition-all">Order Now</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="min-h-screen hero-bg flex items-center justify-center text-center text-white px-6 pt-20 samosa-pattern">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-5xl md:text-7xl font-bold mb-6 animate-fade-in-up">India's Favourite<br>Handmade Samosas</h1>
            <p class="text-xl md:text-2xl mb-12 max-w-2xl mx-auto opacity-90 leading-relaxed">
                Crispy Outside, Legendary Inside. Fresh ingredients, authentic spices, 
                handcrafted with love every single day.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <a href="https://wa.me/919876543210" class="bg-white text-deepbrown px-10 py-4 rounded-full font-semibold text-lg hover:bg-gold hover:scale-105 transition-all shadow-2xl">Order Now</a>
                <a href="#menu" class="border-2 border-white text-white px-10 py-4 rounded-full font-semibold text-lg hover:bg-white hover:text-deepbrown transition-all">Explore Menu</a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-32 px-6 bg-gradient-to-b from-cream to-white dark:from-deepbrown dark:to-gray-900">
        <div class="max-w-6xl mx-auto text-center">
            <h2 class="text-5xl md:text-6xl font-bold mb-12 bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">Our Story</h2>
            <div class="grid md:grid-cols-2 gap-16 items-center">
                <div class="space-y-8">
                    <p class="text-xl leading-relaxed max-w-lg">
                        From the bustling streets of Bardhaman to your table. Every samosa is handcrafted 
                        using traditional family recipes passed down through generations. 
                        We use only the freshest ingredients and authentic spices.
                    </p>
                    <div class="grid grid-cols-3 gap-8 pt-8">
                        <div class="text-center group">
                            <div class="text-4xl font-bold text-saffron group-hover:scale-110 transition-all">10K+</div>
                            <div class="text-sm opacity-75 mt-2">Happy Customers</div>
                        </div>
                        <div class="text-center group">
                            <div class="text-4xl font-bold text-saffron group-hover:scale-110 transition-all">25+</div>
                            <div class="text-sm opacity-75 mt-2">Samosa Varieties</div>
                        </div>
                        <div class="text-center group">
                            <div class="text-4xl font-bold text-saffron group-hover:scale-110 transition-all">Daily</div>
                            <div class="text-sm opacity-75 mt-2">Freshly Made</div>
                        </div>
                    </div>
                </div>
                <div class="relative">
                    <div class="glass p-12 rounded-3xl shadow-2xl menu-card">
                        <div class="w-64 h-64 bg-gradient-to-br from-saffron to-orange-500 rounded-2xl mx-auto mb-6"></div>
                        <h3 class="text-2xl font-bold mb-4">Handcrafted Perfection</h3>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Menu Section -->
    <section id="menu" class="py-32 px-6 samosa-pattern bg-gradient-to-b from-white to-cream dark:from-gray-900 dark:to-deepbrown">
        <div class="max-w-6xl mx-auto text-center">
            <h2 class="text-5xl md:text-6xl font-bold mb-20 bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">Our Menu</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="glass p-8 rounded-3xl cursor-pointer menu-card hover:shadow-2xl group">
                    <div class="w-full h-48 bg-gradient-to-br from-orange-400 to-orange-600 rounded-2xl mb-6 group-hover:scale-110 transition-all"></div>
                    <h3 class="text-2xl font-bold mb-3 group-hover:text-saffron transition-all">Classic Aloo Samosa</h3>
                    <p class="opacity-75 mb-4">Spiced potatoes with traditional Indian masala</p>
                    <div class="text-2xl font-bold text-saffron">₹25</div>
                </div>
                <div class="glass p-8 rounded-3xl cursor-pointer menu-card hover:shadow-2xl group">
                    <div class="w-full h-48 bg-gradient-to-br from-pink-400 to-pink-600 rounded-2xl mb-6 group-hover:scale-110 transition-all"></div>
                    <h3 class="text-2xl font-bold mb-3 group-hover:text-saffron transition-all">Paneer Tikka Samosa</h3>
                    <p class="opacity-75 mb-4">Smoky marinated paneer with tikka spices</p>
                    <div class="text-2xl font-bold text-saffron">₹35</div>
                </div>
                <div class="glass p-8 rounded-3xl cursor-pointer menu-card hover:shadow-2xl group">
                    <div class="w-full h-48 bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-2xl mb-6 group-hover:scale-110 transition-all"></div>
                    <h3 class="text-2xl font-bold mb-3 group-hover:text-saffron transition-all">Cheese Corn Samosa</h3>
                    <p class="opacity-75 mb-4">Creamy cheese and sweet corn filling</p>
                    <div class="text-2xl font-bold text-saffron">₹30</div>
                </div>
                <div class="glass p-8 rounded-3xl cursor-pointer menu-card hover:shadow-2xl group">
                    <div class="w-full h-48 bg-gradient-to-br from-red-400 to-red-600 rounded-2xl mb-6 group-hover:scale-110 transition-all"></div>
                    <h3 class="text-2xl font-bold mb-3 group-hover:text-saffron transition-all">Chicken Keema Samosa</h3>
                    <p class="opacity-75 mb-4">Spicy minced chicken with aromatic spices</p>
                    <div class="text-2xl font-bold text-saffron">₹40</div>
                </div>
                <div class="glass p-8 rounded-3xl cursor-pointer menu-card hover:shadow-2xl group">
                    <div class="w-full h-48 bg-gradient-to-br from-purple-400 to-purple-600 rounded-2xl mb-6 group-hover:scale-110 transition-all"></div>
                    <h3 class="text-2xl font-bold mb-3 group-hover:text-saffron transition-all">Chocolate Dessert Samosa</h3>
                    <p class="opacity-75 mb-4">Crispy shell with molten chocolate center</p>
                    <div class="text-2xl font-bold text-saffron">₹45</div>
                </div>
                <div class="glass p-8 rounded-3xl cursor-pointer menu-card hover:shadow-2xl group md:col-span-2 lg:col-span-1">
                    <div class="w-full h-48 bg-gradient-to-br from-green-400 to-green-600 rounded-2xl mb-6 group-hover:scale-110 transition-all"></div>
                    <h3 class="text-2xl font-bold mb-3 group-hover:text-saffron transition-all">Mini Party Samosas</h3>
                    <p class="opacity-75 mb-4">Assorted mini samosas for celebrations (20 pcs)</p>
                    <div class="text-2xl font-bold text-saffron">₹350</div>
                </div>
            </div>
            <div class="mt-20">
                <a href="https://wa.me/919876543210" class="bg-gradient-to-r from-saffron to-gold text-white px-12 py-5 rounded-full font-bold text-xl hover:shadow-2xl hover:scale-105 transition-all">Order on WhatsApp</a>
            </div>
        </div>
    </section>

    <!-- Special Features -->
    <section class="py-32 px-6 bg-gradient-to-b from-cream to-white dark:from-deepbrown dark:to-gray-900">
        <div class="max-w-6xl mx-auto text-center">
            <h2 class="text-5xl md:text-6xl font-bold mb-20 bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">Why Choose Us?</h2>
            <div class="grid md:grid-cols-5 gap-8">
                <div class="glass p-8 rounded-3xl hover:scale-105 transition-all">
                    <div class="w-16 h-16 bg-saffron rounded-2xl flex items-center justify-center mx-auto mb-6 text-2xl">🥬</div>
                    <h3 class="font-bold text-xl mb-4">Fresh Ingredients</h3>
                    <p class="opacity-75">Sourced daily from local markets</p>
                </div>
                <div class="glass p-8 rounded-3xl hover:scale-105 transition-all">
                    <div class="w-16 h-16 bg-gold rounded-2xl flex items-center justify-center mx-auto mb-6 text-2xl">🧼</div>
                    <h3 class="font-bold text-xl mb-4">Hygienic Kitchen</h3>
                    <p class="opacity-75">World-class hygiene standards</p>
                </div>
                <div class="glass p-8 rounded-3xl hover:scale-105 transition-all">
                    <div class="w-16 h-16 bg-saffron rounded-2xl flex items-center justify-center mx-auto mb-6 text-2xl">🚀</div>
                    <h3 class="font-bold text-xl mb-4">Fast Delivery</h3>
                    <p class="opacity-75">Hot & crispy at your door</p>
                </div>
                <div class="glass p-8 rounded-3xl hover:scale-105 transition-all">
                    <div class="w-16 h-16 bg-gold rounded-2xl flex items-center justify-center mx-auto mb-6 text-2xl">🇮🇳</div>
                    <h3 class="font-bold text-xl mb-4">Authentic Taste</h3>
                    <p class="opacity-75">Traditional family recipes</p>
                </div>
                <div class="glass p-8 rounded-3xl hover:scale-105 transition-all">
                    <div class="w-16 h-16 bg-saffron rounded-2xl flex items-center justify-center mx-auto mb-6 text-2xl">🎉</div>
                    <h3 class="font-bold text-xl mb-4">Event Catering</h3>
                    <p class="opacity-75">Perfect for all celebrations</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section id="testimonials" class="py-32 px-6 samosa-pattern bg-gradient-to-b from-white to-cream dark:from-gray-900 dark:to-deepbrown">
        <div class="max-w-4xl mx-auto text-center">
            <h2 class="text-5xl md:text-6xl font-bold mb-20 bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">What People Say</h2>
            <div class="glass p-12 rounded-3xl relative overflow-hidden">
                <div class="flex transition-transform duration-500 ease-in-out" id="testimonial-carousel">
                    <div class="min-w-full text-center p-8">
                        <div class="w-24 h-24 bg-saffron rounded-full mx-auto mb-8 flex items-center justify-center text-3xl">⭐⭐⭐⭐⭐</div>
                        <p class="text-xl italic mb-6">"Best samosas I've ever had! The paneer tikka one is addictive."</p>
                        <div class="font-bold text-saffron">Priya S.</div>
                    </div>
                    <div class="min-w-full text-center p-8">
                        <div class="w-24 h-24 bg-saffron rounded-full mx-auto mb-8 flex items-center justify-center text-3xl">⭐⭐⭐⭐⭐</div>
                        <p class="text-xl italic mb-6">"Perfect for parties! Everyone loved the mini samosas."</p>
                        <div class="font-bold text-saffron">Rahul M.</div>
                    </div>
                    <div class="min-w-full text-center p-8">
                        <div class="w-24 h-24 bg-saffron rounded-full mx-auto mb-8 flex items-center justify-center text-3xl">⭐⭐⭐⭐⭐</div>
                        <p class="text-xl italic mb-6">"Chocolate samosa blew my mind! Must try dessert."</p>
                        <div class="font-bold text-saffron">Anita K.</div>
                    </div>
                </div>
                <button class="absolute left-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 p-3 rounded-full transition-all" onclick="prevTestimonial()">❮</button>
                <button class="absolute right-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 p-3 rounded-full transition-all" onclick="nextTestimonial()">❯</button>
            </div>
        </div>
    </section>

    <!-- Gallery Section -->
    <section class="py-32 px-6 bg-gradient-to-b from-cream to-white dark:from-deepbrown dark:to-gray-900">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-5xl md:text-6xl font-bold mb-12 text-center bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">Gallery</h2>
            <div class="columns-1 sm:columns-2 lg:columns-3 gap-4 space-y-4">
                <div class="bg-gradient-to-br from-orange-400 to-orange-600 rounded-2xl h-64 group hover:scale-105 transition-all shadow-lg"></div>
                <div class="bg-gradient-to-br from-pink-400 to-pink-600 rounded-2xl h-64 group hover:scale-105 transition-all shadow-lg"></div>
                <div class="bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-2xl h-80 group hover:scale-105 transition-all shadow-lg"></div>
                <div class="bg-gradient-to-br from-red-400 to-red-600 rounded-2xl h-64 group hover:scale-105 transition-all shadow-lg"></div>
                <div class="bg-gradient-to-br from-purple-400 to-purple-600 rounded-2xl h-72 group hover:scale-105 transition-all shadow-lg"></div>
                <div class="bg-gradient-to-br from-green-400 to-green-600 rounded-2xl h-56 group hover:scale-105 transition-all shadow-lg"></div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-32 px-6 bg-gradient-to-b from-white to-cream dark:from-gray-900 dark:to-deepbrown">
        <div class="max-w-6xl mx-auto grid lg:grid-cols-2 gap-16">
            <div>
                <h2 class="text-5xl md:text-6xl font-bold mb-12 bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">Get In Touch</h2>
                <div class="space-y-6">
                    <div class="flex items-start space-x-4 p-6 glass rounded-2xl">
                        <div class="w-12 h-12 bg-saffron rounded-xl flex items-center justify-center text-xl mt-1">📞</div>
                        <div>
                            <h3 class="font-bold text-xl">Phone</h3>
                            <a href="tel:+919876543210" class="text-saffron font-semibold hover:underline">+91 98765 43210</a>
                        </div>
                    </div>
                    <div class="flex items-start space-x-4 p-6 glass rounded-2xl">
                        <div class="w-12 h-12 bg-saffron rounded-xl flex items-center justify-center text-xl mt-1">✉️</div>
                        <div>
                            <h3 class="font-bold text-xl">Email</h3>
                            <a href="mailto:hello@samosajunction.com" class="text-saffron font-semibold hover:underline">hello@samosajunction.com</a>
                        </div>
                    </div>
                    <div class="flex items-start space-x-4 p-6 glass rounded-2xl">
                        <div class="w-12 h-12 bg-saffron rounded-xl flex items-center justify-center text-xl mt-1">📍</div>
                        <div>
                            <h3 class="font-bold text-xl">Address</h3>
                            <div>GT Road, Bardhaman<br>West Bengal, India</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="glass p-8 rounded-3xl">
                <h3 class="text-3xl font-bold mb-8">Send us a message</h3>
                <form class="space-y-6">
                    <input type="text" placeholder="Your Name" class="w-full p-4 rounded-xl border-2 border-white/30 focus:border-saffron focus:outline-none bg-white/50 dark:bg-black/30 transition-all">
                    <input type="tel" placeholder="Phone" class="w-full p-4 rounded-xl border-2 border-white/30 focus:border-saffron focus:outline-none bg-white/50 dark:bg-black/30 transition-all">
                    <input type="email" placeholder="Email" class="w-full p-4 rounded-xl border-2 border-white/30 focus:border-saffron focus:outline-none bg-white/50 dark:bg-black/30 transition-all">
                    <textarea placeholder="Message" rows="5" class="w-full p-4 rounded-xl border-2 border-white/30 focus:border-saffron focus:outline-none bg-white/50 dark:bg-black/30 transition-all resize-none"></textarea>
                    <button type="submit" class="w-full bg-gradient-to-r from-saffron to-gold text-white py-4 px-8 rounded-xl font-bold text-lg hover:scale-105 transition-all shadow-lg">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-deepbrown text-cream py-12 px-6">
        <div class="max-w-6xl mx-auto grid md:grid-cols-4 gap-8 text-center md:text-left">
            <div>
                <div class="text-3xl font-bold mb-4 bg-gradient-to-r from-saffron to-gold bg-clip-text text-transparent">Samosa Junction</div>
                <p class="opacity-75">Crispy Outside, Legendary Inside</p>
            </div>
            <div>
                <h4 class="font-bold text-lg mb-4">Quick Links</h4>
                <ul class="space-y-2">
                    <li><a href="#home" class="hover:text-saffron transition-colors">Home</a></li>
                    <li><a href="#menu" class="hover:text-saffron transition-colors">Menu</a></li>
                    <li><a href="#about" class="hover:text-saffron transition-colors">About</a></li>
                    <li><a href="#contact" class="hover:text-saffron transition-colors">Contact</a></li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-lg mb-4">Business Hours</h4>
                <ul class="space-y-2 opacity-75">
                    <li>Mon-Sat: 10AM - 10PM</li>
                    <li>Sunday: 11AM - 9PM</li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-lg mb-4">Follow Us</h4>
                <div class="flex justify-center md:justify-start space-x-4">
                    <a href="#" class="w-10 h-10 bg-saffron rounded-xl flex items-center justify-center hover:scale-110 transition-all">📸</a>
                    <a href="#" class="w-10 h-10 bg-saffron rounded-xl flex items-center justify-center hover:scale-110 transition-all">📱</a>
                    <a href="#" class="w-10 h-10 bg-saffron rounded-xl flex items-center justify-center hover:scale-110 transition-all">🐦</a>
                </div>
            </div>
        </div>
        <div class="border-t border-white/20 mt-12 pt-8 text-center opacity-75">
            © 2024 Samosa Junction. All rights reserved.
        </div>
    </footer>

    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/919876543210" class="floating-whatsapp z-50" title="Order on WhatsApp">
        <div class="flex items-center justify-center h-full">💬</div>
    </a>

    <script>
        // GSAP Registration
        gsap.registerPlugin(ScrollTrigger);

        // Loading Animation
        window.addEventListener('load', () => {
            document.getElementById('loader').style.opacity = '0';
            setTimeout(() => document.getElementById('loader').remove(), 500);
        });

        // Smooth Animations
        gsap.from('.animate-fade-in-up', {
            scrollTrigger: '.animate-fade-in-up',
            y: 50,
            opacity: 0,
            duration: 1,
            ease: 'power3.out'
        });

        // Menu Cards Animation
        gsap.utils.toArray('.menu-card').forEach((card, i) => {
            gsap.from(card, {
                scrollTrigger: {
                    trigger: card,
                    start: 'top 80%'
                },
                y: 50,
                opacity: 0,
                duration: 0.8,
                delay: i * 0.1,
                ease: 'power3.out'
            });
        });

        // Theme Toggle
        const themeToggle = document.getElementById('theme-toggle');
        themeToggle.addEventListener('click', () => {
            document.documentElement.classList.toggle('dark');
            localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
        });

        // Load saved theme
        if (localStorage.getItem('theme') === 'dark') {
            document.documentElement.classList.add('dark');
        }

        // Testimonial Carousel
        let currentTestimonial = 0;
        const testimonials = document.querySelectorAll('#testimonial-carousel > div');
        
        function nextTestimonial() {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            document.getElementById('testimonial-carousel').style.transform = `translateX(-${currentTestimonial * 100}%)`;
        }
        
        function prevTestimonial() {
            currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
            document.getElementById('testimonial-carousel').style.transform = `translateX(-${currentTestimonial * 100}%)`;
        }

        // Navbar scroll effect
        window.addEventListener('scroll', () => {
            const navbar = document.querySelector('nav');
            if (window.scrollY > 100) {
                navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            } else {
                navbar.classList.remove('backdrop-blur-xl');
                navbar.style.background = 'rgba(255, 255, 255, 0.1)';
            }
        });

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("🚀 Samosa Junction Website Server Starting...")
    print("🌐 Visit: http://localhost:5000")
    print("📱 Fully responsive • Premium animations • SEO optimized")
    app.run(debug=True, host='0.0.0.0', port=5000)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Samosa website running"}
