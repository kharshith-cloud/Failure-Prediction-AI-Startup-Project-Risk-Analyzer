import os
import json
import google.generativeai as genai

def generate_strategic_reasoning(context_data: dict) -> dict:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"status": "error", "reason": "No API key configured."}
        
    try:
        genai.configure(api_key=api_key)
        # Use gemini-1.5-flash as it is fast and reliable
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = (
            "You are a strategic business consultant analyzing a startup/project risk assessment.\n"
            "Based on the following data, provide a concise (2-3 paragraphs) strategic reasoning report "
            "that highlights the main risks and justifies the recommended mitigations. "
            "Do NOT return JSON. Return plain text paragraphs.\n\n"
            f"Context Data: {json.dumps(context_data)}"
        )
        
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        if not text:
            return {"status": "error", "reason": "Empty response from Gemini."}
            
        return {"status": "success", "reasoning": text}
    except Exception as e:
        return {"status": "error", "reason": f"API Exception: {str(e)}"}
