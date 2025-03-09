from setuptools import setup, find_packages

setup(
    name="spam_email_classifier",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "Django>=4.0",
        "djangorestframework",
        "gunicorn",
        "numpy",
        "pandas",
        "scikit-learn",
        "gensim",
        "joblib",
        "django-cors-headers"
    ],
    entry_points={
        "console_scripts": [
            "spam_classifier_manage = backend.manage:main",
        ],
    },
)
