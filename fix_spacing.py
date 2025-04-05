import re
import sys

def add_spacing(text):
    # Replace full-width space with half-width space, just in case
    text = text.replace('\u3000', ' ')

    # 1. Chinese followed by letter/number
    text = re.sub(r'([\u4e00-\u9fff])([A-Za-z0-9])', r'\1 \2', text)
    # 2. Letter/number followed by Chinese
    text = re.sub(r'([A-Za-z0-9])([\u4e00-\u9fff])', r'\1 \2', text)

    # 3. Chinese followed by backtick `
    text = re.sub(r'([\u4e00-\u9fff])(`)', r'\1 \2', text)
    # 4. Backtick ` followed by Chinese
    text = re.sub(r'(`)([\u4e00-\u9fff])', r'\1 \2', text)

    return text

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = add_spacing(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✔ Fixed spacing in {path}")
    else:
        print(f"✅ No spacing issues found in {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_spacing.py <filename>")
    else:
        process_file(sys.argv[1])