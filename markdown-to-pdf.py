import markdown
from weasyprint import HTML
from pathlib import Path

def md_to_pdf(md_file_path):
    # Ensure the markdown file exists
    md_path = Path(md_file_path)
    if not md_path.is_file():
        print(f"The file {md_file_path} does not exist.")
        # The reason why we use return without variable is because it would default to the argument that we used for the function, is that right?
        return
    
    # Read markdown content
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])

    # Add basic HTML structure and CSS styling
    html_template = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 15px;
                line-height: 1.6;
                color: #333;
            }}
            /* Headings */
            h1, h2, h3, h4, h5, h6 {{
                color: #333;
                margin-bottom: 10px;
            }}

            /* Paragraphs */
            p {{ margin: 10px 0; }}

            /* Lists */
            ul, ol {{
                margin-left: 20px;
                padding-left: 20px;
            }}

            ul {{
                list-style-type: disc; /* Bullet points */
            }}

            ol {{
                list-style-type: decimal; /* Numbered lists */
            }}

            li {{
                margin-bottom: 5px;
            }}

            /* Nested Lists */
            ul ul, ol ol, ul ol, ol ul {{
                margin-left: 20px;
            }}

            /* Code blocks */
            pre {{
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 4px;
                overflow-x: auto;
                font-family: 'Courier New', monospace;
            }}

            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 4px;
                font-family: 'Courier New', monospace;
                color: #d6336c;
            }}

            /* Tables */
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}

            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}

            /* Links */
            a {{
                color: #007acc;
                text-decoration: none;
            }}

            a:hover {{
                text-decoration: underline;
            }}

            /* Bold and Italic */
            strong {{ font-weight: bold; }}
            em {{ font-style: italic; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Define output PDF path
    pdf_file_path = md_path.with_suffix('.pdf')

    # Convert HTML to PDF using WeasyPrint
    try:
        HTML(string=html_template).write_pdf(str(pdf_file_path))
        print(f"PDF saved to {pdf_file_path}")
    except Exception as e:
        print(f"Failed to convert to PDF: {e}")

if __name__ == '__main__':
    md_file = input("Enter the path to the markdown file: ")
    md_to_pdf(md_file)