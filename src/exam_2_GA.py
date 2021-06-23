import numpy as np
from matplotlib import pyplot as plt
from Genetic_Algorithm import GA
import time

GA_model = GA(chromosome_size=16, population=200, cross_prob=0.9, muta_prob=0.3)

population = GA_model.population
generation = 100
x1_x2_chrom = GA_model.create_generation()[0]
pool_of_solution = GA_model.create_generation()
best_of_a_generation = np.empty((0, len(x1_x2_chrom)+1))

start_time = time.time()
gen = 1

print(pool_of_solution)

for i in range(generation):
    new_population = np.empty((0, len(x1_x2_chrom)))
    new_population_with_obj_value = np.empty((0, len(x1_x2_chrom)+1))
    sorted_best_for_plotting = np.empty((0, len(x1_x2_chrom)+1))

    print(f"\n\nGeneration {gen}#")

    family = 1

    for j in range(int(population/2)):
        print(f"\nfamily {family}#")

        parent_1 = GA_model.find_parents_ts(pool_of_solution)[0]
        parent_2 = GA_model.find_parents_ts(pool_of_solution)[1]
        
        chlid_1 = GA_model.crossover(parent_1, parent_2)[0]
        chlid_2 = GA_model.crossover(parent_1, parent_2)[1]

        muta_chlid_1 = GA_model.mutation(chlid_1, chlid_2)[0]
        muta_chlid_2 = GA_model.mutation(chlid_1, chlid_2)[1]

        obj_val_muta_chlid_1 = GA_model.getObjective(muta_chlid_1)[2]
        obj_val_muta_chlid_2 = GA_model.getObjective(muta_chlid_2)[2]

        print()
        print(f"Obj_value_for_mutated_chlid #1 at generation #{gen} : {obj_val_muta_chlid_1}")
        print(f"Obj_value_for_mutated_chlid #2 at generation #{gen} : {obj_val_muta_chlid_2}")

        mutated_1_with_obj_val = np.hstack((obj_val_muta_chlid_1, muta_chlid_1))
        mutated_2_with_obj_val = np.hstack((obj_val_muta_chlid_2, muta_chlid_1))

        new_population = np.vstack((new_population, muta_chlid_1, muta_chlid_2))

        new_population_with_obj_value = np.vstack((new_population_with_obj_value,
                                                    mutated_1_with_obj_val, 
                                                    mutated_2_with_obj_val))

        family += 1
    
    pool_of_solution = new_population
    
    sorted_best_for_plotting = np.array(sorted(new_population_with_obj_value,
                                                key=lambda x:x[0]))
    
    best_of_a_generation = np.vstack((best_of_a_generation,
                                        sorted_best_for_plotting[0]))

    gen += 1

