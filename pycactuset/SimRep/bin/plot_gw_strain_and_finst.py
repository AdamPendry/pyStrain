#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simrep.stdplot import *
from postcactus import gw_utils

dashed  = (5,3)
dotted  = (2,2)
dshdot  = (1,2,5,2)
solid   = (None, None)

def plot_spec(hp,hc,fip4,gwpks):
  std_page_setup()

  clrhp   = 'darkslategrey' #'darkgreen'
  clrhc   = 'darkred'
  clrfi   = 'darkblue'
  clrpks  = 'darkslategrey'

  fig, ax = plt.subplots(2, 1, sharex=True)
  plt.subplots_adjust(hspace=0.1,bottom=0.14)

  ax[1].plot(fip4.t/cu_ms, fip4.y/cu_kHz, color=clrfi, dashes=solid,
             lw=1, label=r'GW')
  
  ax[1].set_xlabel(r'$(t-r)\, [\mathrm{ms}]$')
  #ax[1].legend(loc='upper left')#, ncol=2)
  #ax[1].set_ylim(ymin=-1)
  ax[1].set_ylim(ymin=0, ymax=1.1*max(fip4.y) / cu_kHz)
  ax[1].set_ylabel(r'$f \,[\mathrm{kHz}]$')
  ax[1].xaxis.set_minor_locator(AutoMinorLocator())
  ax[1].yaxis.set_minor_locator(AutoMinorLocator())
  
  mpc = 1e6 * unitconv.PARSEC_SI / CU.length
  uh  = 100*mpc
  
  ax[0].plot(hp.t / cu_ms , hp.y / uh, color=clrhp, 
            dashes=solid, lw=1, label=r'$h^+$')
  ax[0].plot(hc.t / cu_ms , hc.y / uh, color=clrhc, 
            dashes=solid, lw=1, label=r'$h^\times$')

  
  for pf,pa in gwpks[:4]:
    ax[1].axhline(y=pf / cu_kHz, color=clrpks, dashes=dotted)
  #
  
  ax[0].legend(loc='upper left', ncol=2)
  ax[0].set_xlim(xmin=hp.t[0] / cu_ms, xmax= hp.t[-1] / cu_ms)
  ax[0].set_ylabel(r'$h \, r_\mathrm{ex} / (100\, \mathrm{MPc})$')
  ax[0].xaxis.set_minor_locator(AutoMinorLocator())
  ax[0].yaxis.set_minor_locator(AutoMinorLocator())

#


def find_peaks(x, y, width, cutamp=0, xmin=None, xmax=None, 
               sortpks=True):
  dx    = x[1]-x[0]
  xmin  = x[0]  if xmin is None else float(xmin)
  xmax  = x[-1] if xmax is None else float(xmax)
  slen  = max(1,int(width/dx))
  imin  = max(slen, int((xmin-x[0])/dx))
  imax  = min(len(x)-slen, int((xmax-x[0])/dx))
  ycut  = cutamp * max(y[imin:imax])
  pks   = []
  for i in arange(imin, imax): 
    mr = max(max(y[(i-slen):i]), max(y[(i+1):(i+slen+1)]))
    if (y[i] > mr) and (y[i]>ycut):
      pks.append((y[i],x[i]))
    #
  #
  if sortpks:
    pks = sorted(pks)
    pks.reverse()
  #
  return [(x,a) for a,x in pks]
#



def load_data(dd, l, m, fcut, tsmooth, fmin, fmax, fsep, cutamp):  

  sd      = simdir.SimDir(dd)
  tah     = sd.ahoriz.tformation

  dist    = sd.gwpsi4mp.outermost
  psi4    = sd.gwpsi4mp.get_psi4(l,m, dist)


  fip4    = psi4.phase_avg_freq(tsmooth)
  fip4.y *= -1
  fip4.t -= dist 
  fip4.clip(tmin=cu_ms, tmax=tah)

  
  # Effective strain spectrum
  f,heff  = gw_utils.eff_strain_from_psi4(psi4, dist)
  
  # Peaks of strain spectrum.
  pks     = find_peaks(f, heff, fsep, cutamp, fmin, fmax)  
  
  hp,hc   = sd.gwpsi4mp.get_strain(l, m, dist, 2*pi*fcut) 
  hp.t    -= dist
  hc.t    -=dist

  return hp,hc,fip4,pks
#

  
def main(opt, args):
  if (opt.m==0):
    raise RuntimeError('No phase velocity for m=0 (real valued signal)') 
  #
  tsmooth     = opt.tsmooth * cu_ms
  fcut        = opt.fficut * cu_kHz
  pkfmin      = opt.pkfmin * cu_kHz
  pkfmax      = opt.pkfmax * cu_kHz
  pkfsep      = opt.pkfsep * cu_kHz

  data        = load_data(opt.datadir, opt.l, opt.m, fcut, tsmooth, 
                          pkfmin, pkfmax, pkfsep, opt.pkacut)
  plot_spec(*data)
  fn   = "%s_l%dm%d" % (opt.figname, opt.l, opt.m)
  fign = os.path.join(opt.figdir, fn)
  viz.savefig_multi(fign, opt.formats)
# 

desc    = "Plots GW strain and instantanuous frequency for l=m=2."
parser  = std_plot_option_parser(desc, 'gw_strain_and_finst')
parser.add_option('-l',  type='int',  default=2, 
                  help="l multipole.")
parser.add_option('-m',  type='int',  default=2, 
                  help="m multipole.")
parser.add_option('--fficut',  type='float',  default=0.5, 
                  help="Angular frequency cutoff for integration [kHz].")
parser.add_option('--tsmooth',  type='float',  default=0.1, 
                  help="Smoothing timescale for instantaneous frequency [ms].")
parser.add_option('--pkfmin',  type='float',  default=1.5, 
                  help="Peak search minimum frequency [kHz].")
parser.add_option('--pkfmax',  type='float',  default=7.0, 
                  help="Peak search maximum frequency [kHz].")
parser.add_option('--pkfsep',  type='float',  default=0.2, 
                  help="Peak search minimum separation [kHz].")
parser.add_option('--pkacut',  type='float',  default=0.05, 
                  help="Peak search amplitude cutoff.")
                   
                  


try_execute(parser, main)











