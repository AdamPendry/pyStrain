#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simrep.stdplot import *

def plot_temp(mintemp, maxtemp, thform):
  std_page_setup()

  fig   = plt.figure()
  ax    = fig.add_subplot(111) 

  if mintemp:
    ax.plot(mintemp.t / cu_ms, mintemp.y, '-', label=r'$\min(T)$')
  if maxtemp:
    ax.plot(maxtemp.t / cu_ms, maxtemp.y, '-', label=r'$\max(T)$')
  #if l1temp:
  #  ax.plot(l1temp.t / cu_ms, l1temp.y, '-', label=r'$L_1(T)$')
  if (thform != None):
    ax.axvline(x=thform / cu_ms, label='AH found', color='k', linewidth=2)
  #
  ax.legend(loc='best')
  ax.set_xlim(xmin=mintemp.t.min() / cu_ms, xmax= mintemp.t.max() / cu_ms)
  ax.set_xlabel(r'$t / \mathrm{ms}$')
  ax.set_ylabel(r'$T / \mathrm{MeV}$')
  ax.grid(True)

#

def main(opt, args):
  sd          = simdir.SimDir(opt.datadir)
  mintemp    = sd.ts.min.get('temperature')
  maxtemp    = sd.ts.max.get('temperature')
  #l1temp     = sd.ts.norm1.get('temperature')
  thform     = sd.ahoriz.tformation
  if not any([mintemp, maxtemp]):
    raise RuntimeError("No data found")
  #
  plot_temp(mintemp, maxtemp, thform)
  viz.savefig_multi(os.path.join(opt.figdir, opt.figname), opt.formats)
# 

desc    = "Plots evolution of temperature."
parser  = std_plot_option_parser(desc, 'evol_temp')
try_execute(parser, main)




