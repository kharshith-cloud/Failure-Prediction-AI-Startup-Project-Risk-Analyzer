import re

with open('templates/result.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the liquid canvas wrapper with the Vesper video background
start_str_bg = '<div class="persistent-background-wrapper" id="persistentBgWrapper">'
end_str_bg = '<!-- Scrim to darken wave at the bottom of the page -->'

if start_str_bg in content and end_str_bg in content:
    start_idx = content.find(start_str_bg)
    end_idx = content.find(end_str_bg)
    
    new_bg_html = """<!-- Vesper Video Background -->
    <div class="hero-photo" id="persistentBgWrapper">
        <video autoplay loop muted playsinline src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260818_072341_50851634-bbc3-4c33-9acc-7647d4db44aa.mp4"></video>
        <div class="gold-overlay"></div>
    </div>
    
    """
    content = content[:start_idx] + new_bg_html + content[end_idx:]

# 2. Add the video CSS
css_injection = """
        .hero-photo {
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
            opacity: 0.85;
        }
        .gold-overlay {
            position: absolute;
            inset: 0;
            background: rgba(214, 168, 79, 0.15);
            mix-blend-mode: color;
            pointer-events: none;
        }
        .gold-overlay::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(to bottom, transparent, #050608 95%);
        }
"""
# We'll just replace the old persistent-background-wrapper CSS
old_bg_css = r"/\* \s*========================================================\s*LIQUID FABRIC AGENT WAVE \(PERSISTENT BACKGROUND\)\s*========================================================\s*\*/[\s\S]*?mix-blend-mode: screen;\s*\}"
content = re.sub(old_bg_css, css_injection, content)

# 3. Add glow effects to .glass-panel
glass_panel_css = r"        \.glass-panel \{[\s\S]*?overflow: hidden;\s*\}"
new_glass_panel_css = """        .glass-panel {
            background: rgba(15, 20, 28, 0.70);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 20px;
            padding: 36px;
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.04);
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }
        
        .glass-panel::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(
                circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
                rgba(214,168,79,0.10),
                transparent 45%
            );
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 0;
            pointer-events: none;
        }
        
        .glass-panel > * {
            position: relative;
            z-index: 1;
        }
        """
content = re.sub(glass_panel_css, new_glass_panel_css, content)

glass_panel_hover = r"        \.glass-panel\.scroll-reveal\.visible:hover \{[\s\S]*?transition: all 0\.25s ease;\s*\}"
new_glass_panel_hover = """        .glass-panel.scroll-reveal.visible:hover {
            transform: translateY(-4px);
            border-color: rgba(214,168,79,0.4);
            background: rgba(19, 24, 32, 0.92);
            box-shadow: 0 25px 70px rgba(0,0,0,0.35), 0 0 35px rgba(214,168,79,0.16), inset 0 1px 0 rgba(255,255,255,0.05);
            transition: all 0.4s ease;
        }
        .glass-panel:hover::before {
            opacity: 1;
        }"""
content = re.sub(glass_panel_hover, new_glass_panel_hover, content)

# 4. Remove liquid canvas JS block
js_start = "// ORGANIC VOLUMETRIC FABRIC / LIQUID CANVAS IMPLEMENTATION"
js_end = "// Form Submit & Loading State Logic" # Wait, result.html doesn't have form submit!
# Let's see what result.html has at the end of the script

with open('templates/result.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 13 generated.")
