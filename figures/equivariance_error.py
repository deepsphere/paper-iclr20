import matplotlib
from matplotlib.lines import Line2D
plt.rcParams['figure.figsize'] = (9,9)

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }
matplotlib.rcParams.update({'font.size': 18})
# -------------- khasanova-Frossard ------------------
equiv_error_KF = pickle.load(open('khasanova_frossard.pickle', 'rb'))
degree_step = {
    32: 3,
    64: 6,
    128: 12,
    256: 25}

bw = 64
lmax = bw
degrees = np.arange(0, lmax, degree_step[bw])
degrees = degrees[1:]
l1, = plt.loglog(degrees, equiv_error_KF[bw][1:], 'mv-')

bw = 128
lmax = bw
degrees = np.arange(0, lmax, degree_step[bw])
degrees = degrees[1:]
plt.loglog(degrees, equiv_error_KF[bw][1:], 'mx-', )

bw = 256
lmax = bw
degrees = np.arange(0, lmax, degree_step[bw])
degrees = degrees[1:]
plt.loglog(degrees, equiv_error_KF[bw][1:], 'mo-', )


# ----------------- healpix ----------------------
nsides = [32, 64, 128]

degree_step = {
            32: 10,
            64: 10,
            128: 50,
            256: 50,
            512: 100,
            1024: 200,
}

equiv_error_V1 = pickle.load(open('V1 - ||Lf||.pickle', 'rb'))
equiv_error_8 = pickle.load(open('V2 - 8 neighbors - ||Lf||.pickle', 'rb'))
equiv_error_20 = pickle.load(open('V2 - 20 neighbors - ||Lf||.pickle', 'rb'))
equiv_error_40 = pickle.load(open('V2 - 40 neighbors - ||Lf||.pickle', 'rb'))

nside = 32
lmax = 3*nside-1
degrees = np.arange(0, lmax+1, degree_step[nside])
degrees = degrees[1:]
l2, = plt.loglog(degrees, equiv_error_V1[nside][1:], 'gv-', label='V1')
l3, = plt.loglog(degrees, equiv_error_8[nside][1:], 'cv-', label='8 neighbors')
l4, = plt.loglog(degrees, equiv_error_20[nside][1:], 'rv-', label='20 neighbors')
l5, = plt.loglog(degrees, equiv_error_40[nside][1:], 'bv-', label='40 neighbors')

nside = 64
lmax = 3*nside-1
degrees = np.arange(0, lmax+1, degree_step[nside])
degrees = degrees[1:]
plt.loglog(degrees, equiv_error_V1[nside][1:], 'gx-', )
plt.loglog(degrees, equiv_error_8[nside][1:], 'cx-', )
plt.loglog(degrees, equiv_error_20[nside][1:], 'rx-', )
plt.loglog(degrees, equiv_error_40[nside][1:], 'bx-', )

nside = 128
lmax = 3*nside-1
degrees = np.arange(0, lmax+1, degree_step[nside])
degrees = degrees[1:]
plt.loglog(degrees, equiv_error_V1[nside][1:], 'go-')
plt.loglog(degrees, equiv_error_8[nside][1:], 'co-', )
plt.loglog(degrees, equiv_error_20[nside][1:], 'ro-', )
plt.loglog(degrees, equiv_error_40[nside][1:], 'bo-', )

# -------------- final parameters ------------------

plt.xlabel('Degree $\ell$', fontdict=font,)
plt.ylabel('Equivariance Error', fontdict=font, )
plt.tick_params(axis='both', which='major')
plt.grid()
plt.xlim([10,np.max(degrees)])
# plt.legend(prop={'size': 20})
ax =plt.gca()
legend_elements_1 = [Line2D([0], [0], color='m', marker='', markersize=8),
                     Line2D([0], [0], color='g', marker='', markersize=8),
                     Line2D([0], [0], color='c', marker='', markersize=8),
                   Line2D([0], [0], color='r', marker='', markersize=8),
                   Line2D([0], [0], color='b', marker='', markersize=8)]
# Add first legend:  only labeled data is included
leg1 = ax.legend(legend_elements_1,['Khasanova, Frossard','Perraudin et al.', 'This paper - 8 neighbors', 'This paper - 20 neighbors', 'This paper - 40 neighbors'], loc='lower left')
# Add second legend for the maxes and mins.
# leg1 will be removed from figure
legend_elements_2 = [Line2D([0], [0], color='k', marker='v', markersize=8),
                   Line2D([0], [0], color='k', marker='x', markersize=8),
                   Line2D([0], [0], color='k', marker='o', markersize=8)]

leg2 = ax.legend(legend_elements, ['$s=32$', '$s=64$', '$s=128$'],loc='upper right')
# Manually add the first legend back
ax.add_artist(leg1)
plt.tight_layout()
plt.savefig("all_in_one.pdf")
plt.show()

matplotlib.rcParams.update({'font.size': 10})
