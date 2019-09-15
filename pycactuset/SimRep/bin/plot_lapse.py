#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simrep.stdplot import *

def plot_lapse(minlapse, maxlapse):
  std_page_setup()

  fig   = plt.figure()
  ax    = fig.add_subplot(111) 
  ax.plot(minlapse.t / cu_ms, minlapse.y, '-', label=r'$\min(\alpha)$')
  if maxlapse:
    ax.plot(maxlapse.t / cu_ms, maxlapse.y, '-', label=r'$\max(\alpha)$')
  ax.legend(loc='best')
  ax.set_xlim(xmin=minlapse.t.min() / cu_ms, xmax= minlapse.t.max() / cu_ms)
  ax.set_xlabel(r'$t / \mathrm{ms}$')
  ax.set_ylabel('Lapse')
  ax.grid(True)
#

def main(opt, args):
  sd          = simdir.SimDir(opt.datadir)
  minlapse    = sd.ts.min['alp']
  maxlapse    = sd.ts.max.get('alp')
  plot_lapse(minlapse, maxlapse)
  viz.savefig_multi(os.path.join(opt.figdir, opt.figname), opt.formats)
# 

desc    = "Plots evolution of lapse."
parser  = std_plot_option_parser(desc, 'evol_lapse')
try_execute(parser, main)









