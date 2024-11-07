from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  
    entry_points={
        "console_scripts": [
            "math_quiz = math_quiz.math_quiz:math_quiz",  
        ],
    },
    author="Javier de Castro Poy",
    author_email="javierdcp@hotmail.es",
    description="A math quiz game.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/javierdcp20/dsss_homework_2",  #  URL  GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
