import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove opaque background from html and put it on .persistent-background-wrapper instead (which is z-index: -3)
html_css = r"        html \{[\s\S]*?background-attachment: fixed !important;\s*\}"
new_html_css = """        html {
            scroll-behavior: smooth;
            background: transparent !important;
        }"""
content = re.sub(html_css, new_html_css, content)

# 2. Fix the Liquid Canvas CSS (remove mix-blend-mode: screen, lower blur)
liquid_canvas_css = r"        \.liquid-canvas \{[\s\S]*?will-change: transform;\s*\}"
new_liquid_canvas_css = """        .liquid-canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 120%; /* Extra height for parallax */
            z-index: 1;
            filter: blur(4px) contrast(1.1);
            opacity: 0.85;
            will-change: transform;
        }"""
content = re.sub(liquid_canvas_css, new_liquid_canvas_css, content)

# 3. Add background gradient to wrapper so the canvas sits beautifully
wrapper_css = r"        \.persistent-background-wrapper \{[\s\S]*?background: var\(--bg\);\s*\}"
new_wrapper_css = """        .persistent-background-wrapper {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -3;
            pointer-events: none;
            overflow: hidden;
            background: radial-gradient(circle at 50% 0%, #151005, #050608 60%);
        }"""
content = re.sub(wrapper_css, new_wrapper_css, content)

# 4. Modify the layers array to be rich gold and cover the whole screen vertically
old_layers = r"const layers = \[.*?\];"
new_layers = """const layers = [
              // Deepest ambient glow (Bronze/Gold) covering top
              { points: 5, speed: 0.00015, offset: 0, amp: 220, yPos: 0.25, 
                colors: ['#1A1308', '#0A0804', 'rgba(0,0,0,0)'] },
                
              // Upper midtone (Warm gold)
              { points: 7, speed: 0.00025, offset: 100, amp: 180, yPos: 0.45, 
                colors: ['#2A1D0B', '#1A1308', '#0A0804'] },
                
              // Main body (Rich Gold)
              { points: 6, speed: 0.0002, offset: 250, amp: 200, yPos: 0.60, 
                colors: ['#4A3B18', '#2A1D0B', '#110D05'] },
                
              // Bright highlight crest (Champagne/Gold)
              { points: 8, speed: 0.00035, offset: 50, amp: 150, yPos: 0.75, 
                colors: ['#9A7B32', '#4A3B18', '#2A1D0B'] },
                
              // Translucent gold vapor overlay near bottom
              { points: 5, speed: 0.0003, offset: 200, amp: 160, yPos: 0.85, 
                colors: ['rgba(214,168,79,0.15)', 'rgba(214,168,79,0.05)', 'rgba(0,0,0,0)'] }
          ];"""
content = re.sub(old_layers, new_layers, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 9 applied.")
