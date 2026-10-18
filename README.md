# Static Site Generator

A static site generator written in Python, built as part of the Boot.dev backend curriculum. It turns a folder of Markdown files into a complete HTML website using a single template, with no third-party libraries and no external Markdown parser.

Live demo: [Ravinder2102.github.io/static-site-generator](https://Ravinder2102.github.io/static-site-generator/)

## Features

- Converts Markdown files into HTML pages using a shared template
- Block-level Markdown: headings (`#` to `######`), paragraphs, block quotes, code blocks, unordered lists, and ordered lists
- Inline Markdown: **bold**, _italic_, `inline code`, links, and images
- Recursively processes every file in `content/`, keeping the folder structure
- Copies static assets (CSS, images) into the output folder
- Configurable base path so links and images work on GitHub Pages
- Unit tests for the parsing and rendering logic

## Prerequisites

- Python 3.10 or later

## Getting Started

```bash
git clone https://github.com/Ravinder2102/static-site-generator.git
cd static-site-generator
```

### Build and preview locally

```bash
bash main.sh
```

This builds the site into `docs/` and serves it at [http://localhost:8888](http://localhost:8888). Press `Ctrl+C` to stop the server.

### Build for GitHub Pages

```bash
bash build.sh
```

This builds into `docs/` with the base path `/static-site-generator/`, so links and images resolve correctly when the site is hosted on GitHub Pages. If you fork this repo, your site will be at `https://<your-username>.github.io/static-site-generator/`.

If your repository has a different name, edit the base path in `build.sh`.

To publish:

1. Commit and push the `docs/` folder.
2. On GitHub, go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, then select your `main` branch and the `/docs` folder.

### Run the tests

```bash
bash test.sh
```

## Writing Content

Add Markdown files to the `content/` folder. Each file becomes an HTML page at the same path, so `content/blog/first-post.md` becomes `docs/blog/first-post.html`.

Every Markdown file **must start with a `# Heading`** (an h1). It is used as the page title, and the build fails if none is found.

Example `content/index.md`:

````markdown
# My Site

Welcome to my **first** page. Read the [blog](/blog/first-post.html).

- Fast
- Simple
- Static
````

Static files such as `index.css` and images go in the `static/` folder and are copied to the root of the output folder.

### Supported Markdown

| Element       | Syntax                      |
| ------------- | --------------------------- |
| Heading       | `# H1` through `###### H6`  |
| Paragraph     | Text separated by blank lines |
| Bold          | `**bold**`                  |
| Italic        | `_italic_`                  |
| Inline code   | `` `code` ``                |
| Link          | `[text](url)`               |
| Image         | `![alt](url)`               |
| Block quote   | `> quote`                   |
| Code block    | Three backticks on their own lines |
| Unordered list | `- item`                   |
| Ordered list  | `1. item` (starting at 1)   |

### Limitations

- Inline styles can't be nested, and italic uses `_underscores_` only.
- Lists can't be nested, and code blocks don't support language tags.

## How It Works

1. **Clean:** the `docs/` folder is deleted.
2. **Copy:** everything in `static/` is copied into `docs/`.
3. **Read:** each file in `content/` is read, along with `template.html`.
4. **Split into blocks:** the Markdown is split on blank lines, and each block's type is detected.
5. **Parse inline text:** text within blocks is split into `TextNode`s for bold, italic, code, links, and images.
6. **Build the tree:** `TextNode`s become `HTMLNode`s (`LeafNode` and `ParentNode`), which are assembled into one `<div>`.
7. **Render:** the HTML is inserted into the template at `{{ Content }}`, the title at `{{ Title }}`, and the base path is applied to every `href="/` and `src="/` in the page.