from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    # Package Metadata
    name='demo',            # Package name (e.g. numpy)
    version='1.0',          # Version number
    author="thewwu",        # Author name
    author_email="",        # Author email
    license="",             # Package license (For open-source / commercial use)
    description="Demo package for project setup",           # 1-sentence summary
    long_description=long_description,                      # Detailed summary like README
    long_description_content_type="text/markdown",          # Format of long summary (e.g. text/x-rst)
    url="https://github.com/thewwu/python_project_setup",   # URL

    # Package Discovery
    packages=["demo"],          # Required package or find_packages() for auto-detection
    package_dir={'': 'src'},    # Mapping package names to directories

    # Dependency Management
    python_requires=">=3.10",               # Python version requirement
    setup_requires="setuptools>=68.2.2",    # Package required before running setup.py
    install_requires=["numpy>=1.18.5"],     # Package required for this package
    
    # Entry point
    entry_points={                          # Entry point for console
        'console_scripts': [
            'demo_run = demo.utils:run'
        ],
    },
)