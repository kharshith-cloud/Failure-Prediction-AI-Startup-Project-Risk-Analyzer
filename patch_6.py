import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Re-introduce scroll reveal logic to analysis-section
reveal_css = """        .analysis-section {
            background: rgba(15, 19, 26, 0.82);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 22px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.28);
            padding: 48px;
            margin-bottom: 40px;
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden; /* for radial gradient */
            opacity: 0;
            transform: translateY(20px);
        }
        
        .analysis-section.visible {
            opacity: 1;
            transform: translateY(0);
        }
"""

content = re.sub(r'        \.analysis-section\s*\{.*?overflow: hidden;\s*/\* for radial gradient \*/\s*\}\n', reveal_css, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 6 applied.")
