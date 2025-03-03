# import pywhatkit as pw

# txt = """Python is used for server-side web development, software development, mathematics, and system scripting. 
# and is popular for Rapid Application Development"""

# pw.text_to_handwriting(txt, "demo1.png", [0, 0, 138])
# print("END")

import pywhatkit as pw

txt = """Python is used for server-side web development, software development, mathematics, and system scripting. 
and is popular for Rapid Application Development"""

try:
    pw.text_to_handwriting(txt, "demo1.png", [0, 0, 138])
    print("Handwriting image created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

print("END")
