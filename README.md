# README

## Requirements
All requirements must be installed and set up for command line usage. For further detail, see the **Command Line Usage** section below.

We manage Python and R installations using miniconda. 
To build the repository as-is, the following applications are additionally required:

* git-lfs
* LyX
* R
* Stata

These software are used by the scripts contained in the repository. By default, the **Setup** and **Build** instructions below will assume their usage.

## Setup
**If you are using Windows, you may need to run certain bash commands in administrator mode due to permission errors. To do so, open your terminal by right clicking and selecting `Run as administrator`. To set administrator mode on permanently, refer to the [RA manual](https://github.com/gentzkow/template/wiki/Repository-Usage#Administrator-Mode).**

1. Create a `config_user.yaml` file in the root directory. A template can be found in the `setup` subdirectory. See the **User Configuration** section below for further detail.

2. If you already have conda setup on your local machine, feel free to skip this step. If not, this will install a lightweight version of conda that will not interfere with your current python and R installations.
Install miniconda and jdk to be used to manage the R/Python virtual environment, if you have not already done this. One easy way to do this is with homebrew, which if you do not have can be download [here](https://brew.sh/), from their websites [here](https://docs.conda.io/en/latest/miniconda.html) and [here](https://www.oracle.com/java/technologies/javase-downloads.html) or with your local package manager as follows:
   ```
   brew cask install miniconda
   brew cask install oracle-jdk
   ```
Once you have done this you need to initialize conda by running the following lines and restarting your terminal:
   ```
   conda config --set auto_activate_base false
   conda init $(echo $0 | cut -d'-' -f 2)
   ```

3. Create conda environment with the command:
   ```
   conda env create -f setup/conda_env.yaml
   ```

4. Run the `check_setup.py` file. One way to do this is to run the following bash command in a terminal from the `setup` subdirectory:
   ```
   python check_setup.py
   ```

5. Install Stata dependencies using the `setup_stata.do` file. We keep all non-base Stata ado files in the `lib` subdirectory, so even if you normally have a program installed, it will be re-installed. One way to download these stata dependencies is to use the following bash command from the `setup` subdirectory:
   ```
   stata-mp -e setup_stata.do
   ```

   If you are using a Windows, you will likely have to adjust this bash command:
   ```
   stata_executable -e setup_stata.do
   ```

   `stata_executable` refers to the name of your Stata executable. For example, if your Stata executable was located in `C:\Program Files\Stata15\StataMP-64.exe`, you would want to use the following bash command:

   ```
   StataMP-64 -e setup_stata.do
   ```

6. Install R dependencies that cannot be managed using conda with the `setup_r.r` file. One way to do this is to run the following bash command in a terminal from the `setup` subdirectory:
   ```
   Rscript setup_r.r
   ```
   
## Usage

Once you have succesfully completed the **Setup** section above, each time that you run any analysis make sure the virtual environment associated with this project is activated, using the command below (replacing with the name of this project).
```
   conda activate PROJECT_NAME
``` 
If you wish to return to your base installation of python and R you can easily deactivate this virtual environment using the command below:
```
   conda deactivate
``` 

## Build
**If you are using Windows, you may need to run certain bash commands in administrator mode due to permission errors. To do so, open your terminal by right clicking and selecting `Run as administrator`. To set administrator mode on permanently, refer to the [RA manual](https://github.com/gentzkow/template/wiki/Repository-Usage#Administrator-Mode).**

1. Follow the *Setup* instructions above.

2. From the root of repository, run the following bash command:
   ```
   python run_all.py
   ```

## Command Line Usage

For specific instructions on how to set up command line usage for an application, refer to the [RA manual](https://github.com/gentzkow/template/wiki/Command-Line-Usage).

By default, the repository assumes the following executable names for the following applications:

```
application : executable
python      : python
git-lfs     : git-lfs
lyx         : lyx
r           : Rscript
stata       : statamp (will need to be updated if using a version of Stata that is not Stata-MP)
```

These are the standard executable names for Mac and are likely to differ on your computer if you are using Windows. Executable names for Windows will typically look like the following:

```
application : executable
python      : python
git-lfs     : git-lfs
lyx         : LyX#.# (where #.# refers to the version number)
r           : Rscript
stata       : StataMP-64 (will need to be updated if using a version of Stata that is not Stata-MP or 64-bit)
```

Default executable names can be updated in `config_user.yaml`. For further detail, see the **User Configuration** section below.

## User Configuration
`config_user.yaml` contains settings and metadata such as local paths that are specific to an individual user and thus should not be committed to Git. For this repository, this includes local paths to [external dependencies](https://github.com/gentzkow/template/wiki/External-Dependencies) as well as executable names for locally installed software.

Required applications may be set up for command line usage on your computer with a different executable name from the default. If so, specify the correct executable name in `config_user.yaml`. This configuration step is explained further in the [RA manual](https://github.com/gentzkow/template/wiki/Repository-Structure#Configuration-Files).

## FAQ
1. Help! I'm running into permission errors when trying to install Python dependencies!

<br>

<img src="https://imgs.xkcd.com/comics/python_environment_2x.png" width="400" height="400">

<br>

In order to solve this problem, we try to isolate the python environment by creating a virtual environment in conda, so the python packages are written directly to locations managed by conda. If you run into any issues downloading packages with conda, you can use python's pip as follows:

The standard bash command for pip installing `requirements.txt` often runs into issues as depending on your Python environment, pip will attempt to install to a root directory (i.e., a directory that by default you should not have write permission)
```
python -m pip install -r requirements.txt
```

One way to get around this is to include `sudo` (or the Windows equivalent of running in administrative mode) in your bash command.
```
sudo python -m pip install -r requirements.txt
```

However, we caution against this (in particular for Macs) given the potential security risks. Instead, we recommend including the `--user` flag to your bash command.
```
python -m pip install --user -r requirements.txt
```

The `--user` flag instructs pip to install to a local directory (i.e., a directory that by default you should have write permission). If you are still running into permission errors, we recommend the following diagnostic steps:

   * Find the local directory that pip is attempting to install to. You can do this by either looking at the permission error message or using the following bash commands:
   ```
   python
   import site
   site.USER_SITE
   ```
   
   * If this is a directory that you should have write permission to but do not, use the `sudo chown` bash command (or the Windows equivalent of changing ownership through properties) to get ownership.

   * If this is a directory that you should not have write permission to, change your `PYTHONUSERBASE` environment variable to a directory that you should and do have write permission to.

If you are using Anaconda, we recommend using the following bash command:
```
conda install --file requirements.txt
```
Note that you may run into issues if any of the Python dependencies are not available on the conda channels. If this is the case, revert back to using `pip`.

## License
MIT License

Copyright (c) 2019 Matthew Gentzkow

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
