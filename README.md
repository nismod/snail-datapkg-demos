# snail-datapkg-demos

This repository contains projects that demonstrate how to analyse risks to
infrastructure using snail and starter data kits.

## Setup

First clone this repository to your machine:

```bash
git clone git@github.com:nismod/snail-datapkg-demos.git

# Alternative ways:
# Using the HTTPS URL:
# git clone https://github.com/nismod/snail-datapkg-demos.git
# Using the GitHub CLI:
# gh repo clone nismod/snail-datapkg-demos
```

We recommend using an environment manager to install the necessary version of
Python and several package dependencies.

Follow the install instructions for `conda` using
[miniforge](https://conda-forge.org/download/)

```bash
conda create -f environment.yml -y
```

Or, for a slightly less well-known but similar option, there is the relatively
lightweight
[`micromamba`](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)


```bash
micromamba create -f environment.yml -y
```

Then, each time you open a terminal or command-line, run the command for conda/micromamba
to activate the environment:

```bash
conda activate snail-datapkg
micromamba activate snail-datapkg
```

If this worked, you should be able to run Python to see the installed version, and import
some of the packages that we'll use:

```bash
python -V
# Python 3.12.15
python -c 'import snail; print(snail.__version__)'
# 0.5.4
python -c 'import snkit; print(snkit.__version__)'
# 1.9.0
```

## Acknowledgments

> MIT License
>
> Copyright (c) 2025-26 Tom Russell, Silvia Colombo, Raghav Pant and all
> [contributors](https://github.com/nismod/snail-datapkg-demos/graphs/contributors)

This library is developed by researchers in the [Oxford Programme for
Sustainable Infrastructure Systems](https://opsis.eci.ox.ac.uk/) at the
University of Oxford, funded by multiple research projects.

This research received funding from the FCDO Climate Compatible Growth
Programme. The views expressed here do not necessarily reflect the UK
government's official policies.
