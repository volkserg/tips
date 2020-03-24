import matplotlib.pyplot as plt
import matplotlib

def print_matrix(c, classes=['','1', '2', '3', '4', '5', '6', '7']):
    fig, ax = plt.subplots(figsize=(11,11))
    
    norm =np.empty(np.array(c).shape)
    for (i, j), z in np.ndenumerate(c):
        norm[i][j] = c[i][j]/sum(c[i])
    ax.matshow(norm, cmap='Wistia',  aspect='auto')
    
#     classes =  ['','1', '2']
#    classes =  ['','1', '2', '3', '4', '5', '6', '7']
    ax.set_xticklabels(classes)
    ax.set_yticklabels(classes)
    for (i, j), z in np.ndenumerate(c):
        p = 100*z/sum(c[i])
        ax.text(j, i, '{0}\n{1:.2f}%'.format(z, p) if i==j else '{}'.format(z), ha='center', va='center')
