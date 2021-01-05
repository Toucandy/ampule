Ampule (Automated MatPlotLib) is a minimalistic tool designed for repeated 
non-interactive processing and plotting of tabular data

##Prerequisites

You need a Linux distribution, python3 installed, and knowledge (or desire to 
learn) of Matplotlib library.

##Features

####Easy import, post-processing and plotting of tabular data

Data are to be stored on disk in the following DSV-like format

    #:x f g
    0.01 0.01 0.0001
    0.02 0.02 0.0004
    0.03 0.03 0.0009
    0.04 0.04 0.0016
    0.05 0.05 0.0025
    0.06 0.06 0.0036

The import is simple

    data, _ = ampule.load(f'dat/poly.dat')

After import, columns are accessed as `data.x`, `data.f` and `data.g`.
The data class is `pandas.DataFrame`, so expressions like `data.f + data.g/2` 
work too. Also you get compatibility with data processing functions from 
numpy, scipy, pandas etc.

However, you don't need to know these libraties for plotting using Matplotlib, 
just pass the columns to the plotter

    plt.plot(data.x, data.f, label = r'$f(x)$')
    plt.plot(data.x, data.g, label = r'$g(x)$')

####Makefile for mass (re)building of output plots

Let's say you have written a script for data plotting, and want to update the 
picture after receving fresh data. Or you decided to prettify your plot and 
have changed the script itself. It couldn't be easier

    make

Ampule will automatically rebuild those and only those pictures for which the 
data or plotting script have changed. For this to work, special dependency 
files are stored (similar to ones producing by `gcc -MT`)

####Import by mask

When you have a lot of data files, you may start giving them parametric names, 
like `H_0.dat`, `H_1.dat`, `H_2.dat` ...
Say no more

    for path, k in search_mask('dat/hermite/H_', '.dat'):
        data, _ = ampule.load(path)
        plt.plot(data.x, data.H, label = rf'$H_{k}$')

####Reproducible plots

Sometimes it is needed for the pictures do not change if they are plotted on 
the same data, especially if you decide to store pictures under version 
control system.  This behavior is supported and enabled by default. If you 
refactor the script without changing its essence, the pictures will not change 
either.

####Metadata support

In addition, you can store some meta-information as follows:

    #:foo=0
    #:bar='bar'

Such variables must be written one per line, and strictly before the column 
names. The work with metadata is straightforward

    data, meta = ampule.load('dat/data.dat')
    print(meta.foo, meta.bar)

##Get started
