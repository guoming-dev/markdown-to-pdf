# 📄 Markdown to PDF Converter

A simple Python script to convert Markdown (.md) files to PDF using WeasyPrint. Designed to help you convert your notes, documentation, or any Markdown file into a well-formatted PDF with custom styling.

## 🚀 Features

- ✅ Convert Markdown files to PDF with ease
- ✅ Supports tables, lists, code blocks, and inline code
- ✅ Customizable HTML and CSS styling for PDFs
- ✅ Handles file validation and error handling
- ✅ Lightweight and easy to set up

---

## 📦 Requirements

- Python 3.8+
- WeasyPrint
- Markdown

Ensure you have the necessary system dependencies for WeasyPrint based on your OS. [WeasyPrint Installation Guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

---

## ⚙️ Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/guoming-dev/markdown-to-pdf.git
   cd markdown-to-pdf
   ```
2. Create a virtual environment (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

1. **Place your Markdown file** in the project directory or provide its path.
2. **Run the script**:
   ```bash
   python markdown-to-pdf.py
   ```
3. **Input the Markdown file path** when prompted:
   ```bash
   Enter the path to the markdown file: example.md
   ```
4. The **PDF** will be generated in the **same directory** as your `.md` file.

---

## 📋 Example

Given an `example.md` with the following content:

```
# Hello, World!

This is a simple **Markdown** file.

## Features

- Easy to use
- Lightweight
- Fast

```python
print("Convert markdown to pdf.")

Run the script:

```bash
python markdown-to-pdf.py
```

You'll get `example.pdf` with the same structure, styled via **CSS**.

---

## 🎨 Customization

The script uses basic HTML and CSS to style the generated PDF. You can customize:

- Fonts
- Colors
- Code block themes
- Table styles

Edit the CSS section in `markdown-to-pdf.py` to match your desired PDF style.

---

## 🧑‍💻 Contributing

Contributions are welcome! 🚀

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a **Pull Request**

---

## 🐛 Issues & Feedback

If you encounter any issues or have suggestions, feel free to open an [Issue](https://github.com/guoming-dev/markdown-to-pdf/issues/new).

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

- [WeasyPrint](https://weasyprint.org/) for PDF rendering.
- [Python-Markdown](https://python-markdown.github.io/) for Markdown to HTML conversion.
- Inspired by the journey through Harvard CS50P’s File I/O module.