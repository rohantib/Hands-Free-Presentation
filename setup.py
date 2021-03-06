import platform
import json
import os

platform_info = platform.system()
if platform_info in ("Windows", "Microsoft"):
    print("Sorry, but Windows is currently not supported for this application. If you really wish to run it, "
          "you can install Bash on Windows 10 and run this application through there.")
    raise SystemExit

snowboy_package_dest = None

if platform_info == "Darwin":
    print("Setting up application for use with OSX binaries...")
    snowboy_package_dest = "./snowboy/OSX"
else:
    dist_info = platform.linux_distribution()
    if "ubuntu" in dist_info[0].lower():
        version_num = int(dist_info[1].split('.')[0])
        if version_num < 14:
            print("Setting up application for use with Ubuntu 12.04 binaries...")
            snowboy_package_dest = "./snowboy/ubuntu_12"
        else:
            print("Setting up application for use with Ubuntu 14.04 binaries...")
            snowboy_package_dest = "./snowboy/ubuntu_14"
    elif dist_info[0].lower() == "linuxmint":
        version_num = int(dist_info[1])
        if version_num < 15:
            print("Setting up application for use with Ubuntu 12.04 binaries...")
            snowboy_package_dest = "./snowboy/ubuntu_12"
        else:
            print("Setting up application for use with Ubuntu 14.04 binaries...")
            snowboy_package_dest = "./snowboy/ubuntu_14"
    else:
        print('Your system is not one of the systems that the setup script automatically supports. '
              'Ubuntu 14.04 binaries are being used by default. If the application fails to run, and you are certain'
              'that all dependencies are installed, manually set the application to use 12.04 binaries by editing'
              'the ".snowboy_path" file to contain ".snowboy/ubuntu_12". If that still does not work, then your '
              'system is not supported for this application.')
        snowboy_package_dest = "./snowboy/ubuntu_14"

with open(".snowboy_path", "w") as package_file:
    package_file.write(snowboy_package_dest)


json_data = {
    "models": [
        os.path.abspath("./models/ex_next_slide.pmdl"),
        os.path.abspath("./models/ex_previous_slide.pmdl")
    ],
    "sensitivity": 0.5,
    "resource": os.path.abspath("./resources/common.res")
}
with open("config.json", "w") as json_file:
    json.dump(json_data, json_file)

print("Setup successful!")
