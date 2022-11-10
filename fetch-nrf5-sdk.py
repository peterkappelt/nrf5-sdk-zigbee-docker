"""
Fetch and unpack a specific version of Nordic nRF5 SDK for Thread and Zigbee
See: https://www.nordicsemi.com/Products/Development-software/nRF5-SDK-for-Thread-and-Zigbee
"""

from argparse import ArgumentParser
from tempfile import TemporaryDirectory
import zipfile
import requests
import os
import shutil

sdk_versions = {
    "4.2.0": "https://www.nordicsemi.com/-/media/Software-and-other-downloads/SDKs/nRF5-SDK-for-Thread/nRF5-SDK-for-Thread-and-Zigbee/nRF5_SDK_for_Thread_and_Zigbee_v4.2.0_af27f76.zip",
    "4.1.0": "https://www.nordicsemi.com/-/media/Software-and-other-downloads/SDKs/nRF5-SDK-for-Thread/nRF5-SDK-for-Thread-and-Zigbee/nRF5SDKforThreadv41.zip",
    "4.0.0": "https://www.nordicsemi.com/-/media/Software-and-other-downloads/SDKs/nRF5-SDK-for-Thread/nRF5-SDK-for-Thread-and-Zigbee/nRF5SDKforThreadandZigbeev400dc7186b.zip",
    "3.2.0": "https://www.nordicsemi.com/-/media/Software-and-other-downloads/SDKs/nRF5-SDK-for-Thread/nRF5-SDK-for-Thread-and-Zigbee/nRF5SDKforThreadandZigbeev3209fade31.zip"    
}

parser = ArgumentParser(
    description="Download and unpack Nordic nRF5 SDK for Thread and Zigbee.\nThe script will output the folder where the sdk was extracted to.")
parser.add_argument(
    "SDK_VERSION", help="SDK version to fetch. One of " + ", ".join(sdk_versions.keys()))

if __name__ == "__main__":
    args = parser.parse_args()
    requested_sdk_version = args.SDK_VERSION
    if not requested_sdk_version in sdk_versions.keys():
        print("Unknown SDK version!")
        exit(1)

    with TemporaryDirectory() as tmp_dl, TemporaryDirectory() as tmp_zip:
        res = requests.get(sdk_versions[requested_sdk_version], stream=True)
        with open(f"{tmp_dl}/{requested_sdk_version}.zip", "wb") as fd:
            for chunk in res.iter_content(chunk_size=8192):
                fd.write(chunk)

        dest_dir = f"nRF5_SDK_Thread_Zigbee_{requested_sdk_version}"

        with zipfile.ZipFile(f"{tmp_dl}/{requested_sdk_version}.zip", "r") as zip:
            zip.extractall(f"{tmp_zip}/{dest_dir}")
        shutil.move(f"{tmp_zip}/{dest_dir}", ".")

        print(dest_dir)
