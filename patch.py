import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add hero badge
hero_badge = '''
        <section class="hero">
            <div style="display:inline-flex; align-items:center; gap:8px; padding:6px 14px; background: rgba(214,168,79,0.08); border: 1px solid rgba(214,168,79,0.3); border-radius: 99px; margin-bottom: 24px;">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="var(--gold-primary)"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"></path></svg>
                <span style="font-size: 0.75rem; color: var(--gold-primary); font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;">AI-Powered Risk Intelligence</span>
            </div>
'''
content = content.replace('<section class="hero">', hero_badge)

# Update section headers
sections = [
    ("01", "Project Overview", "Basic information about your project and its core value proposition."),
    ("02", "Business Context", "Market conditions, industry, resources, competition, and project objectives."),
    ("03", "Risk Intelligence", "Evaluate the key factors that influence project risk."),
    ("04", "Feasibility Assessment", "Estimate the project's feasibility across key dimensions.")
]

for num, title, subtitle in sections:
    old_header = f'''                <div class="section-header">
                    <span class="section-num">{num}</span>
                    <h3 class="section-title">{title}</h3>
                </div>'''
    old_header2 = f'''                <div class="section-header">
                    <span class="section-num">{num}</span>
                    <h3 class="section-title">Feasibility</h3>
                </div>'''
    
    new_header = f'''                <div class="section-header">
                    <div class="section-badge-wrapper"><span class="section-num">{num}</span></div>
                    <div class="section-titles">
                        <h3 class="section-title">{title}</h3>
                        <p class="section-subtitle">{subtitle}</p>
                    </div>
                </div>'''
    content = content.replace(old_header, new_header)
    content = content.replace(old_header2, new_header)

# SVGs for inputs
svg_coins = '<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4C7 4 3 5.5 3 7c0 1.5 4 3 9 3s9-1.5 9-3c0-1.5-4-3-9-3Z"/><path d="M3 7v10c0 1.5 4 3 9 3s9-1.5 9-3V7"/><path d="M3 12c0 1.5 4 3 9 3s9-1.5 9-3"/></svg>'
svg_users = '<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
svg_doc = '<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>'
svg_bars = '<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>'
svg_target = '<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>'
svg_box = '<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'
svg_bulb = '<svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A6 6 0 1 0 7.5 11.5c.76.76 1.23 1.52 1.41 2.5Z"/></svg>'

def wrap_input(match, svg):
    return f'<div class="input-wrapper">{svg}{match.group(0)}</div>'

def wrap_textarea(match, svg):
    return f'<div class="input-wrapper">{svg}{match.group(0)}<div class="char-counter">0/500</div></div>'

content = re.sub(r'<input[^>]*name="project_name"[^>]*>', lambda m: wrap_input(m, svg_coins), content)
content = re.sub(r'<textarea[^>]*name="project_description"[^>]*><\/textarea>', lambda m: wrap_textarea(m, svg_doc), content)

# Change target_market to target_market text input if it is textarea, wait it is textarea
content = re.sub(r'<textarea[^>]*name="target_market"[^>]*><\/textarea>', lambda m: wrap_input(m, svg_users), content) # using input wrapper for textarea is fine

content = re.sub(r'<input[^>]*name="budget"[^>]*>', lambda m: wrap_input(m, svg_coins), content)
content = re.sub(r'<select[^>]*name="competition"[^>]*>[\s\S]*?<\/select>', lambda m: wrap_input(m, svg_bars), content)
content = re.sub(r'<textarea[^>]*name="resources"[^>]*><\/textarea>', lambda m: wrap_input(m, svg_users), content)
content = re.sub(r'<textarea[^>]*name="objectives"[^>]*><\/textarea>', lambda m: wrap_input(m, svg_target), content)

content = re.sub(r'<select[^>]*name="market"[^>]*>[\s\S]*?<\/select>', lambda m: wrap_input(m, svg_bars), content)
content = re.sub(r'<select[^>]*name="team"[^>]*>[\s\S]*?<\/select>', lambda m: wrap_input(m, svg_users), content)
content = re.sub(r'<select[^>]*name="resource"[^>]*>[\s\S]*?<\/select>', lambda m: wrap_input(m, svg_box), content)
content = re.sub(r'<select[^>]*name="innovation"[^>]*>[\s\S]*?<\/select>', lambda m: wrap_input(m, svg_bulb), content)

# Replace feasibility inputs with range inputs
def replace_feasibility(match):
    name = match.group(1)
    label_text = match.group(2)
    return f"""<div class="range-header-wrapper">
                            <label>{label_text}</label>
                            <div class="range-value-box" id="{name}_val">50</div>
                        </div>
                        <input type="range" name="{name}" value="50" required min="0" max="100" class="feasibility-input" oninput="document.getElementById('{name}_val').innerText = this.value; this.style.setProperty('--range-val', this.value + '%');">"""

# Let\'s do this manually
content = re.sub(
    r'<label>Market Opp\.<\/label>\s*<input type="number" name="f_market"[^>]*>\s*<div class="range-container">[\s\S]*?<\/div>',
    r'<div class="range-header-wrapper"><label>Market Opportunity</label><div class="range-value-box" id="f_market_val">50</div></div><input type="range" name="f_market" value="50" required min="0" max="100" class="feasibility-input" style="--range-val: 50%;" oninput="document.getElementById(\'f_market_val\').innerText = this.value; this.style.setProperty(\'--range-val\', this.value + \'%\');">',
    content
)
content = re.sub(
    r'<label>Team Capability<\/label>\s*<input type="number" name="f_team"[^>]*>\s*<div class="range-container">[\s\S]*?<\/div>',
    r'<div class="range-header-wrapper"><label>Team Capability</label><div class="range-value-box" id="f_team_val">50</div></div><input type="range" name="f_team" value="50" required min="0" max="100" class="feasibility-input" style="--range-val: 50%;" oninput="document.getElementById(\'f_team_val\').innerText = this.value; this.style.setProperty(\'--range-val\', this.value + \'%\');">',
    content
)
content = re.sub(
    r'<label>Comp\. Advantage<\/label>\s*<input type="number" name="f_comp"[^>]*>\s*<div class="range-container">[\s\S]*?<\/div>',
    r'<div class="range-header-wrapper"><label>Competitive Advantage</label><div class="range-value-box" id="f_comp_val">50</div></div><input type="range" name="f_comp" value="50" required min="0" max="100" class="feasibility-input" style="--range-val: 50%;" oninput="document.getElementById(\'f_comp_val\').innerText = this.value; this.style.setProperty(\'--range-val\', this.value + \'%\');">',
    content
)
content = re.sub(
    r'<label>Resource Avail\.<\/label>\s*<input type="number" name="f_res"[^>]*>\s*<div class="range-container">[\s\S]*?<\/div>',
    r'<div class="range-header-wrapper"><label>Resource Availability</label><div class="range-value-box" id="f_res_val">50</div></div><input type="range" name="f_res" value="50" required min="0" max="100" class="feasibility-input" style="--range-val: 50%;" oninput="document.getElementById(\'f_res_val\').innerText = this.value; this.style.setProperty(\'--range-val\', this.value + \'%\');">',
    content
)


# Add Footer Features
footer_html = '''
        <div class="features-footer" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; padding: 40px 0 80px; max-width: var(--copy-max); margin: 0 auto; position: relative; z-index: 10;">
            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="color: var(--gold-primary); background: rgba(214,168,79,0.08); padding: 10px; border-radius: 12px; border: 1px solid rgba(214,168,79,0.2);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 12 2.1 12"/><path d="M12 12 6.3 4.9"/><path d="M12 12 21.9 12"/><path d="M12 12 17.7 19.1"/></svg>
                </div>
                <div>
                    <h4 style="font-size: 0.875rem; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">AI-Powered Analysis</h4>
                    <p style="font-size: 0.75rem; color: var(--text-secondary);">Multi-dimensional risk evaluation</p>
                </div>
            </div>
            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="color: var(--gold-primary); background: rgba(214,168,79,0.08); padding: 10px; border-radius: 12px; border: 1px solid rgba(214,168,79,0.2);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"/></svg>
                </div>
                <div>
                    <h4 style="font-size: 0.875rem; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">Strategic Insights</h4>
                    <p style="font-size: 0.75rem; color: var(--text-secondary);">Actionable recommendations</p>
                </div>
            </div>
            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="color: var(--gold-primary); background: rgba(214,168,79,0.08); padding: 10px; border-radius: 12px; border: 1px solid rgba(214,168,79,0.2);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 3v5h5"/><line x1="9" y1="9" x2="10" y2="9"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>
                </div>
                <div>
                    <h4 style="font-size: 0.875rem; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">Comprehensive Report</h4>
                    <p style="font-size: 0.75rem; color: var(--text-secondary);">Detailed intelligence output</p>
                </div>
            </div>
            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="color: var(--gold-primary); background: rgba(214,168,79,0.08); padding: 10px; border-radius: 12px; border: 1px solid rgba(214,168,79,0.2);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
                </div>
                <div>
                    <h4 style="font-size: 0.875rem; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">Secure & Private</h4>
                    <p style="font-size: 0.75rem; color: var(--text-secondary);">Your data stays confidential</p>
                </div>
            </div>
        </div>
'''

content = content.replace('</form>\n    </div>\n\n    <script>', '</form>\n    </div>\n' + footer_html + '\n    <script>')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html patched.")
