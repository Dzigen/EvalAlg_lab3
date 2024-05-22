package lab2;

import org.uncommons.watchmaker.framework.factories.AbstractCandidateFactory;

import java.util.Random;

public class MyFactory extends AbstractCandidateFactory<double[]> {

    private int dimension;

    public MyFactory(int dimension) {
        this.dimension = dimension;
    }


    public double getRandomNumber( Random random, int min, int max) {
        return (random.nextDouble() * (max - min)) + min;
    }

    public double[] generateRandomCandidate(Random random) {
        double[] solution = new double[dimension];
        // x from -5.0 to 5.0

        // your implementation:
        for (int i = 0; i < this.dimension; i++) {
            solution[i] = getRandomNumber(random,-5, 5);
        }

        return solution;
    }
}

