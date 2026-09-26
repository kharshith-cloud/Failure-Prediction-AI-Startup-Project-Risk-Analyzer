import re

with open('templates/result.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if the tracking logic exists
if '--mouse-x' not in content or 'document.addEventListener' not in content:
    js_tracking = """
          // Track mouse position for glass panel glow effect
          document.addEventListener('mousemove', (e) => {
              document.querySelectorAll('.glass-panel').forEach(el => {
                  const rect = el.getBoundingClientRect();
                  const x = ((e.clientX - rect.left) / rect.width) * 100;
                  const y = ((e.clientY - rect.top) / rect.height) * 100;
                  el.style.setProperty('--mouse-x', `${x}%`);
                  el.style.setProperty('--mouse-y', `${y}%`);
              });
          });
"""
    # Insert it right before the end of the script tag or inside an existing script tag
    script_end = r"      </script>\n  </body>"
    new_script_end = js_tracking + "      </script>\n  </body>"
    content = re.sub(script_end, new_script_end, content)
    
    with open('templates/result.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Patch 14 applied: Mouse tracking for glow added to result.html.")
