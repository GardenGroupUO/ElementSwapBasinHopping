#!/bin/bash -e
#SBATCH -J 140octa_cu25_cleri
#SBATCH -A nesi00401       # Project Account
#SBATCH --time=072:00:00     # Walltime
#SBATCH --ntasks=1 #number of nodes * tasks(12)
#SBATCH --mem-per-cpu=1500
#SBATCH --mail-user=annagarden@gmail.com         
#SBATCH --mail-type=ALL             
#SBATCH --hint=nomultithread  #no hyperthreading
##SBATCH --qos=debug

# We use ${CHK_DIR} instead of ${SCRATCH_DIR} so that the GBW file is
# preserved in the event that the job crashes or is killed by the scheduler.
thisdir=$(pwd -P)
CHK_DIR="/nesi/nobackup/nesi00401/monte-carlo"
workdir="${CHK_DIR}/${SLURM_JOB_NAME}-${SLURM_JOB_ID}"
mkdir -p "${workdir}"

cp * "${workdir}/."

# Go to the temporary working directory within ${CHK_DIR}
cd "${workdir}"

python ESBH_Run.py

# Delete temporary files and the temporary copy of the input file
#rm -rv *.tmp "${inputfile}"

# Copy all remaining files back to the starting directory, removing them from
# the working directory if the copy succeeds
#for file in *
#do
#    cp -arv "${file}" "${thisdir}" && rm -rv "${file}"
#done

#cd "${thisdir}"


