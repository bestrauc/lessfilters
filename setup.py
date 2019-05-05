from setuptools import setup

setup(
    name="less-preprocessors",
    version="0.1",
    scripts = [
        'preprocessors/bcl_view.py',
        'preprocessors/dicom_header.py'
    ],
    install_requires=["pydicom"],
)
