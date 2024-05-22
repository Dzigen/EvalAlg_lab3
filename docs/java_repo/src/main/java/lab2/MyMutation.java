package lab2;

import org.uncommons.watchmaker.framework.EvolutionaryOperator;

import java.util.List;
import java.util.Random;
import java.util.stream.IntStream;
import java.lang.Math;

public class MyMutation implements EvolutionaryOperator<double[]> {
    public List<double[]> apply(List<double[]> population, Random random) {
        // initial population
        // need to change individuals, but not their number!

        // your implementation:

        // shuffle population indexes to pick randomly candidates for mutation
        int[] cand_idxs = IntStream.rangeClosed(0, population.size()).toArray();
        for (int i = 0; i < cand_idxs.length; i++) {
            int randomIndexToSwap = random.nextInt(cand_idxs.length);
            int temp = cand_idxs[randomIndexToSwap];
            cand_idxs[randomIndexToSwap] = cand_idxs[i];
            cand_idxs[i] = temp;
        }
        // make mutation for first "mutation_percent" candidates in shuffled list
        int cand_mutations_percent = 50;
        int cand_mutations_amount = (population.size() * cand_mutations_percent) / 100;
        int cand_dimension = 2;
        int gene_mutations_percent = 20;
        int gene_mutations_amount = (cand_dimension * gene_mutations_percent) / 100;

        for (int i = 0; i < cand_mutations_amount; i++){
            double[] modif_candidate = population.get(cand_idxs[i]);
            int mutated_genes = 0;
            for (int j = 0; j < cand_dimension; j++) {
                boolean is_mutate = random.nextBoolean();
                if (is_mutate && Math.abs(modif_candidate[j]) < 5) {
                    modif_candidate[j] = (modif_candidate[j] + random.nextGaussian()) % 5;
                    mutated_genes++;
                }

                if (mutated_genes >= gene_mutations_amount)
                    break;
            }
            population.set(cand_idxs[i], modif_candidate);
        }

        //result population
        return population;
    }
}
