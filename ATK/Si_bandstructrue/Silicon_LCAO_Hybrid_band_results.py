# %% Load BulkConfiguration

silicon_pbe_opt_results_bulk_configuration_1 = nlread(
    filename=r'E:\Stucture\Silicon_PBE_opt_results.hdf5',
    object_id='BulkConfiguration_1'
)[0]


# %% Set LCAOCalculator

# %% LCAOCalculator

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = HybridGGA.HSE06

k_point_sampling = KpointDensity(
    density_a=4.0*Angstrom,
    density_b=4.0*Angstrom,
    density_c=4.0*Angstrom
)

numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling
)

iteration_control_parameters = IterationControlParameters(
    tolerance=1e-05
)

calculator = LCAOCalculator(
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    checkpoint_handler=NoCheckpointHandler
)


# %% Set Calculator

silicon_pbe_opt_results_bulk_configuration_1.setCalculator(calculator)

silicon_pbe_opt_results_bulk_configuration_1.update()

nlsave('Silicon_LCAO_PBE_band_2_results.hdf5', silicon_pbe_opt_results_bulk_configuration_1)


# %% Bandstructure

bandstructure = Bandstructure(
    configuration=silicon_pbe_opt_results_bulk_configuration_1,
    route=['G', 'X', 'W', 'L', 'G', 'K', 'X'],
    points_per_segment=41
)
nlsave('Silicon_LCAO_PBE_band_2_results.hdf5', bandstructure)
