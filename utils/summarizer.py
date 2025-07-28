def summarize_section(text):
    for line in text.split('. '):
        if any(kw in line.lower() for kw in ["form", "sign", "fill", "prepare", "field", "tool", "submit"]):
            return line.strip() + "."
    return text.strip().split('. ')[0] + "."
