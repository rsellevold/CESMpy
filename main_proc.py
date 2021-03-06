import yaml
with open("config.yml","r") as f:
    config = yaml.safe_load(f)

scripts = ["process/all/hist.py <components>",
           "process/atm/calcadd.py",
           "process/lnd/calcadd.py",
           "process/lnd/masks.py",
           "process/all/avg_day2mon.py <components>",
           "process/all/avg_mon2ann.py <components>",
           "process/all/avg_mon2seas.py <components>",
           "process/all/timeseries.py <components> <time>",
           "process/all/trends.py <components> <time>",
           "process/all/timeseries_masks.py <components> <time> <path-to-mask>",
           "process/climateind.py <tasks>"]

nproc = config["machine"]["nproc"]

procfile = open("main_proc","w")

# Add machine directives
procfile.write("#!/bin/bash\n\n")
for i in range(len(config["machine"]["directive"])-1):
	procfile.write(f"{config['machine']['directive'][0]} {config['machine']['directive'][i+1]}\n")
procfile.write("\n")

procfile.write(f"source {config['machine']['condaact']} {config['machine']['condaenv']}\n\n")

for i in range(len(scripts)):
    if config["machine"]["mpi"]:
        if scripts[i] == "process/atm/calcadd":
            procfile.write(f"mpiexec -n 1 python {config['machine']['codepath']}/{scripts[i]}\n")
        elif scripts[i] == "process/lnd/calcadd":
            procfile.write(f"mpiexec -n 1 python {config['machine']['codepath']}/{scripts[i]}\n")
        else:
            procfile.write(f"mpiexec -n {config['machine']['nproc']} python {config['machine']['codepath']}/{scripts[i]}\n")

    else:
        procfile.write(f"python {config['machine']['codepath']}/{scripts[i]}\n")
