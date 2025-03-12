import streamlit as st

def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
    return word_count, char_count, vowel_count

def search_and_replace(text, search, replace):
    return text.replace(search, replace)

def convert_case(text, to_upper):
    return text.upper() if to_upper else text.lower()

def main():
    st.title("Text Analyzer App by SHAHID ")

    
    user_input = st.text_area("Enter your text here:", height=200)

    if st.button("Analyze"):
        word_count, char_count, vowel_count = analyze_text(user_input)
        st.write(f"Word Count: {word_count}")
        st.write(f"Character Count: {char_count}")
        st.write(f"Vowel Count: {vowel_count}")

   
    st.subheader("Search and Replace")
    search_text = st.text_input("Search for:")
    replace_text = st.text_input("Replace with:")
    if st.button("Replace"):
        replaced_text = search_and_replace(user_input, search_text, replace_text)
        st.write("Updated Text:")
        st.write(replaced_text)


    st.subheader("Case Conversion")
    to_upper = st.radio("Convert to:", ("Upper Case", "Lower Case"))
    if st.button("Convert"):
        converted_text = convert_case(user_input, to_upper == "Upper Case")
        st.write("Converted Text:")
        st.write(converted_text)

 
    st.subheader("Type Casting and Comparison")
    word_to_compare = st.text_input("Enter a word to compare:")
    if st.button("Compare"):
        words = user_input.split()
        if word_to_compare in words:
            st.write(f"The word '{word_to_compare}' is in the paragraph.")
        else:
            st.write(f"The word '{word_to_compare}' is NOT in the paragraph.")

if __name__ == "__main__":
    main()