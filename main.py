import streamlit as st
import json

# Load & save library data
def load_library():
    try:
        with open('library.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_library(library):
    with open('library.json', 'w') as file:
        json.dump(library, file, indent=4)

# Initialize library 
library = load_library()

st.title('Library Management System')
menu = st.sidebar.radio("Select an option", ["Add Book", "View Library", "Remove Book", "Search Book", "Save and Exit"])

if menu == "View Library":
    st.sidebar.header("Your Library")
    if library:
        st.table(library)
    else:
        st.write("No book in your library. Add some books!")

# Add Book
elif menu == "Add Book":
    st.sidebar.header("Add a new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=2022, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("Add Book"):
        library.append({"title": title, "author": author, "genre": genre, "read_status": read_status, "year": year})
        save_library(library)
        st.success(f"Added book: {title}")
        st.rerun()

# Remove Book
elif menu == "Remove Book":   
    st.sidebar.header("Remove a book")    
    book_titles = [book["title"] for book in library]
    
    if book_titles:
        selected_book = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library(library)
            st.success("Book removed successfully")
            st.rerun()
    else:
        st.warning("No book in your library. Add some books!")

# Search Book
elif menu == "Search Book":
    st.sidebar.header("Search a book")
    search_term = st.text_input("Enter title or author name")
    
    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No book found")

# Save and exit
elif menu == "Save and Exit":
    save_library(library)
    st.balloons()
    st.success("Library saved successfully")
