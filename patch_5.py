import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Enhance .analysis-section with radial gradient support for mouse tracking
# Default background without hover: rgba(15, 19, 26, 0.82)
# Hover background: rgba(19, 24, 32, 0.92) + the radial gradient
new_analysis_section_css = """        .analysis-section {
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
            overflow: hidden; /* for radial gradient */
        }
        
        .analysis-section::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(
                circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
                rgba(214,168,79,0.06),
                transparent 35%
            );
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
            z-index: 0;
        }

        .analysis-section > * {
            position: relative;
            z-index: 1;
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
        
        .analysis-section:hover::before {
            opacity: 1;
        }

        .analysis-section.active-card {
            border: 1px solid rgba(242,201,107,0.75);
            box-shadow: 0 25px 80px rgba(0,0,0,0.40), 0 0 45px rgba(214,168,79,0.22), inset 0 1px 0 rgba(242,201,107,0.08);
            background: rgba(19, 24, 32, 0.92);
            transform: translateY(-4px);
        }
        
        .analysis-section.active-card::before {
            opacity: 1;
            background: radial-gradient(
                circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
                rgba(214,168,79,0.10),
                transparent 45%
            );
        }
"""
content = re.sub(r'        \.analysis-section\s*\{.*?\.analysis-section\.active-card\s*\{[^}]*\}\n', new_analysis_section_css, content, flags=re.DOTALL)


# Update input focus
new_input_focus = """        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: rgba(214, 168, 79, 0.75);
            background: rgba(214, 168, 79, 0.05);
            box-shadow: 0 0 20px rgba(214, 168, 79, 0.12);
        }"""
content = re.sub(r'        input:focus.*?box-shadow:[^}]*\}', new_input_focus, content, flags=re.DOTALL)

# Update slider thumb active state
slider_css = """        input[type=range]::-webkit-slider-thumb {
            height: 16px;
            width: 16px;
            border-radius: 50%;
            background: #ffffff;
            cursor: pointer;
            -webkit-appearance: none;
            margin-top: -6px;
            box-shadow: none; /* Default normal thumb: white */
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        input[type=range]:hover::-webkit-slider-thumb {
            transform: scale(1.1);
            box-shadow: 0 0 10px rgba(214,168,79,0.5); /* hover thumb: white + soft gold halo */
        }
        input[type=range]:active::-webkit-slider-thumb {
            transform: scale(1.2);
            box-shadow: 0 0 18px rgba(214,168,79,0.85); /* active thumb: white + stronger gold halo */
        }
        
        input[type=range]:hover::-webkit-slider-runnable-track {
            background: linear-gradient(90deg, var(--gold-light) var(--range-val, 50%), rgba(255,255,255,0.15) var(--range-val, 50%));
        }
"""
content = re.sub(r'        input\[type=range\]::-webkit-slider-thumb.*?rgba\(214,168,79,0\.8\);\s*\}', slider_css, content, flags=re.DOTALL)

# Add mouse tracking JS
mouse_tracking_js = """
        // Mouse Proximity Glow Effect
        document.querySelectorAll('.analysis-section').forEach(card => {
            card.addEventListener('mousemove', e => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                card.style.setProperty('--mouse-x', `${x}px`);
                card.style.setProperty('--mouse-y', `${y}px`);
            });
            // Ensure tracking triggers active card logic as well on click
            card.addEventListener('click', function() {
                document.querySelectorAll('.analysis-section').forEach(s => s.classList.remove('active-card'));
                this.classList.add('active-card');
            });
        });
"""
# Replace old click listener logic from patch_4 to include mousemove
content = re.sub(r'        // Card Click Active State Logic.*?\}\);\n        \}\);\n', mouse_tracking_js, content, flags=re.DOTALL)

# Dropdowns styling (select)
dropdown_css = """        select {
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23C5C8CE' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: right 18px center;
            background-size: 16px;
            cursor: pointer;
            color: var(--text-primary);
        }
        select option {
            background: #10151C;
            color: #F5F3EE;
        }"""
content = re.sub(r'        select \{.*?\}\s*\}', dropdown_css, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 5 applied.")
