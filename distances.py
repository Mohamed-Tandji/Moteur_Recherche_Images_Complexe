import numpy as np
from scipy.spatial import distance


def manhattan_distance(v1,v2):
    """s_summary_
    Compute the Manhattan distance between v1 and v2.
    dist=sum(|x_i-y_i|)
    dist=distance.cityblock(v1,v2)
    Args:
        v1 (_type_): Description .
        v2 (_type_):  Description."""
    return np.sum(np.abs(np.array(v1)-np.array(v2).astype(float)))


def euclidean_distance(v1,v2):
    """s_summary_
    Compute the Manhattan distance between v1 and v2.
    dist=sqrt(sum(|x_i-y_i|))**2
    Args:
        v1 (_type_): query image signature .
        v2 (_type_):  offline signature."""
    return np.sqrt(np.sum((np.abs(np.array(v1)-np.array(v2).astype(float)))**2)) # Erreur possibles


def chebyshev_distance(v1,v2):
    """s_summary_
    Compute the Manhattan distance between v1 and v2.
    dist=max(|x_i-y_i|)
    dist=distance.chebyshev(v1,v2)
    Args:
        v1 (_type_): Description .
        v2 (_type_):  Description."""
    return np.max(np.abs(np.array(v1)-np.array(v2).astype(float)))

def canberra_distance(v1,v2):
    """s_summary_
    Compute the Manhattan distance between v1 and v2.

    Args:
        v1 (_type_): Description . 
        v2 (_type_):  Description."""
    return distance.canberra(v1,v2) 

def retrieve_similar_images(features_db,query_features,distance,num_results):
    distances=[]
    for instance in features_db:
        features,label,img_path =instance[:-2],instance[-2],instance[-1]
        if distance=='euclidean':
            dist=euclidean_distance(query_features,features)
        if distance=='manhattan':
            dist=manhattan_distance(query_features,features)
        if distance=='chebyshev':
            dist=chebyshev_distance(query_features,features)
        if distance=='canberra':
            dist=canberra_distance(query_features,features)
            
        distances.append((dist,label,img_path))
    distances.sort(key=lambda x:x[0])
    return distances[:num_results]
