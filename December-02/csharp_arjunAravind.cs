using System;

class SimTriangles {

    public float[] GetSides() {
        float[] sides = new float[3];
        int iter;

        for(iter=0; iter<3; iter++) {
            Console.Write("Enter a side --> ");
            sides[iter] =Convert.ToSingle(Console.ReadLine());
        }

        return sides;
    }

    public float[] GetAngles() {
        float[] angles = new float[3];
        int iter;

        for(iter=0; iter<3; iter++) {
            Console.Write("Enter an angle --> ");
            angles[iter] = Convert.ToSingle(Console.ReadLine());
        }

        if( (angles[0]+angles[1]+angles[2]) != 180) {
            Console.Write("You have entered incorrect values. Try again!\n\n");
            return GetAngles();
        }

        return angles;
    }

    public void swap(ref float num1, ref float num2){
	num1 = num1 + num2;
	num2 = num1 - num2;
	num1 = num1 - num2;
    }

    public void printArray(float[] sides1, float[] sides2) {
        Console.Write("{0},{1},{2} and ", sides1[0], sides1[1], sides1[2]);
        Console.Write("{0},{1},{2}\n", sides2[0], sides2[1], sides2[2]);
    }

    public bool SSSisValid(float[] sides1, float[] sides2) {
        int iter;
        
        //We just need to iterate every possible combination
        //of the side1 array

        for(iter=0; iter<3; iter++) {
            int iter2 = 2;

            //printArray(sides1,sides2);

            //Check for ratio equality
            float ratio1 = sides1[0] / sides2[0];
            float ratio2 = sides1[1] / sides2[1];
            float ratio3 = sides1[2] / sides2[2];

            if (ratio1 == ratio2 && ratio2 == ratio3)
                return true;

            //Let's swap the stuff
	    swap(ref sides1[iter2], ref sides1[iter2-1]);

            iter2--;

            //printArray(sides1, sides2);

            //Check for ratio equality
            ratio1 = sides1[0] / sides2[0];
            ratio2 = sides1[1] / sides2[1];
            ratio3 = sides1[2] / sides2[2];

            if (ratio1 == ratio2 && ratio2 == ratio3)
                return true;

            //We swap again
	    swap(ref sides1[iter2], ref sides1[iter2-1]);
        }

        return false;
    }
    
    public bool SASisValid(float[] sides1, float[] sides2, float[] angles1, float[] angles2) {
        int iter;

        //We just need to iterate every possible combination
        //of the side1 array

        for (iter = 0; iter < 3; iter++) {
            int iter2 = 2;

            //printArray(sides1,sides2);

            //Check for ratio equality
            float ratio1 = sides1[0] / sides2[0];
            float ratio2 = sides1[1] / sides2[1];
            float ratio3 = sides1[2] / sides2[2];

            if (ratio1 == ratio2 && angles1[0] == angles1[1])
                return true;
            else if (ratio2 == ratio3 && angles1[1] == angles1[1])
                return true;
            else if (ratio1 == ratio3 && angles1[2] == angles2[2])
                return true;

            //Let's swap the stuff
	    swap(ref sides1[iter2], ref sides1[iter2-1]);
	    swap(ref angles1[iter2], ref angles1[iter2-1]);

            iter2--;

            //printArray(sides1, sides2);

            //Check for ratio equality
            ratio1 = sides1[0] / sides2[0];
            ratio2 = sides1[1] / sides2[1];
            ratio3 = sides1[2] / sides2[2];

            if (ratio1 == ratio2 && angles1[0] == angles1[1])
                return true;
            else if (ratio2 == ratio3 && angles1[1] == angles1[1])
                return true;
            else if (ratio1 == ratio3 && angles1[2] == angles2[2])
                return true;

            //We swap again
	    swap(ref sides1[iter2], ref sides1[iter2-1]);
	    swap(ref angles1[iter2], ref angles1[iter2-1]);
        }

        return false;
    }

    public bool AAAisValid(float[] angles1, float[] angles2) {
        int iter;

        for (iter = 0; iter < 3; iter++) {
            int iter2 = 2;

            if (angles1[0] == angles2[0] && angles1[1] == angles2[1])
                return true;
            else if (angles1[1] == angles2[1] && angles1[2] == angles2[2])
                return true;
            else if (angles1[2] == angles2[2] && angles1[0] == angles2[0])
                return true;

            //Let's swap the stuff
	    swap(ref angles1[iter2], ref angles1[iter2-1]);

            iter2--;
            
            if (angles1[0] == angles2[0] && angles1[1] == angles2[1])
                return true;
            else if (angles1[1] == angles2[1] && angles1[2] == angles2[2])
                return true;
            else if (angles1[2] == angles2[2] && angles1[0] == angles2[0])
                return true;

            //We swap again
	    swap(ref angles1[iter2], ref angles1[iter2-1]);
        }

        return false;
    }

}

public class TriangleCheck {
    public static void Main() {
        SimTriangles sim = new SimTriangles();

        float[] sides1 = sim.GetSides();
        float[] sides2 = sim.GetSides();

        float[] angles1 = sim.GetAngles();
        float[] angles2 = sim.GetAngles();

        if (sim.SSSisValid(sides1, sides2)) {
            Console.Write("They are similar triangles by SSS!");
        }
        else if (sim.SASisValid(sides1, sides2, angles1, angles2)) {
            Console.Write("They are similar triangles by SAS!");
        }
        else if (sim.AAAisValid(angles1, angles2)) {
            Console.Write("They are similar triangles by AAA!");
        }
        else {
            Console.Write("They are not similar triangles!");
        }

        Console.ReadKey();
            
    }
}
