from setuptools import setup, find_packages

setup(
    name="AliceLostInWonderland",  
    version="0.1.0",  
    author="Daki0903", 
    author_email="",  
    description="A text-based adventure game inspired by Alice in Wonderland.",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    url="https://github.com/tvojkorisnickinaziv/AliceLostInWonderland",  
    packages=find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=[  
        "pygame>=2.1.0",
    ],
    entry_points={  
        "console_scripts": [
            "alice-game=alice_game.main:main",  
        ],
    },
)
