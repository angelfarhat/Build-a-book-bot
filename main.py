path = "books/frankenstein.txt" # location
char_counts = {}

def count_words(text): # counts function
    words = text.split()
    return len(words)

def count_characters(text):
    #Returns a character dictionary
    for char in text.lower(): #count lower cases to avoid duplicates
        if char.isalpha() or char.isspace(): # consider only letters (ignore spaces,)
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def main():
    with open(path) as f:
        contents = f.read()
        return contents


book_text = main() # get the reference from main function


if book_text:
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)

    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---") #start 
    print(f"{word_count} words found in the document\n")

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print("--- End report ---")

else:
    print("Error reading the file")
