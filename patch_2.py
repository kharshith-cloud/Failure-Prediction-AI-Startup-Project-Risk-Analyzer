import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Workspace Container and Sections CSS
workspace_css = """        .workspace-container {
            background: rgba(12, 17, 24, 0.78);
            border: 1px solid rgba(255, 255, 255, 0.10);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border-radius: 26px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.04);
            margin-bottom: 40px;
            overflow: hidden;
            position: relative;
        }

        .analysis-section {
            padding: 48px;
            background: rgba(255, 255, 255, 0.015);
            border-bottom: 1px solid rgba(255, 255, 255, 0.07);
            transition: all 0.4s ease;
        }
        
        .analysis-section:last-child {
            border-bottom: none;
        }

        .analysis-section:hover, .analysis-section:focus-within, .analysis-section.active-section {
            background: rgba(255, 255, 255, 0.035);
        }

        .section-header {
            display: flex;
            align-items: flex-start;
            margin-bottom: 40px;
            /* removed border-bottom from here, using section divider instead */
        }
"""
# Replace old .form-section CSS block
content = re.sub(
    r'\.form-section\s*\{.*?\.form-section:hover,\s*\.form-section:focus-within\s*\{[^}]*\}',
    workspace_css,
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'\.active-section \.section-num, \.form-section:hover \.section-num, \.form-section:focus-within \.section-num',
    '.active-section .section-num, .analysis-section:hover .section-num, .analysis-section:focus-within .section-num',
    content
)

# Remove `padding-bottom: 24px;` and `border-bottom: 1px solid var(--border-soft);` from `.section-header`
content = content.replace(
    'padding-bottom: 24px;\n            border-bottom: 1px solid var(--border-soft);',
    ''
)

# 2. Add feasibility card CSS
feasibility_card_css = """        .feasibility-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 24px;
            transition: all 0.3s ease;
        }
        .feasibility-card:hover {
            background: rgba(255, 255, 255, 0.05);
            border-color: rgba(214,168,79,0.25);
        }
        .range-track-container {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-top: 16px;
        }
        .range-min, .range-max {
            font-size: 0.75rem;
            color: var(--muted-dark);
            font-weight: 500;
        }
"""
content = content.replace('.range-header-wrapper {', feasibility_card_css + '        .range-header-wrapper {')

# 3. HTML Layout fixes
# Wrap forms inside `.workspace-container`
# First, change `<div class="form-section scroll-reveal">` to `<div class="analysis-section scroll-reveal">`
content = content.replace('<div class="form-section scroll-reveal">', '<div class="analysis-section scroll-reveal">')

# Inject <div class="workspace-container"> right after `<form action="/submit" method="POST" id="analysisForm" novalidate>`
content = content.replace('<form action="/submit" method="POST" id="analysisForm" novalidate>', '<form action="/submit" method="POST" id="analysisForm" novalidate>\n            <div class="workspace-container">')

# Close `.workspace-container` right before `<div class="cta-container">`
content = content.replace('<div class="cta-container">', '</div>\n            <div class="cta-container">')

# Replace JS observers
content = content.replace(".querySelectorAll('.form-section')", ".querySelectorAll('.analysis-section')")

# 4. Completely replace the Feasibility Assessment Grid
feasibility_html_old_pattern = r'<div class="form-grid-4">[\s\S]*?</div>\s*</div>\s*</div>\s*<div class="cta-container">'

def get_slider_html(name, label):
    return f'''                    <div class="feasibility-card">
                        <div class="range-header-wrapper">
                            <label style="margin: 0;">{label}</label>
                            <div class="range-value-box" id="{name}_val">50</div>
                        </div>
                        <div class="range-track-container">
                            <span class="range-min">0</span>
                            <input type="range" name="{name}" value="50" required min="0" max="100" class="feasibility-input" style="--range-val: 50%;" oninput="document.getElementById('{name}_val').innerText = this.value; this.style.setProperty('--range-val', this.value + '%');">
                            <span class="range-max">100</span>
                        </div>
                    </div>'''

feasibility_html_new = f'''                <div class="form-grid">
{get_slider_html("f_market", "Market Opportunity")}
{get_slider_html("f_team", "Team Capability")}
{get_slider_html("f_comp", "Competitive Advantage")}
{get_slider_html("f_res", "Resource Availability")}
                </div>
            </div>
            </div>
            <div class="cta-container">'''

content = re.sub(feasibility_html_old_pattern, feasibility_html_new, content)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 2 applied successfully.")
