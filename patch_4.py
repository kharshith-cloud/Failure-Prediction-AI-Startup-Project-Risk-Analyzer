import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the visual styling from workspace-container, turning it into just a layout wrapper
new_workspace_css = """        .workspace-container {
            margin-bottom: 40px;
            position: relative;
        }

        .analysis-section {
            background: rgba(15, 19, 26, 0.82);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 22px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.28);
            padding: 48px;
            margin-bottom: 40px;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
        }
        
        .analysis-section:last-child {
            margin-bottom: 0;
        }

        .analysis-section:hover {
            box-shadow: 0 25px 70px rgba(0,0,0,0.35), 0 0 35px rgba(214,168,79,0.16), inset 0 1px 0 rgba(255,255,255,0.05);
            transform: translateY(-4px);
            background: rgba(19, 24, 32, 0.92);
            border-color: rgba(214,168,79,0.4);
        }

        .analysis-section.active-card {
            border: 1px solid rgba(242,201,107,0.75);
            box-shadow: 0 25px 80px rgba(0,0,0,0.40), 0 0 45px rgba(214,168,79,0.22), inset 0 1px 0 rgba(242,201,107,0.08);
            background: rgba(19, 24, 32, 0.92);
            transform: translateY(-4px);
        }

        .section-header {
            display: flex;
            align-items: flex-start;
            margin-bottom: 40px;
        }
"""
content = re.sub(r'        \.workspace-container\s*\{.*?\.section-header\s*\{[^}]*\}', new_workspace_css, content, flags=re.DOTALL)

# Update Section Num CSS
new_section_num_css = """        .section-num {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: rgba(214,168,79,0.07);
            border: 1px solid rgba(214,168,79,0.28);
            font-size: 1.125rem;
            color: #D6A84F;
            font-weight: 500;
            transition: all 0.4s ease;
        }

        .analysis-section:hover .section-num, .analysis-section.active-card .section-num {
            background: rgba(214,168,79,0.13);
            border-color: rgba(242,201,107,0.65);
            box-shadow: 0 0 22px rgba(214,168,79,0.28);
            color: #F2C96B;
            text-shadow: 0 0 10px rgba(214,168,79,0.5);
        }
"""
content = re.sub(r'        \.section-num\s*\{.*?text-shadow:[^}]*\}\s*\}', new_section_num_css, content, flags=re.DOTALL)

# Add Active Card click logic to JavaScript
active_card_js = """
        // Card Click Active State Logic
        document.querySelectorAll('.analysis-section').forEach(section => {
            section.addEventListener('click', function() {
                document.querySelectorAll('.analysis-section').forEach(s => s.classList.remove('active-card'));
                this.classList.add('active-card');
            });
        });
        
        // Ensure intersection observer doesn't override manual active-card clicks if not wanted,
        // or just let it exist alongside (we are using .active-card now for strong gold states)
"""
content = content.replace("// Feasibility Range Visualizer Logic", active_card_js + "\n        // Feasibility Range Visualizer Logic")

# Clean up CSS media queries for workspace container since it no longer has background/border
content = content.replace(".workspace-container { border-radius: 16px; margin-bottom: 24px; }", ".workspace-container { margin-bottom: 24px; }")

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 4 generated and applied.")
