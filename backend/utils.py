import json

def create_html(json_story_path: str) -> None:
    with open(json_story_path, 'r') as file:
        story = json.load(file)

    with open('backend/templates/base.html', 'r') as html_file:
        html_code = html_file.readlines()
        
        for index, line in enumerate(html_code):
            if line.find('title') != -1:
                html_code[index] = f"\t<title>{story['title']}</title>"
            
            if line.find('content') != -1:
                html_code[index] = f"\t<main>\n{story['story']}\n\t</main>\n"

            if line.find('ending') != -1:
                html_code[index] = f"\t<div class='ending'>\n{story['ending']}\n\t</div>\n"
    
    with open(f"backend/templates/{str(story['title']).replace(' ', '_')}.html", 'a+') as html_story_out:
        for line in html_code:
            html_story_out.write(line)



if __name__ == '__main__':
    create_html("backend/stories/Echoes_Beneath_the_Salt_House.json")