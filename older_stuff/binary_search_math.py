from math import log, ceil

# With 1 probe, can only search a list of size 1.
# With 2 probes, can search a list of size 3.
# With 3 probes, can search a list of size 7.
# With 4 probes, can search a list of size 15.

# Therefore, N = 2^k - 1, 
#   where k = number of probes 
#   and N is the max size of the list.

# If the list is size N, what is the biggest number of probes k?
# k = [log2 (N + 1)] 
#   (square-only-on-top brackets, or ceiling brackets, mean round 
#    up to the nearest integer)

# If there are 1000 elements to search through, what is
# the maximum number of probes that'll be needed?

max_probes = ceil(log(1000+1, 2))
print("Probes needed for a thousand items: {0}".format(max_probes))

max_probes = ceil(log(1000000+1, 2))
print("Probes needed for a million items: {0}".format(max_probes))

max_probes = ceil(log(1000000000+1, 2))
print("Probes needed for a billion items: {0}".format(max_probes))