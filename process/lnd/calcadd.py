import yaml
with open("config.yml","r") as f:
    config = yaml.safe_load(f)
import os,sys
sys.path.append(f"{config['machine']['codepath']}")

import xarray as xr
import lib


def calcadd(fdir, var):
    if var=="ALBEDO_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/FSR_ICE.nc",f"{fdir}/FSDS.nc"], combine="nested")
            ALBEDO_ICE = ds["FSR_ICE"]/ds["FSDS"]
            ALBEDO_ICE.name = "ALBEDO_ICE"
            ALBEDO_ICE = ALBEDO_ICE.to_dataset()
            ALBEDO_ICE.encoding["unlimited_dims"] = "time"
            ALBEDO_ICE.to_netcdf(f"{fdir}/ALBEDO_ICE.nc")
            ALBEDO_ICE.close()
            ds.close()
        except:
            None

    if var=="ALBEDO":
        try:
            ds = xr.open_mfdataset([f"{fdir}/FSR.nc",f"{fdir}/FSDS.nc"], combine="nested")
            ALBEDO = ds["FSR"]/ds["FSDS"]
            ALBEDO.name = "ALBEDO"
            ALBEDO = ALBEDO.to_dataset()
            ALBEDO.encoding["unlimited_dims"] = "time"
            ALBEDO.to_netcdf(f"{fdir}/ALBEDO.nc")
            ALBEDO.close()
            ds.close()
        except:
            None 

    if var=="MELT_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/QSNOMELT_ICE.nc", f"{fdir}/QICE_MELT.nc"], combine="nested")
            MELT_ICE = ds["QSNOMELT_ICE"] + ds["QICE_MELT"]
            MELT_ICE.name = "MELT_ICE"
            MELT_ICE = MELT_ICE.to_dataset()
            MELT_ICE.encoding["unlimited_dims"] = "time"
            MELT_ICE.to_netcdf(f"{fdir}/MELT_ICE.nc")
            MELT_ICE.close()
            ds.close()
        except:
            None

    if var=="MELT":
        try:
            ds = xr.open_mfdataset([f"{fdir}/QSNOMELT.nc", f"{fdir}/QICE_MELT.nc"], combine="nested")
            MELT = ds["QSNOMELT"] + ds["QICE_MELT"]
            MELT.name = "MELT"
            MELT = MELT.to_dataset()
            MELT.encoding["unlimited_dims"] = "time"
            MELT.to_netcdf(f"{fdir}/MELT.nc")
            MELT.close()
            ds.close()
        except:
            None

    if var=="PRECIP_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/SNOW_ICE.nc", f"{fdir}/RAIN_ICE.nc"], combine="nested")
            PRECIP_ICE = ds["SNOW_ICE"] + ds["RAIN_ICE"]
            PRECIP_ICE.name = "PRECIP_ICE"
            PRECIP_ICE = PRECIP_ICE.to_dataset()
            PRECIP_ICE.encoding["unlimited_dims"] = "time"
            PRECIP_ICE.to_netcdf(f"{fdir}/PRECIP_ICE.nc")
            PRECIP_ICE.close()
            ds.close()
        except:
            None

    if var=="PRECIP":
        try:
            ds = xr.open_mfdataset([f"{fdir}/SNOW.nc", f"{fdir}/RAIN.nc"], combine="nested")
            PRECIP = ds["SNOW"] + ds["RAIN"]
            PRECIP.name = "PRECIP"
            PRECIP = PRECIP.to_dataset()
            PRECIP.encoding["unlimited_dims"] = "time"
            PRECIP.to_netcdf(f"{fdir}/PRECIP.nc")
            PRECIP.close()
            ds.close()
        except:
            None

    if var=="SMB_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/SNOW_ICE.nc", f"{fdir}/QSNOFRZ_ICE.nc", f"{fdir}/QSNOMELT_ICE.nc", f"{fdir}/QICE_MELT.nc", f"{fdir}/QSOIL_ICE.nc"], combine="nested")
            SMB_ICE = ds["SNOW_ICE"] + ds["QSNOFRZ_ICE"] - ds["QSNOMELT_ICE"] - ds["QICE_MELT"] - ds["QSOIL_ICE"]
            SMB_ICE.name = "SMB_ICE"
            SMB_ICE = SMB_ICE.to_dataset()
            SMB_ICE.encoding["unlimited_dims"] = "time"
            SMB_ICE.to_netcdf(f"{fdir}/SMB_ICE.nc")
            SMB_ICE.close()
            ds.close()
        except:
            None

    if var=="SMB":
        try:
            ds = xr.open_mfdataset([f"{fdir}/SNOW.nc", f"{fdir}/QSNOFRZ.nc", f"{fdir}/QSNOMELT.nc", f"{fdir}/QICE_MELT.nc", f"{fdir}/QSOIL.nc"], combine="nested")
            SMB = ds["SNOW"] + ds["QSNOFRZ"] - ds["QSNOMELT"] - ds["QICE_MELT"] - ds["QSOIL"]
            SMB.name = "SMB"
            SMB = SMB.to_dataset()
            SMB.encoding["unlimited_dims"] = "time"
            SMB.to_netcdf(f"{fdir}/SMB.nc")
            SMB.close()
            ds.close()
        except:
            None

    if var=="RUNOFF_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/QSNOMELT_ICE.nc", f"{fdir}/QICE_MELT.nc", f"{fdir}/RAIN_ICE.nc", f"{fdir}/QSNOFRZ_ICE.nc"], combine="nested")
            RUNOFF_ICE = ds["QSNOMELT_ICE"] + ds["QICE_MELT"] + ds["RAIN_ICE"] - ds["QSNOFRZ_ICE"]
            RUNOFF_ICE.name = "RUNOFF_ICE"
            RUNOFF_ICE = RUNOFF_ICE.to_dataset()
            RUNOFF_ICE.encoding["unlimited_dims"] = "time"
            RUNOFF_ICE.to_netcdf(f"{fdir}/RUNOFF_ICE.nc")
            RUNOFF_ICE.close()
            ds.close()
        except:
            None

    if var=="FSA_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/FSDS.nc", f"{fdir}/FSR_ICE.nc"], combine="nested")
            FSA_ICE = ds["FSDS"] - ds["FSR_ICE"]
            FSA_ICE.name = "FSA_ICE"
            FSA_ICE = FSA_ICE.to_dataset()
            FSA_ICE.encoding["unlimited_dims"] = "time"
            FSA_ICE.to_netcdf(f"{fdir}/FSA_ICE.nc")
            FSA_ICE.close()
            ds.close()
        except:
            None

    if var=="FIRA_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/FLDS_ICE.nc", f"{fdir}/FIRE_ICE.nc"], combine="nested")
            FIRA_ICE = ds["FLDS_ICE"] - ds["FIRE_ICE"]
            FIRA_ICE.name = "FIRA_ICE"
            FIRA_ICE = FIRA_ICE.to_dataset()
            FIRA_ICE.encoding["unlimited_dims"] = "time"
            FIRA_ICE.to_netcdf(f"{fdir}/FIRA_ICE.nc")
            FIRA_ICE.close()
            ds.close()
        except:
            None

    if var=="FIRA_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/FLDS.nc", f"{fdir}/FIRE_ICE.nc"], combine="nested")
            FIRA_ICE = ds["FLDS"] - ds["FIRE_ICE"]
            FIRA_ICE.name = "FIRA_ICE"
            FIRA_ICE = FIRA_ICE.to_dataset()
            FIRA_ICE.encoding["unlimited_dims"] = "time"
            FIRA_ICE.to_netcdf(f"{fdir}/FIRA_ICE.nc")
            FIRA_ICE.close()
            ds.close()
        except:
            None


    if var=="MELTHEAT_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/MELT_ICE.nc"], combine="nested")
            MELTHEAT_ICE = ds["MELT_ICE"] * 3.337e+5
            MELTHEAT_ICE.name = "MELTHEAT_ICE"
            MELTHEAT_ICE = MELTHEAT_ICE.to_dataset()
            MELTHEAT_ICE.encoding["unlimited_dims"] = "time"
            MELTHEAT_ICE.to_netcdf(f"{fdir}/MELTHEAT_ICE.nc")
            MELTHEAT_ICE.close()
            ds.close()
        except:
            None

    if var=="GHF_ICE":
        try:
            ds = xr.open_mfdataset([f"{fdir}/MELTHEAT_ICE.nc", f"{fdir}/FSA_ICE.nc", f"{fdir}/FIRA_ICE.nc", f"{fdir}/EFLX_LH_TOT_ICE.nc", f"{fdir}/FSH_ICE.nc"], combine="nested")
            GHF_ICE = ds["MELTHEAT_ICE"] - ds["FSA_ICE"] - ds["FIRA_ICE"] + ds["EFLX_LH_TOT_ICE"] + ds["FSH_ICE"]
            GHF_ICE.name = "GHF_ICE"
            GHF_ICE = GHF_ICE.to_dataset()
            GHF_ICE.encoding["unlimited_dims"] = "time"
            GHF_ICE.to_netcdf(f"{fdir}/GHF_ICE.nc")
            GHF_ICE.close()
            ds.close()
        except:
            None


def main():
    time = sys.argv[1]

    fdir = f"{config['run']['folder']}/{config['run']['name']}/lnd/hist/{time}"
    varlist = ["ALBEDO_ICE", "ALBEDO", "MELT_ICE", "MELT", "PRECIP_ICE", "PRECIP", "SMB_ICE", "SMB", "RUNOFF_ICE", "FSA_ICE", "FIRA_ICE", "MELTHEAT_ICE", "GHF_ICE"]

    for i in range(len(varlist)):
        var = varlist[i]
        print(var)
        if var is not None: calcadd(fdir, var)

main()
