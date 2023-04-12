import setuptools
import subprocess
import os

version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in version:
    # https://peps.python.org/pep-0440/#local-version-segments
    v, i, s = version.split("-")
    version = v + "+" + i + ".git." + s

assert "-" not in version
assert "." in version

assert os.path.isfile("torchgating/version.py")
with open("torchgating/version.py", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % f"__version__ = '{version}'")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="torchgating",
    version=version,
    author="Asaf Zorea",
    author_email="zoreasaf@gmail.com",
    description="A PyTorch-based implementation of Spectral Gating, an algorithm for denoising audio signals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/nuniz/TorchSpectralGating",
    packages=setuptools.find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "tests.*"]),
    include_package_data=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["torchgating = torchgating.run:main"]},
    install_requires=[
        "matplotlib >= 3.7.1",
        "numpy >= 1.24.2",
        "soundfile >= 0.11.0",
        "torch >= 2.0.0",
    ],
)
