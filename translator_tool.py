from googletrans import Translator, LANGUAGES

# Create a Translator instance
translator = Translator()

def show_language_codes():
    print("\n📜 Supported Languages:")
    for code, lang in LANGUAGES.items():
        print(f"{code: <8} - {lang}")
    print("\n")

def detect_language(text):
    detection = translator.detect(text)
    lang_name = LANGUAGES.get(detection.lang, 'unknown')
    print(f"🔍 Detected language: {lang_name} ({detection.lang})")

    if detection.confidence is not None:
        print(f"🌡️ Confidence: {detection.confidence * 100:.2f}%")
    else:
        print("🌡️ Confidence: Not available")

def translate_text(text, dest_lang):
    try:
        translated = translator.translate(text, dest=dest_lang)
        lang_name = LANGUAGES.get(dest_lang, dest_lang)
        print(f"🌐 Translated ({lang_name}): {translated.text}")
    except Exception as e:
        print(f"❌ Translation error: {e}")

def menu():
    print("\n🌐 Google Translate Tool")
    print("1. Detect Language")
    print("2. Translate Text")
    print("3. Show Supported Language Codes")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            text = input("\n📝 Enter text to detect language: ")
            detect_language(text)
        
        elif choice == '2':
            text = input("\n📝 Enter text to translate: ")
            dest_lang = input("🎯 Enter target language code (e.g., fr, es, hi): ").lower()
            translate_text(text, dest_lang)
        
        elif choice == '3':
            show_language_codes()
        
        elif choice == '4':
            print("👋 Exiting. Thank you!")
            break
        
        else:
            print("⚠️ Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
