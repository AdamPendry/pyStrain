#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simrep.stdplot import *

def plot_speed(ptph, tah):
  std_page_setup()
  fig   = plt.figure()
  ax    = fig.add_subplot(111) 
  
  ax.plot(ptph.t / cu_ms, ptph.y * 24 / cu_ms, 'k-', 
    label=r'Speed')
  
  if tah is not None:
    ax.axvline(x=tah / cu_ms, ls='-', color='darkslategrey', 
               label='AH formation')
  #

    
  ax.legend(loc='best')
  #ax.set_xlim(xmin=t.min() / cu_ms, xmax= t.max() / cu_ms)
  ax.set_ylim(ymin=0)
  ax.set_xlabel(r'$T_\mathrm{phys} \, [\mathrm{ms}]$')
  ax.set_ylabel(r'$T_\mathrm{phys}/T_\mathrm{cluster}\,[\mathrm{ms}/\mathrm{day}]$')
#

def main(opt, args):
  sd          = simdir.SimDir(opt.datadir)
  ptph        = sd.ts.scalar['physical_time_per_hour']
  tah         = sd.ahoriz.tformation
  
  plot_speed(ptph, tah)
  fp = os.path.join(opt.figdir, opt.figname)
  viz.savefig_multi(fp, opt.formats)
# 

desc    = "Plots computational speed in terms of physical time per computational time."
parser  = std_plot_option_parser(desc, 'computational_speed_global')
try_execute(parser, main)



