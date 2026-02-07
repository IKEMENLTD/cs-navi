
css_content = """

/* =========================================
   MOBILE MENU & RESPONSIVE FIXES
   ========================================= */

/* Hamburger Button (Default: Hidden) */
.hamburger-btn {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 20px;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 1001;
  padding: 0;
}

.hamburger-line {
  width: 100%;
  height: 2px;
  background-color: var(--n-text);
  border-radius: 2px;
  transition: all 0.3s ease;
}

/* Mobile Adjustments */
@media (max-width: 768px) {
  /* Show Hamburger */
  .hamburger-btn {
    display: flex;
  }

  /* Animate Hamburger to X */
  .hamburger-btn.active .hamburger-line:nth-child(1) {
    transform: translateY(9px) rotate(45deg);
  }
  .hamburger-btn.active .hamburger-line:nth-child(2) {
    opacity: 0;
  }
  .hamburger-btn.active .hamburger-line:nth-child(3) {
    transform: translateY(-9px) rotate(-45deg);
  }

  /* Mobile Navigation Drawer */
  .site-nav {
    position: fixed;
    top: 73px; /* Header height approx */
    left: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    flex-direction: column;
    align-items: center;
    padding: 2rem 1.5rem 3rem;
    gap: 1.5rem;
    border-bottom: 1px solid var(--n-glass-border);
    box-shadow: var(--n-shadow-lg);
    
    /* Animation State */
    opacity: 0;
    visibility: hidden;
    transform: translateY(-20px);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .site-nav.active {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  .nav-link {
    font-size: 1.2rem;
    padding: 0.5rem 0;
    width: 100%;
    text-align: center;
    border-bottom: 1px solid rgba(0,0,0,0.05);
  }
  .nav-link:last-child {
    border-bottom: none;
  }

  /* Adjust Hero Spacing */
  .hero-ranking-section {
    padding: 2rem 0;
  }
  
  .section-title {
    font-size: 1.8rem; /* Smaller title on mobile */
  }

  .ranking-grid {
    padding: 0 1rem;
    gap: 1.5rem;
  }
  
  /* Article Grid Spacing */
  .article-grid {
    padding: 2rem 1rem;
    gap: 1.5rem;
  }
  
  .search-filter-section {
    padding: 1.5rem 1rem;
  }
}
"""

with open(r'd:\cardloanmedia-b-2\assets\css\neo-style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
