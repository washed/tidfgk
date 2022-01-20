import glob
import re
import subprocess

TLLOCALMGR = "/usr/bin/tllocalmgr"

pattern = re.compile("\\\\usepackage.*\\{(.+)\\}")
tex_files = glob.glob('**/*.tex', recursive=True)

packages = []

for tex_file in tex_files:
    with open(tex_file) as file:
        lines = file.readlines()
        for line in lines:
            match = pattern.match(line.strip())
            if match:
                packages.append(match.group(1))

# for package in packages:
subprocess.run([TLLOCALMGR, "install", *packages])
subprocess.run([TLLOCALMGR, "texhash"])
