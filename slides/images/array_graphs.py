import dask.array as da

kwargs = {'bgcolor': '#00000000',
          'rankdir': 'BT',
          'node_attr': {'color': 'white',
                        'fontcolor': '#FFFFFF',
                        'penwidth': '3'},
          'edge_attr': {'color': 'white', 'penwidth': '3'}}

x = da.ones((15, 15), chunks=(5, 5))

x.mean(split_every=10).visualize('array-mean.svg', **kwargs)

#x.sum(axis=1).visualize('array-sum.svg', **kwargs)
#(x + x.T).visualize('array-xxT.svg', **kwargs)
#(x.dot(x.T + 1)).visualize('array-xdotxT.svg', **kwargs)
#(x.dot(x.T + 1) - x.mean()).visualize('array-xdotxT-mean.svg', **kwargs)
#(x.dot(x.T + 1) - x.mean()).std().visualize('array-xdotxT-mean-std.svg', **kwargs)
