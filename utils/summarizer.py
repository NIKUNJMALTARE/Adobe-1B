def summarize_section(text):
    lines = text.strip().split('. ')
    return '. '.join(lines[:3]) + '.' if len(lines) >= 3 else text
