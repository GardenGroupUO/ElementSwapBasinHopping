#!/bin/bash -e

#SBATCH --job-name        acceptor_o_ph_conf_1  
#SBATCH --account         uoo03267
#SBATCH --time            01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12 # or fewer. ORCA is inefficient with ntasks > 16
#SBATCH --mem-per-cpu     3G
#SBATCH --mail-user=annagarden@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --partition=large        # specify a partition
#SBATCH --output=%x-%j.out      # %x and %j are replaced by job name and ID
#SBATCH --error=%x-%j.err
module load  ORCA/4.0.1-OpenMPI-2.0.2
orca_exe=$(which orca)

# We use ${CHK_DIR} instead of ${SCRATCH_DIR} so that the GBW file is
# preserved in the event that the job crashes or is killed by the scheduler.
thisdir=$(pwd -P)
CHK_DIR="/nesi/nobackup/uoo03273/orca_temp"
workdir="${CHK_DIR}/${SLURM_JOB_NAME}-${SLURM_JOB_ID}"
mkdir -p "${workdir}"
inputfile="conf_1.inp"
cp "${inputfile}" "${workdir}/."

# Go to the temporary working directory within ${CHK_DIR}
cd "${workdir}"

${orca_exe} "${inputfile}" #> "${outputfile}"

# Delete temporary files and the temporary copy of the input file
#rm -rv *.tmp "${inputfile}"

# Copy all remaining files back to the starting directory, removing them from
# the working directory if the copy succeeds
for file in *
do
    cp -arv "${file}" "${thisdir}" && rm -rv "${file}"
done

cd "${thisdir}"
