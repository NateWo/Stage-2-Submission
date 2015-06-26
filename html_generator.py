#This html_generator was built from instruction provided by Udacity

def generate_section_HTML(section_name, section_meat):
    part1 = '''
<div class="section">
    <div class="section-name">
        ''' + section_name
    part2 = '''
    </div>
    <div class="section-meat">
        <p>
             ''' + section_meat
    part3 = '''
        </p>
    </div>
</div>'''
    
    html = part1 + part2 + part3
    return html

def find_section_name(complete_section):
    start = complete_section.find('HEADING:')
    end = complete_section.find('EXPLANATION:')
    section_name = complete_section[start + 9 : end - 1]
    return section_name

def find_section_meat(complete_section):
    start = complete_section.find('EXPLANATION:')
    section_meat = complete_section[start + 13 : ]
    return section_meat

def section_identifier(multi_section_text, section_number):
    counter = 0
    while counter < section_number:
        counter = counter + 1
        next_section_start = multi_section_text.find('HEADING:')
        next_section_end   = multi_section_text.find('HEADING:', next_section_start + 1)
        if next_section_end >= 0:
            complete_section = multi_section_text[next_section_start : next_section_end]
        else:
            next_section_end = len(multi_section_text)
            complete_section = multi_section_text[next_section_start : ]
        multi_section_text = multi_section_text[next_section_end : ]
    return complete_section

def complete_multi_section_html(multi_section_text):
    current_section_id = 1
    complete_section = section_identifier(multi_section_text, current_section_id)
    multi_section_html = ''
    while complete_section != '':
        section_name = find_section_name(complete_section)
        section_meat = find_section_meat(complete_section)
        section_html = generate_section_HTML(section_name, section_meat)
        multi_section_html = multi_section_html + section_html
        current_section_id = current_section_id + 1
        complete_section = section_identifier(multi_section_text, current_section_id)
    return multi_section_html















