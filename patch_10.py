import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the liquid canvas element
content = re.sub(r'<canvas class="liquid-canvas" id="liquidCanvas"></canvas>', '', content)

# 2. Update persistent wrapper to a premium static dark background
wrapper_css = r"        \.persistent-background-wrapper \{[\s\S]*?background: .*?;\s*\}"
new_wrapper_css = """        .persistent-background-wrapper {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -3;
            pointer-events: none;
            overflow: hidden;
            background: #050608;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(214,168,79,0.035), transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(100,130,180,0.025), transparent 60%),
                radial-gradient(circle at 50% 100%, rgba(214,168,79,0.018), transparent 50%);
        }"""
content = re.sub(wrapper_css, new_wrapper_css, content)

# 3. Remove the entire JS block for ORGANIC VOLUMETRIC FABRIC
js_block = r"// ORGANIC VOLUMETRIC FABRIC / LIQUID CANVAS IMPLEMENTATION[\s\S]*?\}\)\(\);"
content = re.sub(js_block, "", content)

# 4. Remove cursor light HTML if it exists
content = re.sub(r'<div class="cursor-light" id="cursorLight"></div>', '', content)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 10 applied: Motion background removed, static premium background restored.")
