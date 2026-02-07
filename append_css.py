
css_content = """

/* =========================================
   GLOSSARY STYLES (Neo Theme Integration)
   ========================================= */
.glossary-hero {
  background: linear-gradient(135deg, var(--n-primary) 0%, var(--n-primary-dark) 100%);
  padding: 4rem 1.5rem;
  text-align: center;
  color: white;
  margin-bottom: 2rem;
  border-radius: 0 0 var(--n-radius-xl) var(--n-radius-xl);
  box-shadow: var(--n-shadow-lg);
}

.glossary-hero h1 {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
}

.glossary-hero p {
  font-size: 1.1rem;
  opacity: 0.9;
}

.glossary-nav {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  padding: 1rem 0;
  position: sticky;
  top: 70px;
  z-index: 900;
  border-bottom: 1px solid var(--n-glass-border);
  box-shadow: var(--n-shadow-sm);
}

.glossary-nav-inner {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem;
}

.glossary-nav a {
  padding: 0.5rem 1.25rem;
  background: white;
  border-radius: 99px;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--n-text);
  text-decoration: none;
  border: 1px solid transparent;
  box-shadow: var(--n-shadow-sm);
  transition: all 0.2s;
}

.glossary-nav a:hover {
  background: var(--n-primary);
  color: white;
  transform: translateY(-2px);
  box-shadow: var(--n-shadow-md);
}

.glossary-content {
  padding: 3rem 1.5rem;
  max-width: 900px;
  margin: 0 auto;
}

.glossary-section {
  margin-bottom: 4rem;
  scroll-margin-top: 140px;
}

.glossary-section-title {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--n-primary);
  padding-bottom: 0.5rem;
  border-bottom: 3px solid var(--n-primary);
  margin-bottom: 2rem;
  display: inline-block;
}

.glossary-item {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(5px);
  border: 1px solid white;
  border-radius: var(--n-radius-lg);
  padding: 2rem;
  margin-bottom: 1.5rem;
  transition: all 0.3s;
  box-shadow: var(--n-shadow-sm);
}

.glossary-item:hover {
  background: white;
  transform: translateY(-3px);
  box-shadow: var(--n-shadow-md);
  border-color: var(--n-primary);
}

.glossary-term {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--n-text);
  margin-bottom: 0.5rem;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 1rem;
}

.glossary-term-reading {
  font-size: 0.9rem;
  color: var(--n-text-muted);
  font-weight: 400;
}

.glossary-definition {
  font-size: 1rem;
  color: var(--n-text);
  line-height: 1.8;
}

.glossary-tag {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: rgba(59, 130, 246, 0.1);
  color: var(--n-primary);
  font-size: 0.8rem;
  font-weight: 700;
  border-radius: 99px;
  margin-top: 1rem;
}

/* =========================================
   FAQ STYLES (Neo Theme Integration)
   ========================================= */
.faq-hero {
  background: linear-gradient(135deg, var(--n-accent) 0%, #d97706 100%);
  padding: 4rem 1.5rem;
  text-align: center;
  color: white;
  margin-bottom: 2rem;
  border-radius: 0 0 var(--n-radius-xl) var(--n-radius-xl);
  box-shadow: var(--n-shadow-lg);
}

.faq-hero h1 {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
}

.faq-hero p {
  font-size: 1.1rem;
  opacity: 0.95;
}

.faq-nav {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  padding: 1rem 0;
  position: sticky;
  top: 70px;
  z-index: 900;
  border-bottom: 1px solid var(--n-glass-border);
  box-shadow: var(--n-shadow-sm);
}

.faq-nav-inner {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem;
}

.faq-nav a {
  padding: 0.5rem 1.25rem;
  background: white;
  border-radius: 99px;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--n-text);
  text-decoration: none;
  border: 1px solid transparent;
  box-shadow: var(--n-shadow-sm);
  transition: all 0.2s;
}

.faq-nav a:hover {
  background: var(--n-accent);
  color: white;
  transform: translateY(-2px);
  box-shadow: var(--n-shadow-md);
}

.faq-content {
  padding: 3rem 1.5rem;
  max-width: 900px;
  margin: 0 auto;
}

.faq-section {
  margin-bottom: 4rem;
  scroll-margin-top: 140px;
}

.faq-section-title {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--n-text);
  padding-bottom: 0.5rem;
  border-bottom: 3px solid var(--n-accent);
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.faq-section-title svg {
  width: 32px; height: 32px;
  color: var(--n-accent);
}

.faq-item {
  background: white;
  border: 1px solid var(--n-glass-border);
  border-radius: var(--n-radius-lg);
  margin-bottom: 1rem;
  overflow: hidden;
  transition: all 0.3s;
  box-shadow: var(--n-shadow-sm);
}

.faq-item:hover {
  box-shadow: var(--n-shadow-md);
  border-color: var(--n-accent);
}

.faq-question {
  width: 100%;
  padding: 1.5rem 2rem;
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  text-align: left;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--n-text);
  transition: color 0.2s;
}

.faq-question:hover {
  color: var(--n-primary);
}

.faq-question::before {
  content: 'Q';
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px; height: 36px;
  background: linear-gradient(135deg, var(--n-accent) 0%, #d97706 100%);
  color: white;
  border-radius: 50%;
  font-weight: 800;
  flex-shrink: 0;
  box-shadow: 0 4px 10px rgba(245, 158, 11, 0.3);
}

.faq-question-text { flex: 1; }

.faq-toggle {
  width: 24px; height: 24px;
  color: var(--n-text-muted);
  transition: transform 0.3s;
}

.faq-item.active .faq-toggle {
  transform: rotate(180deg);
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  background: rgba(240, 244, 248, 0.5);
}

.faq-item.active .faq-answer {
  max-height: 1000px;
}

.faq-answer-inner {
  padding: 0 2rem 2rem 5rem;
}

.faq-answer-inner p {
  margin-bottom: 1rem;
  line-height: 1.8;
  color: var(--n-text);
}

.faq-answer-inner ul {
  padding-left: 1.5rem;
  margin-bottom: 1rem;
}

.faq-answer-inner li {
  margin-bottom: 0.5rem;
  color: var(--n-text-muted);
}

.faq-highlight {
  background: white;
  border-left: 4px solid var(--n-accent);
  padding: 1rem 1.5rem;
  border-radius: 0 12px 12px 0;
  margin-top: 1.5rem;
  box-shadow: var(--n-shadow-sm);
}

.faq-highlight p { margin: 0; font-weight: 600; color: var(--n-text); }

/* Responsive adjustments for Glossary & FAQ */
@media (max-width: 768px) {
  .glossary-hero, .faq-hero { padding: 3rem 1rem; border-radius: 0 0 20px 20px; }
  .glossary-hero h1, .faq-hero h1 { font-size: 2rem; }
  .glossary-content, .faq-content { padding: 2rem 1rem; }
  .glossary-item { padding: 1.5rem; }
  .glossary-term { font-size: 1.2rem; }
  
  .faq-question { padding: 1.25rem; gap: 1rem; font-size: 1rem; }
  .faq-answer-inner { padding: 0 1.25rem 1.5rem 1.25rem; }
  .faq-question::before { width: 30px; height: 30px; font-size: 0.9rem; }
}
"""

with open(r'd:\cardloanmedia-b-2\assets\css\neo-style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
