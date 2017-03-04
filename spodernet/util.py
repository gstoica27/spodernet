import h5py


def numpy2hdf(path, data):
    '''Write a numpy array to a hdf5 file under the given path.'''
    h5file = h5py.File(path, "w")
    h5file.create_dataset("default", data=data)


def hdf2numpy(path, keyword='default'):
    '''Reads and returns a numpy array for a hdf5 file'''
    h5file = h5py.File(path, 'r')
    dset = h5file.get(keyword)
    return dset[:]


def load_hdf5_paths(paths, limit=None):
    data = []
    for path in paths:
        if limit != None:
            data.append(hdf2numpy(path)[:limit])
        else:
            data.append(hdf2numpy(path))
    return data