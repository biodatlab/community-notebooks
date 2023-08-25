from setuptools import setup

setup(
    name='gpt_business_use_case',
    python_requires='>=3.9',
    install_requires=[
        'openai==0.27.8',
        'beautifulsoup4==4.12.2',
        'pandas==2.0.3',
        'python-docx==0.8.11',
        'markdown==3.4.4'
    ]
)