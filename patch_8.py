import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Global validation error banner removal
content = re.sub(r'{%\s*if error\s*%}.*?{%\s*endif\s*%}', '', content, flags=re.DOTALL)

# 2. Add CSS for .has-error and error-msg to make them visible and premium
has_error_css = """
        .has-error .error-msg {
            display: flex !important;
        }
        .has-error input, .has-error textarea, .has-error select {
            border-color: #e07a5f !important;
            background: rgba(224, 122, 95, 0.05) !important;
        }
        .has-error input:focus, .has-error textarea:focus, .has-error select:focus {
            box-shadow: 0 0 15px rgba(224, 122, 95, 0.2) !important;
        }
"""
if ".has-error .error-msg" not in content:
    content = content.replace("        /* Error Messages Refined */", has_error_css + "\n        /* Error Messages Refined */")

# 3. BUG 2: Form content disappears / huge empty space
# Remove scroll-reveal logic entirely from analysis-section to ensure they stay in document flow
content = content.replace("            opacity: 0;\n            transform: translateY(20px);", "")
content = content.replace("        .analysis-section.visible {\n            opacity: 1;\n            transform: translateY(0);\n        }", "")
content = content.replace('class="analysis-section scroll-reveal"', 'class="analysis-section"')

# Remove intersection observer for scroll-reveal entirely
content = re.sub(r"// Intersection Observer for Scroll Reveal[\s\S]*?observer\.observe\(section\);\n\s*\}\);", "", content)

# 4. BUG 3: Hero padding/margins
content = content.replace("padding: 40px 0;", "padding: 20px 0 0 0;")
content = content.replace("margin-bottom: 80px;", "margin-bottom: 40px;")

# 5. BUG 4: Robust Form JS Validation
robust_submit_js = """// Form Submit & Loading State Logic
        document.getElementById('analysisForm').addEventListener('submit', function(e) {
            let isValid = true;
            
            const requiredFields = [
                {name: 'project_name', grp: 'grp-name'},
                {name: 'project_description', grp: 'grp-desc'},
                {name: 'target_market', grp: 'grp-market'},
                {name: 'objectives', grp: 'grp-obj'},
                {name: 'budget', grp: 'grp-budget'}
            ];
            
            try {
                requiredFields.forEach(f => {
                    const el = document.querySelector('[name="' + f.name + '"]');
                    const grp = document.getElementById(f.grp);
                    
                    if (el && grp) {
                        if (!el.value.trim() || (f.name === 'budget' && isNaN(el.value))) {
                            grp.classList.add('has-error');
                            isValid = false;
                        } else {
                            grp.classList.remove('has-error');
                        }
                    }
                });
                
                if (!isValid) {
                    e.preventDefault();
                    const firstErr = document.querySelector('.has-error');
                    if (firstErr) {
                        firstErr.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                    return; // Stop submission
                }
            } catch (err) {
                console.error("Validation error: ", err);
            }

            // Execute UI loading state
            const btn = document.getElementById('submitBtn');
            const btnText = document.getElementById('btnText');
            const overlay = document.getElementById('loadingOverlay');
            
            if (btn && btnText) {
                btn.disabled = true;
                btnText.textContent = "◌ ANALYZING PROJECT...";
                btn.style.boxShadow = '0 0 30px rgba(214,168,79,0.5)';
            }
            
            if (overlay) {
                overlay.style.display = 'flex';
                setTimeout(() => { overlay.classList.add('visible'); }, 50);
            }
        });"""
        
content = re.sub(r"// Form Submit & Loading State Logic[\s\S]*?\}, 2500\);\n\s*\}\);", robust_submit_js, content)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 8 generated and applied.")
