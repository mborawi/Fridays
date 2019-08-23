package main

import (
	"bufio"
	"fmt"
	"math"
	"math/rand"
	"os"
)

func main() {
	r := rand.New(rand.NewSource(42))
	N := 400000000
	mu := 110000.92
	sig := 12000.4
	fname := "salaries.csv"
	f, err := os.Create(fname)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()
	w := bufio.NewWriter(f)
	defer w.Flush()
	fmt.Println("Saving data to file, this might take a while ( ~15 mins ), coffee time!")
	fmt.Fprintf(w, "salary1,salary2,salary3,salary4\n")
	fmt.Printf("Progress: ... 0.00%%")
	prgress := 1.0 // every 1%
	for i := 1; i <= N; i++ {
		percentage := float64(i) / float64(N) * float64(100)
		if math.Mod(percentage, prgress) == 0 {
			if percentage/prgress >= 10.0 {
				prgress = 10.0 // report progress every 10%
			}
			fmt.Printf("\033[2K\rProgress: ... %.1f%%", percentage)
		}

		// This is a practical programming exercise, not a stats subject!
		// Assume you do not have access to this source code.
		// try not to reverse engineer until u have coded a solution that works
		// Assume output csv file got given to you by your boss or interviewer
		// Now go write _your_own_code_ to find, max, min, mean, and stdev of one of the columns

		z1 := r.NormFloat64()*sig + mu
		z2 := r.NormFloat64()*sig*0.5 + mu*2
		z3 := r.NormFloat64()*sig*0.2 + mu*1.3
		z4 := r.NormFloat64()*sig*0.5 + mu*2
		fmt.Fprintf(w, "%.2f,%.2f,%.2f,%.2f\n", z1, z2, z3, z4)
	}
	fmt.Println("\nFinished saving data to csv file: ", fname)
}
