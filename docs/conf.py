project = 'Thunderbird'
author = 'Thunderbird'
release = '1.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']   

html_js_files = [
    'chatbot.js',
]
html_favicon = '_static/favicon.png'

html_context = {
    'bing_verification_code': 'EF0D113A83DA6960716D3F3EB33D127B'
}

extensions = [
    'sphinx_sitemap',
]

html_baseurl = 'https://docs.yourdomain.com/'
