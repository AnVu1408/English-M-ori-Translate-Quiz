'''runs a quiz that helps users learn translations between English and Māori'''
def get_translations(string):
    """return a dictionary of maori and english translation"""
    list1 = string.strip().splitlines()

    if not list1:
        return []
    header = list1[0].strip().lower()
    valid_headers = {"english,māori", "māori,english"}
    
    if header not in valid_headers:
        print("Header language not recognized!")
        return [] #reutrn an empty list if header language not recognized 
    
    # Determine order based on header
    reverse_order = header == "māori,english"
    
    # Process the translations
    result = []
    for line in list1[1:]:
        parts = line.split(",", 1)  # Only split on the first comma to preserve word-groups
        if len(parts) == 2:
            english, maori = parts
            if reverse_order:
                result.append((maori, english))
            else:
                result.append((english, maori))
    
    return result

def get_translations_from_file(filename):
    """
    Reads a file and extracts translations.
    The file must be in UTF-8 encoding.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:  
            content = file.read()  
            return get_translations(content)  
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        return []

def answer_mask(reo, attempt):
    """produce a string the same length as the reo Māori string"""
    result = ""
    for i in range(len(reo)):
        if i < len(attempt) and reo[i].lower() == attempt[i].lower():
            result += "*"
        else:
            result += reo[i]
    return result


def main():
    '''Main function to run the translation quiz.'''
    filename = input("Please enter a filename: ")
    terms = get_translations_from_file(filename)
    
    if not terms:
        print("We can't play, hōhā!")
        return
    
    print(f"Kia ora, you have {len(terms)} terms to translate today :-)")
    
    to_translate = terms[:]
    incorrect = []
    total_attempts = 0
    
    while to_translate:
        incorrect.clear()
        
        for english, maori in to_translate:
            print(f"en: {english}")
            answer = input("mi: ").strip()
            total_attempts += 1
            
            if answer.lower() == maori.lower():
                print("Ka pai")
            else:
                print(f"A: {answer_mask(maori, answer)}")
                incorrect.append((english, maori))
        
        # Only terms that were incorrectly answered are kept
        to_translate = incorrect[:]
    
    print("You translated all the terms!")
    score = (len(terms) / total_attempts) * 100
    print(f"You scored {score:.2f}%")


main()