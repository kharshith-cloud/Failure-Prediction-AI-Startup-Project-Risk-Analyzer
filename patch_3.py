import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix media queries
media_queries = '''        @media (max-width: 1024px) {
            .features-footer { grid-template-columns: 1fr 1fr !important; }
        }

        @media (max-width: 768px) {
            .hero h2 { font-size: 2.5rem; }
            .form-grid { grid-template-columns: 1fr; gap: 24px; }
            .analysis-section { padding: 32px 20px; }
            .workspace-container { border-radius: 16px; margin-bottom: 24px; }
            .features-footer { grid-template-columns: 1fr !important; }
            .hero-cta { width: 100%; }
        }'''

content = re.sub(
    r'@media\s*\(max-width:\s*1024px\).*?\.hero-cta\s*\{\s*width:\s*100%;\s*\}\s*\}',
    media_queries,
    content,
    flags=re.DOTALL
)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 3 applied successfully.")
