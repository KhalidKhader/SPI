from setuptools import setup

setup(
    name="email-notification",
    version="1.0.0",
    packages=["services"],  
    entry_points={
        "notification.plugins": [
            "email = services.email_service:EmailService", 
        ],
    },
    install_requires=[],
)
