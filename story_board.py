from IPython.display import Markdown, display, Image

def clean_string(input_string):
    input_string = input_string.replace("﴾", "(")  # squiggle parenthesis with parenthesis 
    input_string = input_string.replace("﴿", ")")  # squiggle parenthesis with parenthesis  
    cleaned_string = input_string
    return cleaned_string

def scrub_string(input_string):
    # input_string = input_string.replace("‐", " ")  # replace minus signs with blank
    input_string = input_string.replace("﴾", "(")  # squiggle parenthesis with parenthesis 
    input_string = input_string.replace("﴿", ")")  # squiggle parenthesis with parenthesis     

    unwanted_chars = '"\'‐-–:/“”‘’'  # Add any other quote-like or minus/dash characters
    translation_table = str.maketrans('', '', unwanted_chars)

    cleaned_string = input_string.translate(translation_table)
    return cleaned_string

def outmd(definition, file_name='storyboard.md'):
    """
    Appends a cleaned Markdown definition to the storyboard file and displays it.

    Parameters:
        definition (str): The content to add as a new section.
        file_name (str): The markdown file to append to (default 'storyboard.md').
    """
    definition = clean_string(definition)
    
    # Add a newline before and after for better Markdown formatting
    section = f"\n\n{definition}\n\n"
    
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(section)
    
    display(Markdown(definition))


def start_story(definition, file_name='storyboard.md'):
    """
    Initializes a new storyboard markdown file and writes the provided definition to it.
    
    Parameters:
        definition (str): The starting content for the storyboard.
        file_name (str): The markdown file to create or overwrite (default 'storyboard.md').
    """
    definition = clean_string(definition)
    
    # Use 'w' mode to overwrite (start clean)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(definition)
    
    display(Markdown(definition))

def add_image(image_file_name, file_name='storyboard.md'):
    """
    Inserts a Markdown-formatted image reference into the storyboard file.
    
    Args:
        image_file_name (str): The path or filename of the image (e.g., 'image.png').
        file_name (str): The Markdown file to insert into (default: 'storyboard.md').
    """
    # Clean input (optional, based on your style)
    image_file_name = clean_string(image_file_name)

    # Create the Markdown image tag
    image_markdown = f'![Image]({image_file_name})\n\n'

    # Append the image tag to the storyboard file
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(image_markdown)
    
    # Display it nicely
    display(Markdown(image_markdown))

