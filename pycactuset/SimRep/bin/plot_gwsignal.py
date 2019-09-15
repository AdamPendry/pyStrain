#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simrep.stdplot import *


def plot_moncr_lm(l, m, d, qe, qo, target, formats):
  std_page_setup()

  fig   = plt.figure()
  ax    = fig.add_subplot(111) 

  clrs = ['k','b','r','g','y','m', 'Aqua', 'BlueViolet', 'DarkOrange', 
          'DarkSlateGrey', 'Maroon']
  clrs.reverse()

  
  lbl_odd_re = "$\Re(Q_{odd}), l=%d, m=%d$" % (l, m)
  lbl_even_re = "$\Re(Q_{even}), l=%d, m=%d$" % (l, m)
  lbl_odd_im = "$\Im(Q_{odd}), l=%d, m=%d$" % (l, m)
  lbl_even_im = "$\Im(Q_{even}), l=%d, m=%d$" % (l, m)
  
  ax.plot((qe.t-d) / cu_ms, qe.y.real, '-', label=lbl_even_re, color=clrs.pop())
  ax.plot((qe.t-d) / cu_ms, qe.y.imag, '-', label=lbl_even_im, color=clrs.pop())
  ax.plot((qo.t-d) / cu_ms, qo.y.real, '-', label=lbl_odd_re, color=clrs.pop())
  ax.plot((qo.t-d) / cu_ms, qo.y.imag, '-', label=lbl_odd_im, color=clrs.pop())
  #
  ax.legend(loc='best')
  #ax.set_xlim(xmin=minlapse.t.min() / cu_ms, xmax= minlapse.t.max() / cu_ms)
  ax.set_xlabel(r'$(t - r) / \mathrm{ms}$')
  ax.set_ylabel(r'$Q$')
  #ax.grid(True)
  tf = "%s_l%d_m%d" % (target, l, m)
  viz.savefig_multi(tf, formats)
  plt.close(fig)
#

def plot_moncr_all(det, tform, target, formats):
  for l in det.available_l:
    dmax      = det.available_dist[-1]
    for m in range(0, l+1):
      if det.has_detector(l, m, dmax):
        try:
          qe,qo = det.get_Q(l, m, dmax)
          if (max(max(abs(qe.y)),max(abs(qo.y))) > 1e-10):
            plot_moncr_lm(l, m, dmax, qe, qo, target, formats)
          #
        except Exception,inst:
          print "failed to process l=%d, m=%d, d=%.4e (%s)" % (l,m, dmax, inst)
        #
      #
    #
  #
#

def plot_psi4_lm(l, m, d, p4, target, formats):
  std_page_setup()

  fig   = plt.figure()
  ax    = fig.add_subplot(111) 

  lbl_re = "$r \Re(\Psi_4), l=%d, m=%d$" % (l, m)
  lbl_im = "$r \Im(\Psi_4), l=%d, m=%d$" % (l, m)
  
  ax.plot((p4.t-d) / cu_ms, d*p4.y.real, '-', label=lbl_re, color='b')
  ax.plot((p4.t-d) / cu_ms, d*p4.y.imag, '-', label=lbl_im, color='r')
  #
  ax.legend(loc='best')
  #ax.set_xlim(xmin=minlapse.t.min() / cu_ms, xmax= minlapse.t.max() / cu_ms)
  ax.set_xlabel(r'$(t - r) / \mathrm{ms}$')
  ax.set_ylabel(r'$r\Psi_4$')
  #ax.grid(True)
  tf = "%s_l%d_m%d" % (target, l, m)
  viz.savefig_multi(tf, formats)
  plt.close(fig)
#

def plot_h_lm(l, m, d, hp, hc, tform, tmin, target, formats):
  std_page_setup()

  fig   = plt.figure()
  ax    = fig.add_subplot(111) 

  lbl_hp = "$r h^+, l=%d, m=%d$" % (l, m)
  lbl_hc = "$r h^\\times, l=%d, m=%d$" % (l, m)
  mpc = 1e6 * unitconv.PARSEC_SI / CU.length
  ax.plot((hp.t-d) / cu_ms, hp.y / mpc, '-', label=lbl_hp, color='b')
  ax.plot((hc.t-d) / cu_ms, hc.y / mpc, '-', label=lbl_hc, color='r')
  if (tform != None):
    ax.axvline(x=tform / cu_ms, label='AH found', color='g', linewidth=2)
  #
  ax.legend(loc='best')
  hmin = min(min(hp.y), min(hc.y))
  hmax = max(max(hp.y), max(hc.y))
  ax.set_ylim(ymin=1.3 * hmin / mpc, ymax=1.3 * hmax / mpc)
  ax.set_xlim(xmin=tmin)
  ax.set_xlabel(r'$(t - r) / \mathrm{ms}$')
  ax.set_ylabel(r'$r h / \mathrm{MPc}$')
  #ax.grid(True)
  tf = "%s_l%d_m%d" % (target, l, m)
  viz.savefig_multi(tf, formats)
  plt.close(fig)
#


def plot_heff_lm(l, m, d, f, heff, target, formats):
  std_page_setup()

  fig   = plt.figure()
  ax    = fig.add_subplot(111) 

  lbl = "$d f \\tilde{h}(f), l=%d, m=%d$" % (l, m)

  mpc = 1e6 * unitconv.PARSEC_SI / CU.length
  ax.semilogy(f * cu_ms, heff / mpc, '-', label=lbl, color='b')

  ax.legend(loc='best')
  fmax  = (f[heff>heff.max()*1e-2]).max()
  #hmin = min(min(hp.y), min(hc.y))
  #hmax = max(max(hp.y), max(hc.y))
  ax.set_xlim(xmin=0, xmax=fmax *cu_ms)
  ax.set_ylim(ymin=1e-3*heff.max()/ mpc, ymax=1.5*heff.max()/ mpc)
  ax.set_xlabel(r'$f / \mathrm{kHz}$')
  ax.set_ylabel(r'$d f \tilde{h} / \mathrm{MPc}$')
  #ax.grid(True)
  tf = "%s_l%d_m%d" % (target, l, m)
  viz.savefig_multi(tf, formats)
  plt.close(fig)
#


def plot_psi4_all(det, tform, basen, formats, w0, tmin):
  dmax      = det.available_dist[-1]
  for l in det.available_l:
    for m in range(0, l+1):
      if det.has_detector(l, m, dmax):
        try:
          psi4 = det.get_psi4(l, m, dmax)
          if (dmax*max(abs(psi4.y)) > 1e-10):
            plot_psi4_lm(l, m, dmax, psi4, basen+'psi4_outer' , formats)
            hp,hc = det.get_strain(l, m, dmax, w0/CU.freq)
            plot_h_lm(l, m, dmax, hp, hc, tform, tmin, basen+'strain', formats)
            f,heff = det.get_eff_strain(l, m, dmax, w0/CU.freq)
            plot_heff_lm(l, m, dmax, f, heff, basen+ 'spec', formats)
          #
        except Exception,inst:
          print "failed to process l=%d, m=%d, d=%.4e (%s)" % (l,m, dmax, inst)
        #
      #
    #
  #
#


def main(opt, args):
  sd          = simdir.SimDir(opt.datadir)
  basen       = os.path.join(opt.figdir, opt.figname)
  all_moncr   = sd.gwmoncrief
  all_psi4    = sd.gwpsi4mp  
  thform      = sd.ahoriz.tformation
  plot_moncr_all(all_moncr, thform, basen+'moncr_outer', opt.formats)
  plot_psi4_all(all_psi4, thform, basen, opt.formats, opt.fcut, opt.tmin)
# 

desc    = "Plots GW signal from Psi_4 and Moncrief formalism, as well as strain and spectra."
parser  = std_plot_option_parser(desc, 'gw_')
parser.add_option('--fcut',  type='float',  default=500.0, 
                  help="Angular frequency cutoff for integration.")
parser.add_option('--tmin',  type='float',  default=0, 
                  help="Omit evolution before time tmin")

try_execute(parser, main)











