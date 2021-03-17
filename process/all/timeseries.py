import yaml
with open("config.yml","r") as f:
    config = yaml.safe_load(f)
import os,sys
sys.path.append(f"{config['machine']['codepath']}")

from mpi4py import MPI
import lib


def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    comp = sys.argv[1]
    comp = comp.split(",")
    times = sys.argv[2]
    times = times.split(",")

    fdir = []
    for c in comp:
        for seas in times:
            fdir.append([f"{config['run']['folder']}/{config['run']['name']}/{c}/hist/{seas}",seas])

    regions = config["timeseries"]["regions"]
    print("Making varlist")
    varlist = lib.mpimods.make_varlist3(fdir,regions)
    print("Done making varlist")
    varlist = lib.mpimods.check_varlist(varlist, size)

    for i in range(int(len(varlist)/size)):
        if rank==0:
            data = [(i*size)+k for k in range(size)]
        else:
            data = None
        data = comm.scatter(data, root=0)
        var = varlist[data]
        print(var)
        if var is not None: 
            try:
                lib.proc.ts(var[0], var[2], var[1], var[3])
            except:
                print("Error, continuing")

main()
