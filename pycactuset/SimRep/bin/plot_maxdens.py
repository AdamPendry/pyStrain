#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simrep.stdplot import *

def plot_maxdens(maxrho):
  std_page_setup()
  fig   = plt.figure()
  ax    = fig.add_subplot(111) 

  ax.plot(maxrho.t / cu_ms, maxrho.y * CU.density, '-')  
  ax.set_xlim(xmin=maxrho.t.min() / cu_ms, xmax= maxrho.t.max() / cu_ms)
  ax.set_xlabel(r'$t / \mathrm{ms}$')
  ax.set_ylabel(r'$\max(\rho) / (\mathrm{kg}\,\mathrm{m}^{-3})$')
  ax.grid(True)
#


def main(opt, args):
  sd          = simdir.SimDir(opt.datadir)
  maxrho      = sd.ts.max['rho']
  plot_maxdens(maxrho)
  viz.savefig_multi(os.path.join(opt.figdir, opt.figname), opt.formats)
# 

desc    = "Plots evolution of maximum density."
parser  = std_plot_option_parser(desc, 'evol_maxdens')
try_execute(parser, main)








