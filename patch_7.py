import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CTAs and New Styles CSS
new_css = """
        .premium-cta {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 260px;
            height: 64px;
            border-radius: 999px;
            background: rgba(15, 19, 26, 0.85);
            border: 1px solid rgba(214,168,79,0.5);
            color: #F2C96B;
            font-size: 1.125rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(214,168,79,0.2), inset 0 1px 0 rgba(255,255,255,0.05);
            transition: all 0.4s ease;
            text-decoration: none;
            margin: 0 auto;
        }
        .premium-cta:hover {
            background: rgba(214,168,79,0.1);
            border-color: rgba(242,201,107,0.8);
            box-shadow: 0 0 35px rgba(214,168,79,0.35), inset 0 1px 0 rgba(255,255,255,0.1);
            transform: translateY(-3px);
            color: #ffffff;
        }
        .premium-cta:active {
            transform: translateY(1px) scale(0.98);
            box-shadow: 0 0 15px rgba(214,168,79,0.4);
        }
        .cta-container {
            display: flex;
            justify-content: center;
            margin-top: 40px;
        }

        /* Feasibility Numeric Inputs */
        .feasibility-number {
            width: 100%;
            text-align: center;
            font-size: 32px;
            font-weight: 600;
            color: #F5F5F5;
            background: transparent;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 12px;
            margin: 16px 0;
            transition: all 0.3s ease;
            -moz-appearance: textfield;
        }
        .feasibility-number::-webkit-inner-spin-button, 
        .feasibility-number::-webkit-outer-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        .feasibility-number:focus {
            border-color: rgba(242,201,107,0.75);
            box-shadow: 0 0 25px rgba(214,168,79,0.16);
            outline: none;
        }
        .metric-visual {
            margin-top: 10px;
        }
        .metric-track {
            height: 4px;
            background: rgba(255,255,255,0.1);
            border-radius: 2px;
            position: relative;
            margin-bottom: 8px;
        }
        .metric-fill {
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 50%;
            background: var(--metric-color, #D6A84F);
            border-radius: 2px;
            transition: width 0.3s ease, background 0.3s ease;
        }
        .metric-thumb {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 12px;
            height: 12px;
            background: #fff;
            border-radius: 50%;
            box-shadow: 0 0 10px var(--metric-color, #D6A84F);
            transition: left 0.3s ease, box-shadow 0.3s ease;
        }
        .metric-labels {
            display: flex;
            justify-content: space-between;
            font-size: 0.7rem;
            color: var(--muted);
            font-weight: 600;
            letter-spacing: 0.05em;
        }

        /* Feature Cards */
        .features-footer {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            padding: 60px 0 100px;
            max-width: var(--copy-max);
            margin: 0 auto;
            position: relative;
            z-index: 10;
        }
        .feature-card {
            background: rgba(15, 19, 26, 0.82);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 32px 24px;
            transition: all 0.4s ease;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: rgba(214,168,79,0.5);
            background: rgba(19, 24, 32, 0.92);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3), 0 0 25px rgba(214,168,79,0.12);
        }
        .feature-icon-wrapper {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(214,168,79,0.2);
            border-radius: 14px;
            padding: 12px;
            margin-bottom: 20px;
            color: #D6A84F;
            transition: all 0.4s ease;
        }
        .feature-card:hover .feature-icon-wrapper {
            background: rgba(214,168,79,0.15);
            border-color: rgba(242,201,107,0.6);
            color: #F2C96B;
            box-shadow: 0 0 20px rgba(214,168,79,0.3);
            transform: translateY(-2px) scale(1.05);
        }
        .feature-title {
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 8px;
            transition: color 0.3s ease;
        }
        .feature-card:hover .feature-title {
            color: #ffffff;
        }
        .feature-desc {
            font-size: 0.85rem;
            color: var(--text-secondary);
            line-height: 1.5;
            transition: color 0.3s ease;
        }
        .feature-card:hover .feature-desc {
            color: #e0e0e0;
        }

        /* Error Messages Refined */
        .error-msg {
            display: none;
            color: #e07a5f;
            font-size: 0.8rem;
            font-weight: 500;
            margin-top: 8px;
            align-items: center;
            gap: 6px;
        }
        .error-msg::before {
            content: '⚠';
            font-size: 0.9rem;
        }
        
        .hero-cta {
"""

content = content.replace("        .hero-cta {", new_css)
content = content.replace('class="hero-cta"', 'class="premium-cta"')
content = content.replace('class="hero-cta ', 'class="premium-cta ')
content = content.replace('id="submitBtn">', 'id="submitBtn" class="premium-cta">')
content = content.replace('id="submitBtn" class="cta-button">', 'id="submitBtn" class="premium-cta">')


# 2. Feasibility HTML
feasibility_html_old_pattern = r'<div class="form-grid">\s*<div class="feasibility-card">[\s\S]*?<div class="cta-container">'

def get_new_feasibility_html(name, label):
    return f'''                    <div class="feasibility-card">
                        <div class="metric-info">
                            <label style="margin: 0; font-size: 0.8rem; letter-spacing: 0.1em; color: var(--muted); text-transform: uppercase;">{label}</label>
                        </div>
                        <div class="metric-input-wrapper">
                            <input type="number" name="{name}" value="50" min="0" max="100" class="feasibility-number" required>
                        </div>
                        <div class="metric-visual">
                            <div class="metric-track">
                                <div class="metric-fill" id="{name}_fill"></div>
                                <div class="metric-thumb" id="{name}_thumb"></div>
                            </div>
                            <div class="metric-labels"><span>LOW</span><span>HIGH</span></div>
                        </div>
                    </div>'''

feasibility_html_new = f'''                <div class="form-grid">
{get_new_feasibility_html("f_market", "Market Opportunity")}
{get_new_feasibility_html("f_team", "Team Capability")}
{get_new_feasibility_html("f_comp", "Competitive Advantage")}
{get_new_feasibility_html("f_res", "Resource Availability")}
                </div>
            </div>
            
            <div class="cta-container">'''

content = re.sub(feasibility_html_old_pattern, feasibility_html_new, content)

# 3. Feasibility JS
old_js = r"// Feasibility Range Visualizer Logic.*?\}\);"
new_js = """// Feasibility Numeric Input Logic
        document.querySelectorAll('.feasibility-number').forEach(input => {
            const updateVisuals = function() {
                let val = parseInt(input.value);
                if (isNaN(val)) val = 0;
                
                // Color intelligence
                let color = '#D6A84F'; // gold (40-69)
                if (val < 40) color = '#e07a5f'; // red (0-39)
                else if (val >= 70) color = '#a3c383'; // green-gold (70-100)
                
                if (val > 100) { val = 100; input.value = 100; }
                if (val < 0) { val = 0; input.value = 0; }
                
                const card = input.closest('.feasibility-card');
                const fill = card.querySelector('.metric-fill');
                const thumb = card.querySelector('.metric-thumb');
                
                if (fill && thumb) {
                    fill.style.width = val + '%';
                    thumb.style.left = val + '%';
                    
                    fill.style.background = color;
                    thumb.style.boxShadow = `0 0 10px ${color}`;
                }
            };
            input.addEventListener('input', updateVisuals);
            updateVisuals(); // initial run
        });"""
content = re.sub(old_js, new_js, content, flags=re.DOTALL)

# 4. Features HTML Replacement
features_old_html = r'<div class="features-footer"[\s\S]*?</div>\s*</div>\s*</div>\s*</div>'
features_new_html = """        <div class="features-footer">
            <div class="feature-card" onclick="document.querySelector('#workspace').scrollIntoView({behavior: 'smooth'})">
                <div class="feature-icon-wrapper">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 12 2.1 12"/><path d="M12 12 6.3 4.9"/><path d="M12 12 21.9 12"/><path d="M12 12 17.7 19.1"/></svg>
                </div>
                <h4 class="feature-title">AI-Powered Analysis</h4>
                <p class="feature-desc">Multi-dimensional risk evaluation</p>
            </div>
            <div class="feature-card" onclick="document.querySelector('#grp-name').scrollIntoView({behavior: 'smooth'})">
                <div class="feature-icon-wrapper">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"/></svg>
                </div>
                <h4 class="feature-title">Strategic Insights</h4>
                <p class="feature-desc">Actionable recommendations</p>
            </div>
            <div class="feature-card" onclick="document.querySelector('#grp-budget').scrollIntoView({behavior: 'smooth'})">
                <div class="feature-icon-wrapper">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 3v5h5"/><line x1="9" y1="9" x2="10" y2="9"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>
                </div>
                <h4 class="feature-title">Comprehensive Report</h4>
                <p class="feature-desc">Detailed intelligence output</p>
            </div>
            <div class="feature-card" onclick="this.querySelector('.feature-icon-wrapper').style.transform = 'scale(1.1)'; setTimeout(() => this.querySelector('.feature-icon-wrapper').style.transform = '', 300);">
                <div class="feature-icon-wrapper">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
                </div>
                <h4 class="feature-title">Secure & Private</h4>
                <p class="feature-desc">Your data stays confidential</p>
            </div>
        </div>"""
content = re.sub(features_old_html, features_new_html, content, flags=re.DOTALL)

# 5. Header Status and Loading Overlay
content = content.replace(
    '<div class="status-dot"></div>\n                AI Analysis Ready',
    '<div class="status-dot" style="background:#4ade80; box-shadow:0 0 8px #4ade80;"></div>\n                AI Analysis Ready'
)
content = content.replace('<div class="loading-text" id="loadingText">Analyzing your project...</div>', '')

# Remove extra elements inside the button itself, we just need text for the loading state
content = content.replace('<div class="spinner" id="btnSpinner"></div>', '')

# Replace JS submit text 
content = content.replace("btnText.innerText = 'Analyzing...';", "btnText.innerText = '◌ ANALYZING PROJECT...';\n                btn.style.boxShadow = '0 0 30px rgba(214,168,79,0.5)';")


# 6. Hero Spacing Updates
content = content.replace('margin-bottom: 160px;', 'margin-bottom: 80px;')
content = content.replace('--hero-gap: 85px;', '--hero-gap: 40px;')
content = content.replace('padding: 60px 0 100px;', 'padding: 40px 0 80px;')

# 7. Button Fixes: Remove default border from generic buttons
content = content.replace('button[type="submit"]', '.premium-cta')
content = content.replace("document.querySelectorAll('.premium-cta, .premium-cta')", "document.querySelectorAll('.premium-cta')")

# Handle error-msg display block by converting `display: block` to `display: flex` when showing
content = content.replace("reqField.nextElementSibling.style.display = 'block';", "reqField.nextElementSibling.style.display = 'flex';")


with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 7 generated and applied.")
