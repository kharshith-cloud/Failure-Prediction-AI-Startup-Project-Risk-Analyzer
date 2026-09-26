import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean out the broken liquid canvas javascript safely
start_str = "// ========================================================\n        // ORGANIC VOLUMETRIC FABRIC / LIQUID CANVAS IMPLEMENTATION"
end_str = "// Form Submit & Loading State Logic"

if start_str in content and end_str in content:
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    # We remove everything between the start of the canvas logic and the start of the form logic
    content = content[:start_idx] + "\n        " + content[end_idx:]
else:
    print("Could not find exact markers for JS stripping.")

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 11 applied: Cleaned up broken JS.")
