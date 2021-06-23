from CrackBox import Black_Box_Function
import numpy as np

class GA:
    def __init__(self, chromosome_size=16, population=200, cross_prob=0.9, muta_prob=0.3):
        self.crack = Black_Box_Function("input2.txt", "output2.txt", "2-6.exe")
        self.chromosome_size = chromosome_size
        self.population = population
        self.cross_prob = cross_prob
        self.muta_prob = muta_prob

    def create_generation(self):
        chromosome = np.random.randint(high=2, low=0, size=self.chromosome_size)
        all_solution = np.empty((0, len(chromosome)))

        for i in range(self.population):
            np.random.shuffle(chromosome)
            all_solution = np.vstack((all_solution, chromosome))

        return all_solution

    #Function from black box
    def f(self, decode_x1, decode_x2):
        return self.crack.getFunction(decode_x1, decode_x2)

    #Objective Function
    def getObjective(self, chromosome):
        lb_x = -2
        ub_x = 2
        len_x = len(chromosome)//2
        precision_x = (ub_x - lb_x)/(2**len_x - 1)

        z = 0
        t = 1
        x_bit = 0
        x1_bit_sum = 0

        for i in range(len(chromosome)//2):
            x_bit = chromosome[-t]*(2**z)
            x1_bit_sum += x_bit
            z += 1
            t += 1
        
        z = 0
        t = 1 + len(chromosome)//2
        x_bit = 0
        x2_bit_sum = 0

        for i in range(len(chromosome)//2):
            x_bit = chromosome[-t]*(2**z)
            x2_bit_sum += x_bit
            z += 1
            t += 1

        decode_x1 = (x1_bit_sum) * precision_x + lb_x
        decode_x2 = (x2_bit_sum) * precision_x + lb_x

        return (decode_x1, decode_x2, self.f(decode_x1, decode_x2))

    #Tournament selection
    def find_parents_ts(self, all_solution):
        parents = np.empty((0, np.size(all_solution, 1)))

        for i in range(2):
            indices_list = np.random.choice(len(all_solution), 3, replace=False)

            posb_parent_1 = all_solution[indices_list[0]]
            posb_parent_2 = all_solution[indices_list[1]]
            posb_parent_3 = all_solution[indices_list[2]]

            obj_func_parent_1 = self.getObjective(posb_parent_1)[2]
            obj_func_parent_2 = self.getObjective(posb_parent_2)[2]
            obj_func_parent_3 = self.getObjective(posb_parent_3)[2]

            min_obj_func = min(obj_func_parent_1, obj_func_parent_2, obj_func_parent_3)

            if min_obj_func == obj_func_parent_1:
                selected_parent = posb_parent_1
            elif min_obj_func == obj_func_parent_2:
                selected_parent = posb_parent_2
            else:
                selected_parent = posb_parent_3
                
            parents = np.vstack((parents, selected_parent))
        
        parent_1 = parents[0,:]
        parent_2 = parents[1,:]

        return (parent_1, parent_2)

    #Crossover
    def crossover(self, parent_1, parent_2):
        cross_prob=self.cross_prob

        chlid_1 = np.empty((0, len(parent_1)))
        chlid_2 = np.empty((0, len(parent_2)))

        cross_rand_prob = np.random.rand()

        if cross_rand_prob < cross_prob:

            index_1 = np.random.randint(0, len(parent_1))
            index_2 = np.random.randint(0, len(parent_2))

            while index_1 == index_2:
                index_2 = np.random.randint(0, len(parent_2))

            if index_1 > index_2:
                index_1, index_2 = index_2, index_1
            
            #Parent_1
            first_sec_par_1 = parent_1[:index_1]
            mid_sec_par_1 = parent_1[index_1:index_2+1]
            last_sec_par_1 = parent_1[index_2+1:]
            
            #Parent_2
            first_sec_par_2 = parent_2[:index_1]
            mid_sec_par_2 = parent_2[index_1:index_2+1]
            last_sec_par_2 = parent_2[index_2+1:]

            chlid_1 = np.concatenate((first_sec_par_1, mid_sec_par_2, last_sec_par_1))
            chlid_2 = np.concatenate((first_sec_par_2, mid_sec_par_1, last_sec_par_2))

        else:
            chlid_1 = parent_1
            chlid_2 = parent_2

        return (chlid_1, chlid_2)

    def mutation(self, chlid_1, chlid_2):
        muta_prob=self.muta_prob

        #Chlid_1
        mutated_chlid_1 = np.empty((0, len(chlid_1)))

        t = 0
        for i in chlid_1:
            muta_rand_prob = np.random.rand()

            if muta_rand_prob < muta_prob:

                if chlid_1[t] == 0:
                    chlid_1[t] = 1
                else:
                    chlid_1[t] = 0

                mutated_chlid_1 = chlid_1
                t += 1

            else:
                mutated_chlid_1 = chlid_1
                t += 1

        #Chlid_2
        mutated_chlid_2 = np.empty((0, len(chlid_2)))

        t = 0
        for i in chlid_2:
            muta_rand_prob = np.random.rand()

            if muta_rand_prob < muta_prob:

                if chlid_2[t] == 0:
                    chlid_2[t] = 1
                else:
                    chlid_2[t] = 0

                mutated_chlid_2 = chlid_2
                t += 1
            
            else:
                mutated_chlid_2 = chlid_2
                t += 1

        return (mutated_chlid_1, mutated_chlid_2)