"""Post generation script to show README."""

print("\nREADME.md:")
with open("README.md") as readme_md:
    for line in readme_md.readlines():
        if "```" in line:
            continue
        print("\t" + line.rstrip())
