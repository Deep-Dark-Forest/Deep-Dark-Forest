import re

def replace_colors(html_content):
    # 替换颜色映射表
    color_replacements = {
        "#666666": "#ffffff",
        "#339966": "#beddca",
        "#9933ff": "#e4bfff",
        "#808000": "#d8d3ae",
        "#6666ff": "#d5caff"
    }
    
    # 遍历替换颜色
    for old_color, new_color in color_replacements.items():
        html_content = re.sub(re.escape(old_color), new_color, html_content)
    
    # 只替换文本颜色为#ffffff为黑色，其他#ffffff不受影响
    html_content = re.sub(r'color:\s*#ffffff(;|)', 'color: #000000\\1', html_content)

    return html_content

# 读取HTML文件
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 写入修改后的HTML文件
def write_html_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    # 输入的HTML文件路径
    input_file = 'input.html'
    output_file = 'output.html'

    # 读取原始HTML内容
    html_content = read_html_file(input_file)

    # 替换颜色
    modified_html = replace_colors(html_content)

    # 写入修改后的内容到新文件
    write_html_file(output_file, modified_html)

    print(f"修改后的HTML已保存为 {output_file}")
