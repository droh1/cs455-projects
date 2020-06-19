/******************************************************************************
* File HW1.cpp
* Homework: CMSC 455 HW 1
* Author: Daniel Roh
*
*	Simulate a Estes 3 rocket launching to calculate the max height
*
******************************************************************************/
#include <iostream>
using namespace std;

int main(void) {
	bool test = true;
	const double g = 9.80665; //Gravity 
	const double Rho = 1.293; //Air density
	const double dt = 0.10; //Time step
	const double A = (0.000506 + 0.00496); //Surface Area (body + fins)
	const double impulse[20] = { 0, 6, 14.09, 5.6, 4.5, 4.5, 4.5, 4.3, 4.3, 4.24, 4.25, 4.25, 4.3, 4.25, 4.2, 4.3 , 4.3 ,4.2 , 4.0 ,0 };
	
	double t = 0, s = 0, v = 0, a = 0, F = 0, Ft = 0; //Time, Height, Velocity, Acceleration, Force (minus gravity), Thurst
	double m = (0.0340 + 0.0242); //Weight of rocket motor + fuel
	double Cd = (0.45 + 0.01); //Coeficient of drag (body + fins)

	cout << "Starting Simulation:" << endl;
	while (test == true) { //Until the rocket stops moving
		double Fd = (v * v);//Calculate FoD
		Fd = Fd * A;
		Fd = Fd * Rho;
		Fd = Fd * Cd;
		Fd = Fd / 2;

		//double Fd = (1 / 2) * Cd * Rho * A * (v * v); //This equation gives 0 for some reason

		double Fg = m * g; //Calculate FoG
		int x = (t * 10); //Get the array location at timestep
		if (x < 20) { //If the motor is spent or still going
			Ft = impulse[x];
		}
		else {
			Ft = 0;
		}

		double v2 = v * v; 
		v2 = v2 * 0.000506; //Force of drag by body
		v2 = v2 * Rho;
		v2 = v2 * 0.45;
		v2 = v2 / 2;

		double v1 = v * v;
		v1 = v1 * 0.00496; //Force of drag by fins
		v1 = v1 * Rho;
		v1 = v1 * 0.01;
		v1 = v1 / 2;
		
		//FdB = ((1 / 2) * 0.45 * Rho * 0.000506 * (v * v)); //Some reason this equation does not calcuate properly when placed together
		//FdF = ((1 / 2) * 0.01 * Rho * 0.00496 * (v * v)); 

		double temp = v2 + v1 + Fg;
		double F = Ft - temp; //Add the values for this later
		//double F = Ft - (FdB + FdF + Fg); 

		double a = F / m; //Calculate accelration 
		double dv = a * dt; //Calculate velocity change

		v = v + dv; //Get new velocity


		double ds = v * dt; //Calculate the distince mov
		s = s + ds; //Calculate the new hight

		if (m >= 0.0434) { //Check if all the fuel was burned
			m = m - 0.0001644 * Ft; //Removed fuel burned
		}

		t = t + dt; //Move time

		if ((v < 0.0) && (t > 1.9)) { //Check if the velocity is 0 and if the simulation is past 2 seconds
			test = false;
			break;
		}
		
		//cout << " t: " << t << "Fd: " << Fd << " Fg: " << Fg << " Ft: " << Ft << " F: " 
		//		<< F << " a: " << a << " dv: " << dv << " v: " << v << " ds: " << ds << " s: " << s << " m: " << m << endl; //DEBUG
		cout << "Time: " << t << " Height: " << s << " Velocity: " << v << " Acceleration: " << a << " Mass: " << m << endl;

	}
		
	
	cout << "Simulation Finished" << endl;
}
