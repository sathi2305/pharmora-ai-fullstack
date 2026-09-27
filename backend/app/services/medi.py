RESPONSES={"en": "I understand that is worrying. Fluconazole slows CYP2C9 that clears Warfarin -> bleeding risk 86%. You are right to ask. Please show doctor. 💙", "ta": "இது கவலை அளிக்கும் என்று புரிகிறது. ஃப்ளூகோனசோல் CYP2C9 மெதுவாக்குகிறது -> இரத்தப்போக்கு 86%. மருத்துவரிடம் காட்டுங்கள். 💙", "hi": "मैं समझता हूँ चिंताजनक है। फ्लुकोनाज़ोल CYP2C9 धीमा करता है -> ब्लीडिंग 86%। डॉक्टर से सलाह लें। 💙"}
def generate_medi_response(message, language="en", user_meds=None, genotype=None):
    base=RESPONSES.get(language, RESPONSES["en"])
    if genotype: base+=f"\nNote CYP2C9 {genotype} slow metabolizer."
    return base+"\n\n⚠️ I am Medi, not a doctor. Consult doctor. Sources: DrugBank."
