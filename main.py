def main():
    path = "books/frankenstein.txt"
    content = get_book_text(path)
    count = count_words(content)
    char_counts = count_characters(content)
    char_counts_list = sort_character_counts(char_counts)    
    print_report(path, count, char_counts_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(content):
    return len(content.split())

def count_characters(content):
    char_counts = {}
    content = content.lower()
    for c in content:
        if not c.isalpha():
            continue
        if c not in char_counts:
            char_counts[c] = 0
        char_counts[c] += 1
    return char_counts

def sort_character_counts(char_counts):
    def sort_fn(item):
        return item["count"]
    
    char_counts_list = [{ "character": k, "count": v } for k, v in char_counts.items()]
    char_counts_list.sort(reverse=True, key=sort_fn)
    return char_counts_list

def print_character_counts(char_counts_list):
    for item in char_counts_list:
        character = item["character"]
        count = item["count"]
        print(f"The '{character}' character was found {count} times")

def print_report(path, count, char_counts_list):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the book!\n")
    print_character_counts(char_counts_list)
    print(f"--- End report ---")

main()