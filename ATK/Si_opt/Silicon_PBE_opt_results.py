# %% Load BulkConfiguration

silicon__hybrid_band_bulk_configuration_0 = nlread(
    filename=r'E:\Stucture\Silicon_Hybrid_band.hdf5',
    object_id='BulkConfiguration_0'
)[0]


# %% Set PlaneWaveCalculator

# %% PlaneWaveCalculator

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = GGA.PBE

#----------------------------------------
# PAW Data Set
#----------------------------------------
basis_set = [
    PAWPBESuggested.Silicon,
    ]

k_point_sampling = KpointDensity(
    density_a=4.0*Angstrom,
    density_b=4.0*Angstrom,
    density_c=4.0*Angstrom
)

numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling
)

iteration_control_parameters = IterationControlParameters(
    tolerance=1e-06
)

calculator = PlaneWaveCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    checkpoint_handler=NoCheckpointHandler
)

nlsave('Silicon_Hybrid_opt_results.hdf5', calculator)


# %% Set Calculator

silicon__hybrid_band_bulk_configuration_0.setCalculator(calculator)

nlsave('Silicon_Hybrid_opt_results.hdf5', silicon__hybrid_band_bulk_configuration_0)


# %% OptimizeGeometry

restart_strategy = RestartFromTrajectory(
    trajectory_filename='Silicon_Hybrid_opt_results.hdf5',
    object_id='optimize_trajectory'
)

optimized_configuration = OptimizeGeometry(
    configuration=silicon__hybrid_band_bulk_configuration_0,
    max_forces=0.015*eV/Angstrom,
    constraints=[
        BravaisLatticeConstraint()
    ],
    trajectory_filename='Silicon_Hybrid_opt_results.hdf5',
    trajectory_object_id='optimize_trajectory',
    restart_strategy=restart_strategy
)

nlsave('Silicon_Hybrid_opt_results.hdf5', optimized_configuration)
