#!/usr/bin/env python3

"""Print DICOM headers, without the pixel data."""

import sys

import pydicom

dcm_path = sys.argv[1]
dcm = pydicom.dcmread(dcm_path)
try:
    print(dcm)
except Exception as e:
    print(f"Invalid DICOM header: {e}")


