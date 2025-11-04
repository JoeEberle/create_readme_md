####################################################################################
#
# Library to help generate readme files efficiently
# Joe Eberle - 10/13/2025 
#
####################################################################################

def generate_intro(solution_name, solution_description, target_directory):
    solution_name = solution_name.replace('_SN','').title()
    solution_name = solution_name.replace('_',' ')
    return f"""
    
# {solution_name} 

## {solution_description}

    """

def generate_solution_image(image_filename): ## logo for the solution
    return f"""![Image image_filename]({image_filename})"""



def generate_readme_solution_features():
    return f"""
## ✨ Solution Features

- 🧠 **Easy to understand** — clear APIs and examples
- ⚙️ **Easily configurable** — sensible defaults with overrides
- 🧰 **Starter templates** — kickstart projects in minutes
- ⚡ **Fast & automated** — fewer manual steps
- ⏱️ **Saves time** — focus on what matters

"""

def generate_instructions(solution_name, target_directory):

    image_filename = "getting_started.png"
    if os.path.exists(target_directory+'\\'+image_filename):
        instruction_content = f"""
## Getting Started
    """        
        instruction_content += generate_solution_image(image_filename) 
    else:
        instruction_content = f"""
## Getting Started

To get started with the **{solution_name}** solution repository, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies listed at the top of the notebook.
3. Explore the example code provided in the repository and experiment.
4. Run the notebook and make it your own - **EASY !**
    """        
    
    return instruction_content



def generate_code_features(solution_name, target_directory):
    return f"""

## ⚙️ Key Features

- ✅ **Self Documenting** Automatically identifies and annotates major steps in a notebook, making the codebase readable and well structured.
- ✅ **Self Testing** Includes built in **unit tests** for each function to validate logic and ensure code reliability.
- ✅ **Easily Configurable** Uses a simple **config.ini** file for centralized settings and easy customization through key value pairs.
- ✅ **Talking Code** explains itself through inline commentary, helping you understand both **what** it does and **why** it does it.
- ✅ **Self Logging** extends Python’s standard **logging** module for **step by step runtime insights**.
- ✅ **Self Debugging** Includes debugging hooks and detailed error tracing to simplify development and troubleshooting.
- ✅ **Low Code or  No Code** Designed to minimize complexity — most full solutions are under 50 lines of code.
- ✅ **Educational** Each template includes educational narrative and background context to support learning, teaching, and collaborative development.

    """

def generate_reference(repo_URL = 'https://github.com/JoeEberle/', email = 'josepheberle@outlook.com'):
    return f"""

## Github {repo_URL} - Email  {email} 
    """

def generate_addendum(target_directory):
    image_list = []
    mark_down_string = " "
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            if file.endswith(".png"):
                image_list.append(file)

    for image in image_list:
        if image not in ('code.png','sample.png','notebook_features.png'
                         ,'developer.png','solution_features.png'
                         ,'developer.png','getting_started.png'                         
                         ,'brand.png','solution_sign.png','solution_stacked_sign.png'):
            mark_down_string += f"![additional_image]({image})  <br>"  
    return f"""
## List of Figures
{mark_down_string}
    """

def generate_readme(filename_to_generate, solution_name, solution_description, target_directory, over_write):
    """ Generate a readme.md file.   """
    readme_filename = filename_to_generate
    copy_status = ""

    if os.path.exists(target_directory+'\\'+readme_filename) and (over_write == False):
        copy_status = 'Read me already exists - not generating'
        return copy_status
    else:
        copy_status = 'Read me  not found - generating file'
        image_filename = "solution_sign.png"    
        solution_name = solution_name.replace('_',' ').title()
        readme_content = add_solution_sign(image_filename)        
        readme_content += generate_intro(solution_name, solution_description, target_directory)        

        image_filename = "code.png"
        readme_content += generate_solution_image(image_filename)  

        if "nsp" not in solution_name.lower() and "oec" not in solution_name.lower():
            readme_content += generate_table_of_contents()

        # solution_description_filename = "story_board.md"
        # if os.path.exists(target_directory+'\\'+solution_description_filename):
        #     file_name = target_directory+'\\'+solution_description_filename
        #     # Open the Markdown file in read mode and read its content
        #     with open(file_name, "r", encoding="utf-8", errors="replace") as f:
        #         readme_content += f.read()

        solution_description_filename = "storyboard.md"
        if os.path.exists(target_directory+'\\'+solution_description_filename):
            file_name = target_directory+'\\'+solution_description_filename
            # Open the Markdown file in read mode and read its content
            with open(file_name, "r", encoding="utf-8", errors="replace") as f:
                readme_content += f.read()  
        
        solution_description_filename = "solution_description.md"
        if os.path.exists(target_directory+'\\'+solution_description_filename):
            file_name = target_directory+'\\'+solution_description_filename
            # Open the Markdown file in read mode and read its content
            with open(file_name, "r", encoding="utf-8", errors="replace") as f:
                readme_content += f.read()
        else:
            readme_content += generate_solution_description(solution_name, solution_description, target_directory)
       
        readme_content += add_markdown(target_directory)

        image_filename = "code.png"
        readme_content += generate_solution_image(image_filename)          

        image_filename = "sample.png"
        if os.path.exists(target_directory+'\\'+image_filename):
            readme_content += generate_solution_image(image_filename)        

        repo_URL = 'https://github.com/JoeEberle/'
        email = 'josepheberle@outlook.com'
        
        if "nsp" not in solution_name.lower() and "oec" not in solution_name.lower():
            readme_content += generate_instructions(solution_name, target_directory)  
            readme_content += generate_readme_solution_features() 
            readme_content += generate_code_features(solution_name, target_directory) 
            # readme_content += generate_addendum(target_directory)  
            # readme_content += generate_reference(repo_URL, email)
            # readme_content += generate_branding(target_directory)                
        
        if not os.path.exists(target_directory):      # Create the target directory if it doesn't exist
            os.makedirs(target_directory)
    
        readme_path = os.path.join(target_directory, filename_to_generate)     # Specify the path for the readme.md file
    
        with open(readme_path, 'w', encoding='utf-8', errors='replace') as f:      # Write the template to the readme.md file
            f.write(readme_content)
 
    
    result = f"{readme_path}'" 
    return result 

