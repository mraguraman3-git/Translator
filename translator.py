from googletrans import Translator

def translate_file(input_file, output_file):
    translator = Translator()

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    translated = translator.translate(text, src="en", dest="ta")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated.text)

    print("Translation complete!")
    print("Output saved to:", output_file)


if __name__ == "__main__":
    input_file = "translateTest.txt"
    output_file = "translated_tamil.txt"

    translate_file(input_file, output_file)