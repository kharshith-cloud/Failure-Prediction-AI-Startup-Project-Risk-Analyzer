import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the wrapper with the Vesper video wrapper
old_bg_html = r'<div class="persistent-background-wrapper" id="persistentBgWrapper">[\s\S]*?</div>\s*</div>'
# Actually, the div ends at </div>.
old_bg_html = r'<div class="persistent-background-wrapper" id="persistentBgWrapper">.*?</div>\s*<div class="grain-overlay"></div>\s*</div>'

# Let's just use replace using exact strings to be safe.
start_str = '<div class="persistent-background-wrapper" id="persistentBgWrapper">'
end_str = '<!-- Scrim to darken wave at the bottom of the page -->'

if start_str in content and end_str in content:
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    new_bg_html = """<!-- Vesper Video Background -->
    <div class="hero-photo" id="persistentBgWrapper">
        <video autoplay loop muted playsinline src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260818_072341_50851634-bbc3-4c33-9acc-7647d4db44aa.mp4"></video>
        <div class="gold-overlay"></div>
    </div>
    
    """
    
    content = content[:start_idx] + new_bg_html + content[end_idx:]

# 2. Update CSS
wrapper_css = r"        \.persistent-background-wrapper \{[\s\S]*?rgba\(214,168,79,0\.018\), transparent 50%\);\s*\}"

new_css = """        .hero-photo {
            position: fixed;
            inset: 0;
            z-index: -3;
            overflow: hidden;
            background: #000;
        }
        .hero-photo video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            opacity: 0.85; /* Slight dimming so UI pops */
        }
        .gold-overlay {
            position: absolute;
            inset: 0;
            background: rgba(214, 168, 79, 0.15); /* Gold shade */
            mix-blend-mode: color;
            pointer-events: none;
        }
        .gold-overlay::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(to bottom, transparent, #050608 95%);
        }"""
        
content = re.sub(wrapper_css, new_css, content)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 12 applied: Vesper Video Background Added with Gold Shade.")
